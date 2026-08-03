import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    # 1) by using label  (mostly preferred)
    #page.locator("#country").select_option("Bangladesh") 
    #page.locator("#country").select_option(label="Australia")  #by label
    #page.wait_for_timeout(5000)

    # 2) by using value 
    #page.locator("#country").select_option("germany")
    #page.locator("#country").select_option(value="germany")
    #page.wait_for_timeout(5000)

    # 3) by using index 
    # page.locator("#country").select_option(index=4)  #index starts form 0
    # page.wait_for_timeout(5000)

    #checking the number of options in the dropdown 
    dropdown_options=page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)
    
    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    #print countries using loop 
    for option in options_text:
        print(option)

    page.wait_for_timeout(5000)
    