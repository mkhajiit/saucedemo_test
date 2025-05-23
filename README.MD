# 🧪 SauceDemo 자동화 테스트 프로젝트

- 테스트 대상: [https://www.saucedemo.com/](https://www.saucedemo.com/)
- 사용 기술: Python, Selenium, Pytest

---

## 📂 프로젝트 개요

SauceDemo 사이트를 대상으로 로그인, 로그아웃 등 주요 기능에 대해 작성한 테스트 케이스를 토대로 Selenium을 이용해 자동화 테스트를 진행합니다.

---

## 🐞 문제 상황 및 해결 과정

### 1번 문제

`test_logout.py` 파일에서 로그아웃 테스트 중 다음과 같은 에러가 발생하였습니다:
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable

### 원인

- 메뉴가 완전히 열리기 전에 로그아웃 버튼을 클릭하려 하여 에러 발생.
- 요소가 렌더링되기 전이거나 애니메이션이 끝나기 전이라 상호작용할 수 없는 상태였음.

### 해결 방법

- 요소가 **클릭 가능한 상태가 될 때까지 대기**하도록 `WebDriverWait`을 사용하여 수정함.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)
```

### 코드 상세 설명

• WebDriverWait(driver, 5)

    • driver: Selenium WebDriver 인스턴스

    • 5: 최대 5초 동안 대기

        • 조건이 더 빨리 만족되면 바로 다음 코드로 넘어감

        • 조건 미충족시 5초 후 TimeoutException 발생

• .until(...)

    • 괄호 안 조건이 만족될 때까지 기다림

    • 만족 시 바로 통과하여 다음 줄 실행

• EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))

    • EC는 expected_conditions의 약자, 미리 정의된 조건 모음

    • element_to_be_clickable: 요소가 화면에 보이고 클릭 가능한 상태인지 확인

    • (By.ID, "logout_sidebar_link"): ID가 "logout_sidebar_link"인 요소를 찾음

### 2번 문제

`test_navigation.py` 파일에서 네비게이션 메뉴 테스트 중 에러가 발생:
햄버거 메뉴를 클릭 이후 다음 클릭부터 작동을 하지 않는 문제

### 원인

- 사이드 메뉴 내부 항목들은 보이는 것 같아도, CSS 애니메이션(transform)이 끝나기 전까지는 물리적으로 클릭할 수 없는 상태이기 때문
- Selenium은 이런 "보이지만, 클릭 불가능한 위치"를 검사하지 않기 때문에, 결국 .click()이 실패하거나 무시되게 됩니다.

### 해결 방법

- 요소가 **클릭 가능한 상태가 될 때까지 대기**하도록 `WebDriverWait`을 사용하고 driver.execute_script 로 자바스크립트로 강제 클릭을 해서 해결

```python

driver.find_element(By.ID, "react-burger-menu-btn").click()

menu_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, menu_id))
  )
driver.execute_script("arguments[0].click();", menu_link)

```

### 코드 상세 설명

• driver.execute_script("arguments[0].click();", element)

    • "arguments[0]"는 두 번째 인자로 넘긴 element를 가리킵니다.

    • 이 자바스크립트는 그 요소를 클릭하는 동작을 수행합니다.

### 3번 문제

headless 없이 브라우저를 띄워서 테스트할때 크롬 비밀번호 변경 팝업으로 코드 실행 안되는 문제

해결: headless를 키거나 브라우저 띄워서 테스트 할때는 time.sleep을 주고 팝업을 꺼줘야함

### 4번 문제

타임아웃 에러는 보통 브라우저 환경때문에 ui테스트에서 자주 발생하니 재실행 시켜주면 된다

### 5번 문제

headless 모드 일때만 에러가 발생하는 문제
Selenium의 불안정한 headless 모드 문제 playwright 학습하자
