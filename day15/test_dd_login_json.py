import time
import pytest
import json
from playwright.sync_api import expect, Page

#Read the json file 
file=open("../testdata/data.json", "r")
login_data=json.load(file)

@pytest.mark.parametrize("email, password, validity", [ 
                         (data["email"], data["password"], data["validity"]) for data in login_data])  

def test_login_data_driven_json(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #Filling the login form 
    page.locator("#Email").fill(email) 
    page.locator("#Password").fill(password)  
    page.locator("input[value='Log in']").click()

    #validation 
    if validity == "valid":
        logout_link=page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)  

    else:
        error_message=page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)  #assertion for unsuccessful login
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")  #assertion for unsuccessful login

    