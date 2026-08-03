import pytest
from playwright.sync_api import expect, Page
import openpyxl

login_data= []

workbook=openpyxl.load_workbook("../testdata/data.xlsx")  #load the excel file
sheet=workbook.active

#reading data from excel sheet using for loop
for row in sheet.iter_rows(min_row=2, values_only=True):  #skip the header row  
    email, password, validity = row  #unpack the values from each row
    login_data.append((str(email or ""), str(password or ""), str(validity or "")))  #append the data to the empty list
workbook.close()  #close the excel file

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

    