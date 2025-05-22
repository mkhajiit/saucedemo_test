import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pytest 설정
@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  # options.add_argument("--headless")  
  options.add_argument("--no-sandbox") 
  options.add_argument("--disable-dev-shm-usage") 

  # ChromeDriver 자동 설치
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)

  yield driver 
  driver.quit() 

# 테스트 코드
def test_navigation_all_items(driver):
  