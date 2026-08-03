import time
from playwright.sync_api import Page, expect

def test_orangehrm_login(page: Page):
    # loading the webpage of orangehrm
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # filling out the username filed with credentials
    page.get_by_placeholder("Username").fill("Admin")
    
    # filling out the password input field with ceedentials 
    page.get_by_placeholder("Password").fill("admin123")
    
    # clicking on login button 
    page.get_by_role("button", name="Login").click()
    
    # verification adn validation
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    page.wait_for_timeout(5000)