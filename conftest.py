import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# local imports
from pages.login_page import LoginPageLocators
from utils.test_data import LoginData




# Fixture for setup and teardown
@pytest.fixture(scope="module")
def setup_teardown():
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    driver.implicitly_wait(10)  # Implicit wait for elements to load

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginData.login_email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.login_password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
    yield driver  # Yield control to the test function
    driver.quit()
























