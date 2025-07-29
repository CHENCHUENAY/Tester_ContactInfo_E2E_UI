










import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random

# Local imports for page locators and test data
from pages.login_page import LoginPageLocators
from pages.dashboard_page import DashboardPageLocators
from pages.contacts_page import ContactPageLocators
from utils.test_data import PositiveData
from utils.test_data import NegativeData



class TestPositiveFlow:
    @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.positive
    def testPositiveFlowE2E(self, setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance

        # Navigate to the 'Add Contact' form
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()

        # Fill in the form with valid data from test data file
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        driver.find_element(*ContactPageLocators.EMAIL).send_keys(*PositiveData.email)
        driver.find_element(*ContactPageLocators.PHONE).send_keys(*PositiveData.gen_phone)
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)         
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        # Pause and validate if contact was created successfully
        time.sleep(5)
        assert PositiveData.gen_phone in driver.page_source
        print('phone checked here')
        print(PositiveData.gen_phone)

        # Click on the created contact and go to edit page
        driver.find_element(*DashboardPageLocators.select_contact_by_phone(PositiveData.gen_phone)).click()
        driver.find_element(*ContactPageLocators.EDIT_CONTACT_BUTTON).click()

        wait = WebDriverWait(driver, 10)

        # Wait until form fields are populated before clearing and updating them
        wait.until(lambda d: d.find_element(*ContactPageLocators.FIRST_NAME).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.FIRST_NAME).clear()
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys("Enay")

        wait.until(lambda d: d.find_element(*ContactPageLocators.LAST_NAME).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.LAST_NAME).clear()
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys("Kumarzz")

        wait.until(lambda d: d.find_element(*ContactPageLocators.BIRTHDATE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.BIRTHDATE).clear()
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)

        wait.until(lambda d: d.find_element(*ContactPageLocators.EMAIL).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.EMAIL).clear()
        driver.find_element(*ContactPageLocators.EMAIL).send_keys("EnayTest@fake.com")

        wait.until(lambda d: d.find_element(*ContactPageLocators.PHONE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.PHONE).clear()
        driver.find_element(*ContactPageLocators.PHONE).send_keys(*PositiveData.gen_phone)

        wait.until(lambda d: d.find_element(*ContactPageLocators.STREET1).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STREET1).clear()
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)

        wait.until(lambda d: d.find_element(*ContactPageLocators.STREET2).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STREET2).clear()
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)

        wait.until(lambda d: d.find_element(*ContactPageLocators.CITY).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.CITY).clear()
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)

        wait.until(lambda d: d.find_element(*ContactPageLocators.STATE_PROVINCE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).clear()
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)

        wait.until(lambda d: d.find_element(*ContactPageLocators.POSTAL_CODE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.POSTAL_CODE).clear()
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)

        wait.until(lambda d: d.find_element(*ContactPageLocators.COUNTRY).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.COUNTRY).clear()
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)

        # Submit the updated contact form
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        # Wait for changes and validate update
        time.sleep(5)
        assert 'Kumarzz' in driver.page_source

        # Return back to contacts list
        driver.find_element(*ContactPageLocators.RETURN_BUTTON).click()

        wait.until(EC.presence_of_element_located((By.XPATH, "(//td[contains(text(),'enaytest@fake.com')])")))
        email_displayed = driver.find_element(By.XPATH, "(//td[contains(text(),'enaytest@fake.com')])").text

        # Ensure updated contact is listed correctly
        assert email_displayed == "enaytest@fake.com"
        print('updated contact is displayed in the list ')
        time.sleep(2)


class TestNegativeFlow:
    @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.negativeEmpty
    def test_missing_required_fields(self, setup_teardown):
        driver = setup_teardown

        # Try submitting an empty form
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error_message = driver.find_element(By.ID, "error").text.strip()

        # Validate error message for missing fields
        assert error_message == "Contact validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required."
        print("Captured error:", error_message)

    @pytest.mark.negativeEmail
    def test_invalid_email_format(self, setup_teardown):
        driver = setup_teardown

        # Submit form with an invalid email address
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        driver.find_element(*ContactPageLocators.EMAIL).send_keys("chenchuenay.com")  # Invalid format
        driver.find_element(*ContactPageLocators.PHONE).send_keys(*PositiveData.gen_phone)
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error = driver.find_element(By.ID, "error").text.strip()

        # Validate error message for invalid email
        assert error == "Contact validation failed: email: Email is invalid"
        print("Captured error:", error)

    @pytest.mark.negativePhone
    def test_invalid_phone_number(self, setup_teardown):
        driver = setup_teardown

        # Submit form with invalid phone number
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        driver.find_element(*ContactPageLocators.EMAIL).send_keys(*PositiveData.email)
        driver.find_element(*ContactPageLocators.PHONE).send_keys("99999")  # Invalid phone
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error = driver.find_element(By.ID, "error").text.strip()

        # Validate error message for phone number
        assert error == "Contact validation failed: phone: Phone number is invalid"
        print("Captured error:", error)

    @pytest.mark.negativePostal
    def test_invalid_postal_code(self, setup_teardown):
        driver = setup_teardown

        # Submit form with invalid postal code
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        driver.find_element(*ContactPageLocators.EMAIL).send_keys(*PositiveData.email)
        driver.find_element(*ContactPageLocators.PHONE).send_keys(*PositiveData.gen_phone)
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)         #error
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys("7")  # Invalid postal code
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error = driver.find_element(By.ID, "error").text.strip()

        # Validate error message for postal code
        assert error == "Contact validation failed: postalCode: Postal code is invalid"
        print("Captured error:", error)


class TestDeleteRecords:
    @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.delete
    def test_delete_all_contacts(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 10)

        while True:
            try:
                # Locate all data rows in the table (skip header)
                rows = driver.find_elements(By.XPATH, "//table//tr[position()>1]")
                if len(rows) == 0:
                    print("All records cleared.")
                    break

                # Click the first data cell of the first row
                rows[0].find_element(By.XPATH, "./td[2]").click()

                # Wait for delete button and click it
                wait.until(EC.presence_of_element_located(ContactPageLocators.DELETE_BUTTON))
                driver.find_element(*ContactPageLocators.DELETE_BUTTON).click()

                # Accept confirmation alert
                driver.switch_to.alert.accept()

                # Wait until the row is removed from DOM
                wait.until(EC.staleness_of(rows[0]))

            except Exception as e:
                print(f"Error occurred: {e}")




