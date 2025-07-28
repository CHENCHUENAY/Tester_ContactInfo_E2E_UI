import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


import random


'''Local imports'''
from pages.login_page import LoginPageLocators
from pages.dashboard_page import DashboardPageLocators
from pages.contacts_page import ContactPageLocators
from utils.test_data import PositiveData
from utils.test_data import NegativeData





class TestPositiveFlow:
    @pytest.mark.usefixtures("setup_teardown")
    def testPositiveFlowE2E(self, setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance

        # we are at dashboard now
        # Click to add new contact
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        # Fill out the create form
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

        # Wait and validate contact creation
        time.sleep(5)
        assert PositiveData.gen_phone in driver.page_source
        print('phone checked here')
        print(PositiveData.gen_phone)

        '''UPDATION PART'''
        # Click on the created contact and go to edit page
        driver.find_element(*DashboardPageLocators.select_contact_by_phone(PositiveData.gen_phone)).click()
        driver.find_element(*ContactPageLocators.EDIT_CONTACT_BUTTON).click()

        wait = WebDriverWait(driver, 10)

        # Clear and update each field with explicit wait for non-empty value

        # First Name
        wait.until(lambda d: d.find_element(*ContactPageLocators.FIRST_NAME).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.FIRST_NAME).clear()
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys("Enay")

        # IM UPDATING ONLY FIRSTNAME,LASTNAME AND EMAIL FEILDS BELOW
        # Last Name
        wait.until(lambda d: d.find_element(*ContactPageLocators.LAST_NAME).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.LAST_NAME).clear()
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys("Kumarzz")

        # Birthdate
        wait.until(lambda d: d.find_element(*ContactPageLocators.BIRTHDATE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.BIRTHDATE).clear()
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)

        # Email
        wait.until(lambda d: d.find_element(*ContactPageLocators.EMAIL).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.EMAIL).clear()
        driver.find_element(*ContactPageLocators.EMAIL).send_keys("EnayTest@fake.com")

        # Phone
        wait.until(lambda d: d.find_element(*ContactPageLocators.PHONE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.PHONE).clear()
        driver.find_element(*ContactPageLocators.PHONE).send_keys(*PositiveData.gen_phone)

        # Street1
        wait.until(lambda d: d.find_element(*ContactPageLocators.STREET1).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STREET1).clear()
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)

        # Street2
        wait.until(lambda d: d.find_element(*ContactPageLocators.STREET2).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STREET2).clear()
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)

        # City
        wait.until(lambda d: d.find_element(*ContactPageLocators.CITY).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.CITY).clear()
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)

        # StateProvince
        wait.until(lambda d: d.find_element(*ContactPageLocators.STATE_PROVINCE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).clear()
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)

        # PostalCode
        wait.until(lambda d: d.find_element(*ContactPageLocators.POSTAL_CODE).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.POSTAL_CODE).clear()
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)

        # Country
        wait.until(lambda d: d.find_element(*ContactPageLocators.COUNTRY).get_attribute("value") != "")
        driver.find_element(*ContactPageLocators.COUNTRY).clear()
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)

        # Submit the updated form
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()


        print('now checking Kumarzz')
        time.sleep(5)
        assert 'Kumarzz' in driver.page_source

        # Return to contact list and validate
        driver.find_element(*ContactPageLocators.RETURN_BUTTON).click()
        print('returned')

        wait.until(EC.presence_of_element_located((By.XPATH, "(//td[contains(text(),'enaytest@fake.com')])")))
        email_displayed = driver.find_element(By.XPATH, "(//td[contains(text(),'enaytest@fake.com')])").text

        # validate record is updated and present in contacts list
        assert email_displayed == "enaytest@fake.com"
        print('updated contact is displayed in the list ')
        time.sleep(2)



