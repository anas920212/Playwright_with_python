import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_options=page.locator("#colors>option")  #unsorted list
    #dropdown_options=page.locator("#animals>option") #sorted list

    options_text=[text.strip() for text in dropdown_options.all_text_contents()] #capturing all the options in a variable

    original_list=options_text.copy()  
    sorted_list =sorted(options_text)  #sorting method

    print("Original list:", original_list)
    print("Sorted list:", sorted_list)

    if original_list==sorted_list:
        print("dropdown options are sorted order....")
        #assert True
    else:
        print("dropdown options are not sorted order....")
        #assert False

    page.wait_for_timeout(5000)
    