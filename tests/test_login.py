import time
import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

from pages.login_page import LoginPage


# 엑셀 파일 읽기
data = pd.read_excel("login_data.xlsx")


# driver 생성/종료 관리
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://dongeui09.dothome.co.kr/login.html")
    yield driver
    driver.quit()


# 엑셀 데이터를 한 줄씩 반복 실행
@pytest.mark.parametrize("user_id,user_pw,expected", data.values)
def test_login(driver, user_id, user_pw, expected):

    login_page = LoginPage(driver)

    # 로그인 동작 수행
    login_page.enter_id(user_id)
    login_page.enter_pw(user_pw)
    login_page.click_login()
    
    time.sleep(3)  # 3초 대기
    
    # 결과 검증
    if expected == "success":
        assert "로그아웃" in driver.page_source
    else:
        try:
            # alert 전환
            alert = driver.switch_to.alert
            alert_text = alert.text   # alert 문구 가져오기
            alert.accept()            # 확인 버튼 클릭
            # 실제 alert 문구 검증
            assert "로그인 실패!" in alert_text
        except NoAlertPresentException:
            # alert가 없으면 실패 처리
            assert False, "로그인 실패인데 alert가 뜨지 않았음"
