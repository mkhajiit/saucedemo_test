from selenium.webdriver.common.by import By

# 로그인 헬퍼 함수
def helper_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()