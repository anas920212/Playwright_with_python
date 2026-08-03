import time
import pytest
import csv
from playwright.sync_api import expect, Page

login_data=[]  #empty list 

#Read the csv file 
csvfile= open("/Users/anasmahdi/Desktop/PLaywright_with_Python/testdata/data.csv", newline= '', encoding ='utf-8')
reader=csv.DictReader(csvfile)  #read the csv file and store the data in a dictionary
for row in reader:
    login_data.append((row["email"],row["password"],row["validity"]))  #append the data to the empty list

@pytest.mark.parametrize("email, password, validity", login_data)
def test_login_data_driven_csv(email, password, validity, page: Page):
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

    