
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random




import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class TestPositiveFlow:
    @pytest.mark.usefixtures("setup_teardown")
    def testPositiveFlowE2E(self, setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance

        # we are at dashboard now
        # Click to add new contact
        driver.find_element(By.ID, "add-contact").click()
        # Fill out the create form
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Chenchu")
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Enay")
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').send_keys("1997-04-19")
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("chenchuTest@fake.com")
        phone = str(random.randint(9000000000, 9999999999))  # Generate a random phone number
        driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)
        driver.find_element(By.XPATH, '//*[@id="street1"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="street2"]').send_keys("United Arab Emirates")
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').send_keys("00000")
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United Arab Emirates")
        driver.find_element(By.ID, "submit").click()

        # Wait and validate contact creation
        time.sleep(5)
        assert phone in driver.page_source
        print('phone checked here')
        print(phone)

        # Click on the created contact and go to edit page
        driver.find_element(By.XPATH, f'(//td[normalize-space()={phone}])').click()
        driver.find_element(By.XPATH, "//button[@id='edit-contact']").click()

        wait = WebDriverWait(driver, 10)

        # Clear and update each field with explicit wait for non-empty value

        # First Name
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="firstName"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="firstName"]').clear()
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Enay")

        # Last Name
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="lastName"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="lastName"]').clear()
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Kumarzz")

        # Birthdate
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="birthdate"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').send_keys("1997-04-19")

        # Email
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="email"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="email"]').clear()
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("EnayTest@fake.com")

        # Phone
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="phone"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="phone"]').clear()
        driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)

        # Street1
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="street1"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="street1"]').clear()
        driver.find_element(By.XPATH, '//*[@id="street1"]').send_keys("Abu Dhabi")

        # Street2
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="street2"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="street2"]').clear()
        driver.find_element(By.XPATH, '//*[@id="street2"]').send_keys("United Arab Emirates")

        # City
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="city"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="city"]').clear()
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Abu Dhabi")

        # StateProvince
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="stateProvince"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').clear()
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').send_keys("Abu Dhabi")

        # PostalCode
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="postalCode"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').clear()
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').send_keys("00000")

        # Country
        wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="country"]').get_attribute("value") != "")
        driver.find_element(By.XPATH, '//*[@id="country"]').clear()
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United Arab Emirates")

        # Submit the updated form
        driver.find_element(By.ID, "submit").click()


        print('now checking Kumarzz')
        time.sleep(5)
        assert 'Kumarzz' in driver.page_source

        # Return to contact list and validate
        driver.find_element(By.XPATH, "//button[@id='return']").click()
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
        driver.find_element(By.ID, "add-contact").click()

        # clicking submit with all fields empty
        driver.find_element(By.ID, "submit").click()


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
        driver.find_element(By.ID, "add-contact").click()
        # Fill out the create form
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Chenchu")
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Enay")
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').send_keys("1997-04-19")

        # invalid email
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("chenchuTestfake.com")

        phone = str(random.randint(9000000000, 9999999999))  # Generate a random phone number
        driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)
        driver.find_element(By.XPATH, '//*[@id="street1"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="street2"]').send_keys("United Arab Emirates")
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').send_keys("00000")
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United Arab Emirates")
        driver.find_element(By.ID, "submit").click()

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
        driver.find_element(By.ID, "add-contact").click()
        # Fill out the create form
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Chenchu")
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Enay")
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').send_keys("1997-04-19")
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("chenchuTest@fake.com")

        phone = '99999'  #invalid phone number
        driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)
        driver.find_element(By.XPATH, '//*[@id="street1"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="street2"]').send_keys("United Arab Emirates")
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').send_keys("00000")
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United Arab Emirates")
        driver.find_element(By.ID, "submit").click()

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
        driver.find_element(By.ID, "add-contact").click()
        #     # Fill out the create form
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Chenchu")
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Enay")
        driver.find_element(By.XPATH, '//*[@id="birthdate"]').send_keys("1997-04-19")
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("chenchuTest@fake.com")

        phone = str(random.randint(9000000000, 9999999999))  # Generate a random phone number
        driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)
        driver.find_element(By.XPATH, '//*[@id="street1"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="street2"]').send_keys("United Arab Emirates")
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Abu Dhabi")
        driver.find_element(By.XPATH, '//*[@id="stateProvince"]').send_keys("Abu Dhabi")

        # invalid postal code
        driver.find_element(By.XPATH, '//*[@id="postalCode"]').send_keys("00")
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United Arab Emirates")
        driver.find_element(By.ID, "submit").click()


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
                # Check if any row exists with delete option
                rows = driver.find_elements(By.XPATH, "//table//tr[position()>1]")  # Exclude table header
                if not rows:
                    print("✅ All records cleared.")
                    break

                # Click the first row’s cell to select
                driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]").click()
                wait.until(EC.presence_of_element_located((By.ID, 'delete')))
                driver.find_element(By.ID, 'delete').click()
                driver.switch_to.alert.accept()

            except Exception as e:
                print("Something went wrong or no more records.")
                break


