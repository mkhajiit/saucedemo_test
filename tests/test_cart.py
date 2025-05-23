import pytest
from helper.helper_login import helper_login
from helper.helper_add_to_cart import add_to_cart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

selected_items=[
  ("add-to-cart-sauce-labs-backpack", "Sauce Labs Backpack"),
  ("add-to-cart-sauce-labs-bike-light", "Sauce Labs Bike Light"),
  ("add-to-cart-sauce-labs-bolt-t-shirt","Sauce Labs Bolt T-Shirt")
]

# 테스트 코드
def test_cart_add_to_cart(driver): # 장바구니 상품 추가 테스트
  helper_login(driver,"standard_user","secret_sauce")
  add_to_cart(driver,selected_items)

  cart_items = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
  cart_item_names = [item.text for item in cart_items] # 리스트 컴프리헨션

  # 클릭한 상품명이 장바구니에 전부 존재하는지 검증
  for _, expected_name in selected_items:
    assert expected_name in cart_item_names, f"{expected_name} 이 카트에 없으므로 기능이 오작동"
  
def test_cart_remove_from_cart(driver): # 장바구니 상품 제거 테스트
  helper_login(driver,"standard_user","secret_sauce")
  add_to_cart(driver,selected_items)

  wait = WebDriverWait(driver, 10)
  btn = wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
  btn.click()

  assert not driver.find_elements(By.ID,"remove-sauce-labs-backpack"),"아직 제품이 카트에 남아있습니다."

def test_cart_checkout_empty(driver): # 미입력으로 checkout
  helper_login(driver,"standard_user","secret_sauce")
  add_to_cart(driver,selected_items)

  checkout_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
  )

  checkout_button.click()
  
  continue_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "continue"))
  )

  continue_button.click()

  error_container = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
  )
  
  error_text = error_container.find_element(By.TAG_NAME, "h3").text
  assert error_text == "Error: First Name is required"