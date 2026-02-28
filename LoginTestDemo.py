from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# 브라우저 열기 (Chrome)
driver = webdriver.Chrome()

# 브라우저 열기 (Edge)
# driver = webdriver.Edge()

# 사이트 접속
driver.get("http://dongeui09.dothome.co.kr/login.html")

# 아이디 입력
driver.find_element(By.NAME, "id").send_keys("t")
# 비밀번호 입력
driver.find_element(By.NAME, "pw").send_keys("t")
# 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "input[value='로그인']").click()


# alert 객체 가져오기
#alert = driver.switch_to.alert

# 결과값 확인 위해 3->10초 대기로 임시 변경
time.sleep(10)



# 결과 메시지 출력
# alert 텍스트 가져오기 (로그인 실패 시)
#message = alert.text
#print("로그인 결과:", message)
# 확인 버튼 클릭
#alert.accept()

# 브라우저 종료
driver.quit()
