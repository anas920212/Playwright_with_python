from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_page_object_model(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

    #visiting the website 
    login_page.navigate()

    #calling the login method from the LoginPage class
    login_page.login("standard_user", "secret_sauce")

    #assertion to verify successful login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    

