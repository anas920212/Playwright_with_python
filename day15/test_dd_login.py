#Test combinations for login functionality
#valid data ---> successful login ---> Test case passed
# valid data ---> unsuccessful login ---> Test case failed
# invalid data ---> successful login ---> Test case failed
# invalid data ---> unsuccessful login ---> Test case passed

login_test_data = [("laura.taylor123@example.com", "test123", "valid"),
                    ("laura.taylor123@example.com", "test321", "invalid"),
                    ("validuser@example.com", "testxyz", "invalid"),
                    ("", "", "invalid")
                    ]

import time
import pytest
from playwright.sync_api import expect, Page

@pytest.mark.parametrize("email, password, validity", login_test_data)  #parameterization of test data  #decorator to pass the test data to the test function
def test_login_data_driven(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #Filling the login form 
    page.locator("#Email").fill(email)  #email id 
    page.locator("#Password").fill(password)  #password
    page.locator("input[value='Log in']").click()

    #validation of login functionality based on the validity of the test data
    if validity == "valid":
        logout_link=page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)  #assertion for successful login

    else:
        error_message=page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)  #assertion for unsuccessful login

        expect(page).to_have_url("https://demowebshop.tricentis.com/login")  #assertion for unsuccessful login

    