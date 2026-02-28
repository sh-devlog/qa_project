from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_id(self, user_id):
        self.driver.find_element(By.NAME, "id").send_keys(user_id)

    def enter_pw(self, user_pw):
        self.driver.find_element(By.NAME, "pw").send_keys(user_pw)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='로그인']").click()
