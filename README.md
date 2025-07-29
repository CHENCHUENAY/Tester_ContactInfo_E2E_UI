# Tester_ContactInfo_E2E_UI
PROJECT NAME: Contact List - UI Automation (Selenium + Pytest)

DESCRIPTION:
This project automates the UI functionality of the “Thinking Tester Contact List” web application. 
It uses Python, Selenium WebDriver, and Pytest framework. It follows the Page Object Model (POM) design pattern, 
and includes both positive and negative test flows, dynamic test data generation, HTML reporting, and modular file structure.

---------------------------------------------------------------
TECH STACK:
- Python 3.12
- Selenium WebDriver
- Pytest
- WebDriverManager
- Pytest HTML report plugin
- Page Object Model (POM)
- Chrome Browser

---------------------------------------------------------------
FOLDER STRUCTURE:

contact-list-ui-automation/
|
|-- pages/
|   |-- login_page.py              # Contains locators for login screen
|   |-- dashboard_page.py          # Contains locators related to dashboard after login
|   |-- contact_page.py            # All locators related to contact CRUD operations
|
|-- tests/
|   |-- test_positive_negative.py  # Contains test cases for both positive and negative flows
|
|-- utils/
|   |-- test_data.py               # Contains positive and negative test data objects
|
|-- conftest.py                    # Contains driver setup, teardown and login fixture
|-- requirements.txt              # Project dependencies
|-- README.txt                    # This file

---------------------------------------------------------------
FEATURES AUTOMATED:

1. Login Functionality
2. Add New Contact with Random Data
3. Update Contact (Clear and Re-enter)
4. Validate Updated Contact in UI
5. Delete Contact (including loop to delete all)
6. Negative Test Cases:
   - Missing required fields
   - Invalid email format
   - Invalid phone number
   - Invalid postal code
7. Assertion Validations for UI response
8. Dynamic phone number generation
9. Explicit Waits for reliability
10. HTML Report generation with pytest-html

---------------------------------------------------------------
SETUP INSTRUCTIONS:

1. Clone the repository or download the code.

2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate   (on Windows: venv\Scripts\activate)

3. Install dependencies:
   pip install -r requirements.txt

4. Run tests:
   pytest -s

5. Generate HTML report:
   pytest --html=report.html

---------------------------------------------------------------
TESTING NOTES:

- All test data is stored in test_data.py file inside the utils folder.
- The locators follow POM structure and are stored in separate files inside the pages folder.
- The login process is moved to conftest.py so all tests get pre-logged in.
- Tests are modular and can run independently.
- Explicit waits are used to avoid flaky behavior while clearing and updating form fields.

---------------------------------------------------------------
SAMPLE TEST CASES:

testPositiveFlowE2E:
- Adds a contact
- Updates the contact
- Validates presence
- Returns to contact list and asserts data

test_delete_all_contacts:
- Deletes all contacts in the table
- Handles even last row deletion edge case

test_invalid_email_format:
- Attempts to create contact with bad email
- Validates error message

test_missing_required_fields:
- Submits empty form
- Validates error for required fields

---------------------------------------------------------------
AUTHOR:
Name: Enay Kumar Reddy
Contact: chenchuenay97@gmail.com
htttps://ae.linkedin.com/in/enaykumar
