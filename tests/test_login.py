import pytest
import time
from helper.helper_login import helper_login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pytest 설정
@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")  # 창 안 띄우고 백그라운드에서 실행
  options.add_argument("--no-sandbox") # 보안 격리 기능(sandbox)을 끈다
  options.add_argument("--disable-dev-shm-usage") # /dev/shm 대신 일반 디스크를 사용하게 해서 안정성이 높아진다

  # ChromeDriver 자동 설치
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)

  yield driver # 테스트 함수에 driver 객체를 전달한다
  driver.quit() # 테스트가 끝난 뒤 자동으로 실행되어 크롬 브라우저를 종료 시킨다

# 테스트 코드 작성
def test_login_success(driver): # 로그인 성공 TC-01-03
  helper_login(driver,"standard_user","secret_sauce") # 로그인 헬퍼 함수
  assert "inventory" in driver.current_url, "로그인 후 URL에 'inventory'가 포함되어야 합니다."

def test_login_fail_empty(driver): # 로그인 실패 TC-01-01
  helper_login(driver,"","") # 로그인 헬퍼 함수
  
  error_message = driver.find_element(By.CSS_SELECTOR,".error-message-container.error h3")
  assert error_message.text == "Epic sadface: Username is required"

def test_login_fail_different(driver): # 로그인 실패 TC-01-02
  helper_login(driver,"standard_user","1234") # 로그인 헬퍼 함수

  error_message = driver.find_element(By.CSS_SELECTOR,".error-message-container.error h3")
  assert error_message.text == "Epic sadface: Username and password do not match any user in this service"