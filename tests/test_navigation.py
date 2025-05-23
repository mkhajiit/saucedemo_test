import pytest
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
  options.add_argument("--headless")  
  options.add_argument("--no-sandbox") 
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--window-size=1920,1080")

  # ChromeDriver 자동 설치
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)

  yield driver 
  driver.quit()

# 테스트 코드
def test_navigation_all_items(driver): # all items 선택
  helper_login(driver,"standard_user","secret_sauce")
  open_menu_and_click(driver,"inventory_sidebar_link")

  assert "/inventory.html" in driver.current_url

def test_navigation_about(driver): # about 선택
  helper_login(driver,"standard_user","secret_sauce")
  open_menu_and_click(driver,"about_sidebar_link")

  assert "saucelabs.com" in driver.current_url

@pytest.mark.xfail(reason="일부러 실패하도록 설계된 테스트입니다.")
def test_navigation_reset_app_state(driver): # reset_app_state 선택(일부러 실패하도록 구성한 테스트 케이스)
  helper_login(driver,"standard_user","secret_sauce")

  driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
  driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

  open_menu_and_click(driver,"reset_sidebar_link")

  # 목록에 있는 클래스 버튼들의 클래스명이 btn btn_primary btn_small btn_inventory 가 아닌게 있으면 안된다를 조건으로 걸기
  expected_class = "btn btn_primary btn_small btn_inventory"
  buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")

  for btn in buttons:
    actual_class = btn.get_attribute("class")
    assert actual_class == expected_class, f"클래스명이 다릅니다: {actual_class}"
# 에러 발생: all items 목록에서는 reset이 발생하지 않았음

@pytest.mark.xfail(reason="일부러 실패하도록 설계된 테스트입니다.")
def test_navigation_swag_labs(driver): # swag_labs 클릭(일부러 실패하도록 구성한 테스트 케이스)
  helper_login(driver,"standard_user","secret_sauce")
  driver.find_element(By.CLASS_NAME,"app_logo").click()

  try:
    assert "/home.html" in driver.current_url
  except AssertionError as e:
    raise AssertionError(f"[홈 화면이 아닙니다]에러 메시지: {e}.")
# 에러 발생: 로고를 클릭해도 링크가 없어서 home 화면으로 이동하지 않음(home 화면이 미구현 되어 있음)