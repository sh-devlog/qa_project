# Selenium이란?
웹 브라우저를 자동으로 조작해서 테스트할 수 있게 해주는 오픈소스 자동화 도구<br>
파이썬, 자바, 자바스크립트 등 여러 언어 지원<br>
#### < 구성요소 >
Selenium WebDriver: 브라우저(Chrome, Edge 등)를 실제로 제어하는 핵심 도구<br>
Selenium IDE: 간단한 녹화 기반 자동화 도구<br>
Selenium Grid: 여러 환경에서 병렬 테스트 실행<br>
#### < 설치과정 >
1. 파이썬 설치, VS Code 실행
2. 터미널 창에 python -m pip install selenium 입력
* -m : 모듈 실행
* pip : 파이썬 라이브러리 설치 모듈
* 초기 설치 시 인터넷 연결되어 있는지 확인 필요<br>
#### < 문법 >
1. driver.find_element(By.ID, "TestId").send_keys("test")<br>
=> ID가 "TestId"인 입력 칸을 찾아 "test"라는 글자를 입력<br>
* By.ID           : id 값으로 찾기
* By.CLASS_NAME   : class 이름으로 찾기
* By.NAME         : name 속성으로 찾기
* By.TAG_NAME     : 태그 이름으로 찾기
* By.CSS_SELECTOR : CSS 문법으로 찾기<br>
2. driver.get()<br>
=> 페이지 열기<br>
3. .click()<br>
=> 클릭<br><br>

# Page Object Model (POM)
페이지를 하나의 클래스(객체)로 만들어서 관리하는 설계 방식
