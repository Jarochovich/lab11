import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get("http://localhost:3000")
    assert "React" in driver.title

def test_learn_react_link(driver):
    driver.get("http://localhost:3000")
    link = driver.find_element(By.LINK_TEXT, "Learn React")
    assert link.is_displayed()

def test_logo_exists(driver):
    driver.get("http://localhost:3000")
    logo = driver.find_element(By.CLASS_NAME, "App-logo")
    assert logo.is_displayed()

def test_page_contains_text(driver):
    driver.get("http://localhost:3000")
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Edit" in body_text or "React" in body_text