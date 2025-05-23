from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def add_to_cart(driver,selected_items):

  for button_id, _ in selected_items:
    driver.find_element(By.ID,button_id).click()

  driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

  # # 장바구니 페이지에 있는 상품명 추출
  # WebDriverWait(driver, 5).until(
  #     EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
  # )

  