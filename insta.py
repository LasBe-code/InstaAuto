from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
import sys
import time
import random

form_class = uic.loadUiType("insta.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_hashtag.clicked.connect(self.addList_hashtag)
        self.btn_hashtag_del.clicked.connect(self.removeItem_hashtag)
        self.btn_dm.clicked.connect(self.addList_dm)
        self.btn_dm_del.clicked.connect(self.removeItem_dm)
        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)

    def sleep(self, x):
        loop = QEventLoop()
        x = int(x*2000)
        QTimer.singleShot(x, loop.quit)
        loop.exec_()

    def qwer(self, total, noyangsim): #텍스트에디터 글 추가
        t = str(total)
        n = str(noyangsim)
        y = str(total - noyangsim)
        a = ('성공 : '+ y +  ' ㅣ 실패 : '+ n + ' ㅣ total : '+ t) 
        a = str(a)
        print(a)
        self.textbox.append(a)

    def addList_hashtag(self) :
        self.list_hashtag.addItem(self.line_hashtag.text())
    def removeItem_hashtag(self) :
        #ListWidget에서 현재 선택한 항목을 삭제할 때는 선택한 항목의 줄을 반환한 후, takeItem함수를 이용해 삭제합니다. 
        self.removeItemRow = self.list_hashtag.currentRow()
        self.list_hashtag.takeItem(self.removeItemRow)

    def addList_dm(self) :
        self.list_dm.addItem(self.line_dm.text())         
    def removeItem_dm(self) :
        self.removeItemRow = self.list_dm.currentRow()
        self.list_dm.takeItem(self.removeItemRow)

    def stop(self):
        self.__init__()

    def start(self) :
        insta_id = self.line_id.text()  #아이디
        insta_pw = self.line_pw.text()  #비밀번호
        insta_c = 80   #한 해시태그 반복횟수
        total = 1   #돌린 횟수
        noyangsim = 0 #실패
        total_want = int(self.line_cycle.text())   #돌릴 횟수
        i = 0
            
        insta_hashtag = [self.list_hashtag.item(t).text() for t in range(self.list_hashtag.count())]   #해시태그

        insta_cm = [self.list_dm.item(y).text() for y in range(self.list_dm.count())]

        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://instagram.com')
        self.sleep(3)

        e = driver.find_elements_by_class_name('_2hvTZ')[0]
        e.send_keys(self.line_id.text()) #아이디
        e = driver.find_elements_by_class_name('_2hvTZ')[1]
        e.send_keys(self.line_pw.text()) #비밀번호
        e.send_keys(Keys.ENTER)
        self.sleep(3)
        e = driver.find_elements_by_class_name('sqdOP')[1] #계정저장
        e.click()
        self.sleep(3)
        e = driver.find_elements_by_class_name('aOOlW')[1] #알람설정
        e.click()
        self.sleep(3) 

        while(total != total_want):
        
            try:
                e = driver.find_elements_by_class_name('pbgfb')[0]  #해시태그 검색
                e.click()
                e = driver.find_elements_by_class_name('XTCLo')[0]  #동적페이지 대응
                e.send_keys(random.choice(insta_hashtag))
                self.sleep(random.randint(3, 10))  
                e = driver.find_elements_by_class_name('-qQT3')[0] #검색 목록 중 첫번째 클릭
                e.click()                #해시태그 검색
                self.sleep(random.randint(3, 10))  

                for i in range(insta_c):
                    if total % 20 == 0:
                        self.textbox.append('------대휴식------')
                        self.sleep(500)
                    i += random.randint(2, 4)
                    print(i)
                    e = driver.find_elements_by_class_name('_9AhH0')[9+i]
                    e.click()                    #인기 게시물 건너뛰고 일반 게시물 클릭

                    try:                         
                        self.sleep(random.randint(3, 10)) 
                        xpath = "//article/header/div[2]/div[1]/div[1]/span/a"
                        e=driver.find_element_by_xpath(xpath)
                        e.click()               
                    except:                      #삭제 된 게시물일 경우 초기상태로 돌아가 반복문 처음부터 재실행
                        text = ('[삭제 된 게시물]')
                        text = str(text)
                        self.textbox.append(text)
                        noyangsim += 1
                        xpath = "/html/body/div[5]/div[3]/button"
                        e=driver.find_element_by_xpath(xpath) #창 닫기
                        e.click()
                        total += 1
                        self.qwer(total, noyangsim)
                        continue

                    self.sleep(random.randint(3, 10))  

                    try:    #팔로우 수가 1000단위가 넘어가면 , 가 숫자 변환에 오류를 줘서 replace로 콤마 제거
                        follower = float(driver.find_elements_by_class_name('g47SY')[1].text.replace(",", "")) 
                        following = float(driver.find_elements_by_class_name('g47SY')[2].text.replace(",", ""))
                        yangsim = following / follower          #팔로잉/팔로워 수치 계산
                        follow = ('팔로워 : '+ str(follower) +' ㅣ 팔로잉 : '+ str(following)+' ㅣ 양심수치 : '+ str(yangsim))
                        follow = str(follow)
                        self.textbox.append(follow)
                        
                    except: #10000단위는 포기
                        driver.back()
                        driver.back()
                        total += 1
                        noyangsim += 1
                        print('실패2')
                        text = ('[대상의 팔로워 혹은 팔로잉 수가 너무 많습니다]')
                        text = str(text)
                        self.textbox.append(text)
                        self.qwer(total, noyangsim)
                        continue
                    
                    if yangsim < 0.8 :                      #노양심 뒤로가기 두번 해야됨
                        self.textbox.append('[양심이 없습니다.]')
                        noyangsim += 1
                        total += 1
                        self.qwer(total, noyangsim)
                        driver.back()
                        driver.back()
                        self.sleep(random.randint(3, 10))
                        continue

                    else:
                        xpath = "//section/main//div[1]/div[1]/div/div/div/span/span[1]/button"
                        e=driver.find_element_by_xpath(xpath) #팔로우 버튼 찾기
                        # e = driver.find_elements_by_class_name('sqdOP')[0]
                        e_text = e.text
                        if e_text != '팔로우':                #팔로우 되어있을 시 뒤로가기
                            self.textbox.append('[이미 팔로우 되어있습니다.]')
                            total += 1
                            noyangsim += 1
                            driver.back() 
                            driver.back()
                            self.sleep(random.randint(3, 10))

                        else:
                            e.click()
                            self.sleep(random.randint(3, 10)) 
                            e = driver.find_elements_by_class_name('_9AhH0')[0] #첫 번째 게시물 클릭
                            e.click()
                            cnt = random.randint(3, 5)

                            for j in range(cnt):  #좋아요 작업
                                self.sleep(random.randint(3, 5)) 
                                if random.randint(0, 1) != 1:      #좋아요 가챠
                                    try:
                                        e = driver.find_elements_by_class_name('_65Bje')[0] #다음 게시물
                                        e.click()
                                    except:
                                        break #예외처리 : 다음 게시물이 없으면 브레이크
                                else:
                                    e = driver.find_elements_by_class_name('fr66n')[0] #좋아요 클릭
                                    e.click()
                                    self.sleep(1)
                                    try:
                                        e = driver.find_elements_by_class_name('_65Bje')[0] #다음 게시물
                                        e.click()
                                    except:
                                        break #예외처리 : 다음 게시물이 없으면 브레이크      
                            
                            xpath = "/html/body/div[5]/div[3]/button"
                            e=driver.find_element_by_xpath(xpath) #창 닫기
                            e.click()

                            self.sleep(3) 
                            element = driver.find_element_by_tag_name('body') #위로 스크롤
                            element.send_keys(Keys.PAGE_UP)

                            self.sleep(random.randint(3, 5)) 
                            e = driver.find_elements_by_class_name('sqdOP')[0] #DM 버튼 클릭
                            e.click()

                            self.sleep(random.randint(3, 5)) 
                            xpath = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"
                            e=driver.find_element_by_xpath(xpath) #DM 텍스트 박스
                            e.click()
                            e.send_keys(random.choice(insta_cm)) #DM 코맨트 입력
                            e.send_keys(Keys.ENTER)

                            self.sleep(2) 
                            
                            for q in range(4+cnt): #뒤로가기
                                driver.back()
                                self.sleep(0.5)

                            total += 1
                            self.textbox.append('[성공]')
                            self.qwer(total, noyangsim)
                            
                            self.sleep(random.randint(3, 10)+10)
            
            except:
                self.textbox.append('#############오류로 인한 재실행#############')
                self.sleep(15)
                driver.refresh()  #새로고침
                i = 0
                self.sleep(random.randint(3, 10)+3) 
                continue

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()