import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pytest fixture 설정
@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  options.add_argument("--no-sandbox") # 보안 격리 기능(sandbox)을 끈다
  options.add_argument("--disable-dev-shm-usage") # /dev/shm 대신 일반 디스크를 사용하게 해서 안정성이 높아진다

  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)

  yield driver
  driver.quit()

# 테스트 코드
def test_logout(driver):
  driver.get("https://www.saucedemo.com/")

  # 로그인
  driver.find_element(By.ID,"user-name").send_keys("standard_user")
  driver.find_element(By.ID, "password").send_keys("secret_sauce")
  driver.find_element(By.ID, "login-button").click()

  # 메뉴 열고 로그아웃
  driver.find_element(By.ID,"react-burger-menu-btn").click()

  # '로그아웃' 버튼이 클릭 가능한 상태가 될 때까지 기다리지 않으면 에러가 발생함
  WebDriverWait(driver, 5).until(
      EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
  )

  driver.find_element(By.ID,"logout_sidebar_link").click()

  assert "saucedemo.com" in driver.current_url