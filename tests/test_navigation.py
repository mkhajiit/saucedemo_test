import pytest
import time
from helper.helper_open_menu_and_click import open_menu_and_click
from helper.helper_login import helper_login
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
def test_navigation_all_items(driver): # all items 선택
  helper_login(driver,"standard_user","secret_sauce")
  open_menu_and_click(driver,"inventory_sidebar_link")
  time.sleep(2)

  assert "/inventory.html" in driver.current_url

def test_navigation_about(driver): # about 선택
  helper_login(driver,"standard_user","secret_sauce")
  open_menu_and_click(driver,"about_sidebar_link")

  time.sleep(2)

  assert "saucelabs.com" in driver.current_url

def test_navigation_reset_app_state(driver): # reset_app_state 선택
  helper_login(driver,"standard_user","secret_sauce")

  driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
  driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

  open_menu_and_click(driver,"reset_sidebar_link")

  time.sleep(2)

  # 목록에 있는 클래스 버튼들의 클래스명이 btn btn_primary btn_small btn_inventory 가 아닌게 있으면 안된다를 조건으로 걸기
  expected_class = "btn btn_primary btn_small btn_inventory"
  buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")

  for btn in buttons:
    actual_class = btn.get_attribute("class")
    assert actual_class == expected_class, f"클래스명이 다릅니다: {actual_class}"
  

  