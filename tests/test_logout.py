import pytest
import time
from helper.helper_login import helper_login
from helper.helper_open_menu_and_click import open_menu_and_click
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
  helper_login(driver,"standard_user","secret_sauce")
  open_menu_and_click(driver,"logout_sidebar_link")
  
  assert "https://www.saucedemo.com/" in driver.current_url