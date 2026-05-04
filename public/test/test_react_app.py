import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Настройка браузера для CI/CD (обязательно Headless режим)"""
    options = Options()
    options.add_argument('--headless')  # Ключевой момент для GitHub Actions [citation:3]
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_page_title(driver):
    """Простой тест: открыть React-приложение и проверить заголовок"""
    driver.get("http://localhost:3000")
    assert "React" in driver.title