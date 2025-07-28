from selenium.webdriver.common.by import By


class DashboardPageLocators:
    ADD_CONTACT = By.ID, "add-contact"

    def select_contact_by_phone(phone):
        return (By.XPATH, f'(//td[normalize-space()={phone}])')

    def validate_email(email):
        return (By.XPATH, f"(//td[contains(text(),'{email.lower()}')])")



