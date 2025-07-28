from selenium.webdriver.common.by import By


class ContactPageLocators:
    ADD_CONTACT_BUTTON = (By.ID, "add-contact")
    EDIT_CONTACT_BUTTON = (By.ID, "edit-contact")
    DELETE_BUTTON = (By.XPATH, "//button[@id='delete']")
    RETURN_BUTTON = (By.ID, "return")
    ERROR_MESSAGE = (By.ID, "error")

    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastName"]')
    BIRTHDATE = (By.XPATH, '//*[@id="birthdate"]')
    EMAIL = (By.XPATH, '//*[@id="email"]')
    PHONE = (By.XPATH, '//*[@id="phone"]')
    STREET1 = (By.XPATH, '//*[@id="street1"]')
    STREET2 = (By.XPATH, '//*[@id="street2"]')
    CITY = (By.XPATH, '//*[@id="city"]')
    STATE_PROVINCE = (By.XPATH, '//*[@id="stateProvince"]')
    POSTAL_CODE = (By.XPATH, '//*[@id="postalCode"]')
    COUNTRY = (By.XPATH, '//*[@id="country"]')
    SUBMIT_CONTACT = (By.ID, "submit")

