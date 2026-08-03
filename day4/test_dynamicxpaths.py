#  #dynamic xpaths 
#     page.locator("//button[@name='start' or @name='stop']")
#     page.locator("//button[contains(@name,'st')]")
#     page.wait_for_timeout(5000)

import pytest
from playwright.sync_api import Page, expect
import re

# def test_handle_dynamic_elements(page : Page):
#     #launch the url
#     page.goto("https://testautomationpractice.blogspot.com/")

#     for i in range(5):
#         button=page.locator("//button[text()='START' or text()='STOP']")
#         button.click()
#         page.wait_for_timeout(5000)

    #handle dynamic links using CSS
# def test_handle_dynamic_elements_css(page: Page):
#     page.goto("https://testautomationpractice.blogspot.com/")

#     for i in range(5):
#         button=page.locator("button[name='start'],button[name='stop']")
#         button.click()
#         page.wait_for_timeout(5000)

    # using playwright locator 

def test_handle_dynamic_elements_css(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for i in range(5):
        button=page.get_by_role(role="button", name=re.compile(r'ST.*'))
        button.click()
        page.wait_for_timeout(5000)
        


  