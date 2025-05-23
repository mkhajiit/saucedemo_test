from helper.helper_login import helper_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 로그인 후 메뉴 열고 클릭하는 헬퍼 함수
def open_menu_and_click(driver,menu_id):\

  burger_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
  burger_button.click()

    
    # 해당 메뉴 항목 클릭 가능할 때까지 기다리고, 자바스크립트 클릭으로 클릭 처리
  menu_link = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, menu_id))
    )
  driver.execute_script("arguments[0].click();", menu_link)