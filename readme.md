# InstaAuto

# ⚡️InstaAuto

인스타그램 계정을 운영하다 반복적인 작업을 자동화하고 싶어 시작한 토이 프로젝트입니다.

파이썬 + 셀레니움을 이용해 제작하였고 소통 및 팔로우를 위한 알고리즘을 제작 및 지속적으로 수정했습니다.

테스트 계정으로 테스트해보며 인스타그램측 벤을 회피하기 위해 알고리즘을 계속해서 개선했고, 어느정도 완성되었을 때, 본 계정으로 개인적인 컨텐츠만 올리고 다른 사람들과의 소통은 프로그램으로 자동화를 돌려 목표였던 1k 팔로워를 달성했습니다.

제작 후 편리하게 사용하기 위해 PyQT를 이용해 GUI를 구성하였고 패키징하여 직접 사용해보고 지인들에게 배포하였습니다.

**제작기간 : 2021.04.06 ~ 2021.04.10**

# 📌 사용 기술 & 개발 환경

- Python
- Selenium
- PyQT
- ChromeDriver
- Windows 10
- VSCode

# 📌 키워드

- 파이썬과 셀레니움을 이용해 웹 데이터 크롤링 기술 학습
- 프로그램 작동 현황에 대한 로그를 TextView로 출력해 이용자가 직관적으로 확인
- PyQT를 이용한 GUI 구성으로 사용성 증가
- 제작부터 패키징 배포 및 수정에 대한 전반적인 경험

# 📌 Troubleshooting

```python
time.sleep()
```

페이지 전환 과정에서 봇 의심을 피하고 페이지 로딩시간과 명령어의 타이밍을 맞춰주기 위해 중간중간 휴식시간을 주었습니다. 이 메소드는 GUI 환경에서 쓰레드를 멈추게 해 어떠한 조작도 할 수 없게 만들었습니다.

```python
def sleep(self, x): 
	loop = QEventLoop() 
	x = int(x*2000) 
	QTimer.singleShot(x, loop.quit) 
	loop.exec_()
```

프로그램이 대기시간을 갖는 도중에도 GUI를 조작할 수 있도록 위와 같이 PyQT용 QTimer를 이용해 해결했습니다.

# 📌 참고 자료

[**제작 일지**](https://lasbe.tistory.com/3)

![InstaAuto.jpg](InstaAuto%20dcd7b59684fa442abe93a50e10e16f81/InstaAuto.jpg)
