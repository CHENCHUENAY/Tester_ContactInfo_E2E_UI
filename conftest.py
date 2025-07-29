



import os
import pytest
import base64
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html import extras

# Local imports (these point to elements on the login page and test data)
from pages.login_page import LoginPageLocators
from utils.test_data import LoginData


# This fixture opens the browser before each test and closes it after
# @pytest.fixture(scope="module")
# def setup_teardown():
#     # Start Chrome browser using webdriver manager
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#
#     # Open the login page
#     driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
#     driver.implicitly_wait(10)
#
#     # Log into the app using test data
#     driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginData.login_email)
#     driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.login_password)
#     driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
#
#     # Give the driver to the test, then quit after
#     yield driver
#     driver.quit()




import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPageLocators
from utils.test_data import LoginData

@pytest.fixture(scope="module")
def setup_teardown():
    # Setup Chrome options for headless CI environments
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')  # Needed for CI
    options.add_argument('--disable-dev-shm-usage')  # Fix shared memory crash
    options.add_argument('--disable-gpu')  # Avoid GPU in headless
    options.add_argument('--remote-debugging-port=9222')  # Prevent crash
    options.add_argument('--disable-software-rasterizer')  # Fix for some CI crashes

    # Start WebDriver with the options above
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.implicitly_wait(10)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")

    # Perform login before yielding
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginData.login_email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.login_password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    yield driver
    driver.quit()



# This adds screenshots to HTML report if a test fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Wait for the test to finish
    outcome = yield
    result = outcome.get_result()

    # Only take screenshot if the test failed
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup_teardown")

        if driver:
            # Make sure screenshots folder exists
            os.makedirs("screenshots", exist_ok=True)

            # Create a filename with the test name and time
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"

            # Take the screenshot
            driver.save_screenshot(screenshot_path)

            # Read the screenshot and convert it to base64
            with open(screenshot_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode()

            # Add the screenshot to the report
            image_html = f'<img src="data:image/png;base64,{image_base64}" width="400" height="250">'
            extra = getattr(result, "extra", [])
            extra.append(extras.html(image_html))
            result.extra = extra