class TestNegativeFlow:
    @pytest.mark.usefixtures("setup_teardown")

    def test_missing_required_fields(self,setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance

        # we are at dashboard now
        # Click to add new contact
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()

        # clicking submit with all fields empty
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()


        wait = WebDriverWait(driver, 10)

        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error_message = driver.find_element(By.ID, "error").text.strip()
        print("Captured error:", error_message)
        # validating error message
        assert error_message == "Contact validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required."
        print(error_message)



    def test_invalid_email_format(self,setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance
        # we are at dashboard now
        # Click to add new contact
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        # Filling out form with invalid email
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        # invalid email
        driver.find_element(*ContactPageLocators.EMAIL).send_keys('chenchuenay.com')
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
        error_Email = driver.find_element(By.ID, "error").text.strip()
        print("Captured error:", error_Email)
        # validating error message
        assert error_Email == "Contact validation failed: email: Email is invalid"
        print(error_Email)


    def test_invalid_phone_number(self,setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance
        # we are at dashboard now
        # Click to add new contact
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        # Filling out form with invalid phone number
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        # invalid email
        driver.find_element(*ContactPageLocators.EMAIL).send_keys(*PositiveData.email)

        driver.find_element(*ContactPageLocators.PHONE).send_keys('99999')# input invalid phone number
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys(*PositiveData.postalCode)
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)

        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error_Invalid_number = driver.find_element(By.ID, "error").text.strip()
        print("Captured error:", error_Invalid_number)
        # validating error message
        assert error_Invalid_number == "Contact validation failed: phone: Phone number is invalid"
        print(error_Invalid_number)



    def test_invalid_postal_code(self,setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance
        #     # we are at dashboard now
        #     # Click to add new contact
        driver.find_element(*DashboardPageLocators.ADD_CONTACT).click()
        # Filling out form with invalid postal code
        driver.find_element(*ContactPageLocators.FIRST_NAME).send_keys(*PositiveData.firstName)
        driver.find_element(*ContactPageLocators.LAST_NAME).send_keys(*PositiveData.lastName)
        driver.find_element(*ContactPageLocators.BIRTHDATE).send_keys(*PositiveData.birthdate)
        # invalid email
        driver.find_element(*ContactPageLocators.EMAIL).send_keys(*PositiveData.email)

        driver.find_element(*ContactPageLocators.PHONE).send_keys(PositiveData.gen_phone)
        driver.find_element(*ContactPageLocators.STREET1).send_keys(*PositiveData.street1)
        driver.find_element(*ContactPageLocators.STREET2).send_keys(*PositiveData.street2)
        driver.find_element(*ContactPageLocators.CITY).send_keys(*PositiveData.city)
        driver.find_element(*ContactPageLocators.STATE_PROVINCE).send_keys(*PositiveData.stateProvince)
        driver.find_element(*ContactPageLocators.POSTAL_CODE).send_keys('7') # input invalid postal code
        driver.find_element(*ContactPageLocators.COUNTRY).send_keys(*PositiveData.country)
        driver.find_element(*ContactPageLocators.SUBMIT_CONTACT).click()

        wait = WebDriverWait(driver, 10)

        wait.until(lambda d: d.find_element(By.ID, "error").text.strip() != "")
        error_Invalid_postal = driver.find_element(By.ID, "error").text.strip()
        print("Captured error:", error_Invalid_postal)
        # validating error message
        assert error_Invalid_postal == "Contact validation failed: postalCode: Postal code is invalid"
        print(error_Invalid_postal)




"""To clear Records/Contacts only"""

class TestDeleteRecords:
    @pytest.mark.usefixtures("setup_teardown")
    def test_delete_all_contacts(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 10)

        while True:
            try:
                # Find rows (excluding the header row)
                rows = driver.find_elements(By.XPATH, "//table//tr[position()>1]")

                # If no visible contacts left
                if len(rows) == 0:
                    print("✅ All records cleared.")
                    break

                # Click on the second column cell of the first contact
                rows[0].find_element(By.XPATH, "./td[2]").click()

                # Wait for delete button and click
                wait.until(EC.presence_of_element_located(ContactPageLocators.DELETE_BUTTON))
                driver.find_element(*ContactPageLocators.DELETE_BUTTON).click()

                # Accept alert
                driver.switch_to.alert.accept()

                # 💡 Wait for table to reload after deletion
                wait.until(EC.staleness_of(rows[0]))

            except Exception as e:
                print(f"❌ Error occurred: {e}")
                
                break




class TestDeleteRecords:
    @pytest.mark.usefixtures("setup_teardown")
    def test_delete_all_contacts(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 10)

        while True:
            try:
                # ✅ Get all rows excluding the header row, and skip any rows without data
                rows = driver.find_elements(By.XPATH, "//table/tbody/tr[td[2] and normalize-space(td[2]) != '']")

                if not rows:
                    print("✅ All records cleared.")
                    break

                # ✅ Click the first *valid* data row
                rows[0].find_element(By.XPATH, "./td[2]").click()

                # Wait and delete
                wait.until(EC.element_to_be_clickable(ContactPageLocators.DELETE_BUTTON))
                driver.find_element(*ContactPageLocators.DELETE_BUTTON).click()
                driver.switch_to.alert.accept()

                time.sleep(1)  # Allow time for DOM update

            except Exception as e:
                print("❌ Something went wrong or no more records.")
                print("Error:", str(e))
                break


