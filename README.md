## Selenium이란?
웹 브라우저를 자동으로 조작해서 테스트할 수 있게 해주는 오픈소스 자동화 도구

## 구성요소
Selenium WebDriver: 브라우저(Chrome, Edge 등)를 실제로 제어하는 핵심 도구
Selenium IDE: 간단한 녹화 기반 자동화 도구
Selenium Grid: 여러 환경에서 병렬 테스트 실행

## 특징
파이썬, 자바, 자바스크립트 등 여러 언어를 지원

## 설치과정
1. 파이썬 설치, VS Code 실행
2. 터미널 창에 python -m pip install selenium 입력
* -m : 모듈 실행
* pip : 파이썬 라이브러리 설치 모듈
* 초기 설치 시 인터넷 연결되어 있는지 확인 필요

## 문법
1. driver.find_element(By.ID, "TestId").send_keys("test")
=> ID가 "TestId"인 입력 칸을 찾아 "test"라는 글자를 입력
By.ID           : id 값으로 찾기
By.CLASS_NAME   : class 이름으로 찾기
By.NAME         : name 속성으로 찾기
By.TAG_NAME     : 태그 이름으로 찾기
By.CSS_SELECTOR : CSS 문법으로 찾기

2. driver.get()
=> 페이지 열기

3. .click()
=> 클릭
