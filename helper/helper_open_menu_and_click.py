from helper.helper_login import helper_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 로그인 후 메뉴 열고 클릭하는 헬퍼 함수
def open_menu_and_click(driver,menu_id):\

  # 메뉴 열기
  burger_button = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
  )
  burger_button.click()

  # 요소가 존재하고 visible될 때까지 기다림
  WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, menu_id))
  )

  # 새로 찾기 (중간에 stale 되지 않게)
  menu_link = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, menu_id))
  )

  # JavaScript로 클릭
  driver.execute_script("arguments[0].click();", menu_link)