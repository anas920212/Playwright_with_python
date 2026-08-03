from playwright.sync_api import sync_playwright, expect, Playwright, Page
import pytest

#Direct - inject userlogin with url 

#https://the-internet.herokuapp.com/basic_auth

#https://admin:admin@the-internet.herokuapp.com/basic_auth


@pytest.mark.skip
def test_authPopup(page: Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    page.wait_for_load_state()  #wait_for_load_state()- it will wait till the entire page is loaded 
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(5000)  #wait_for_timeout() method is used to specify the fixed time 


#using context - we can pass username and password along with the context (most preffered approach)

def test_authPopup(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page=context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()  
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(5000)  
