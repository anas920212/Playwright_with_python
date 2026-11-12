from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        #locators 
        self.username_input = page.locator("//input[@id='user-name']")
        self.password_input = page.locator("//input[@id='password']")
        self.login_button = page.locator("//input[@id='login-button']") 

    def navigate(self):
            self.page.goto("https://www.saucedemo.com/")    

    def login(self, username: str, password: str):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()