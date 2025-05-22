# 🧪 SauceDemo 자동화 테스트 프로젝트

- **테스트 대상**: [https://www.saucedemo.com/](https://www.saucedemo.com/)
- **사용 기술**: Python, Selenium, Pytest

---

## 📂 프로젝트 개요

SauceDemo 사이트를 대상으로 로그인, 로그아웃 등 주요 기능에 대해 Selenium을 이용해 자동화 테스트를 진행합니다.

---

## 🐞 문제 상황 및 해결 과정

### 문제 발생

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

📘 코드 상세 설명
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
