import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options)
    return chrome_browser

def test_button_exists(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.XPATH, "//input[@name='submit']").is_displayed()

def test_checkbox_exists(browser):
    browser.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    assert browser.find_element(By.XPATH, "//input[@name='checkbox']").is_displayed()