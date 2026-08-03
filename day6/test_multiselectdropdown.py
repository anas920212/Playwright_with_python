import pytest
from playwright.sync_api import Page, expect

def test_multi_select_dropdown(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #selecting multiple options from the dropdown - 3 ways 
    # 1) by using label 
    #page.locator("#colors").select_option(["Red", "Blue", "Green"]) #keeping them in the list box #for using label (css)
    #page.locator("#colors").select_option(label=["Red", "Blue", "Green"])

    # 2) by using value 
    # page.locator("#colors").select_option(value=["red", "blue", "green"])
    # page.wait_for_timeout(5000)
    
    # 3) by using index
    # page.locator("#colors").select_option(index=[2,4])
    # page.wait_for_timeout(5000)

    #checking the number of options in the dropdown
    dropdown_options=page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    