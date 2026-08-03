import pytest
from playwright.sync_api import Page, expect

def test_inputbox(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    text_box=page.locator("#name")

    #visibility and enability
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #checking the attribute of the elements
    expect(text_box).to_have_attribute("maxlength", "15")

    #get an attribute of the element
    maxlength=text_box.get_attribute("maxlength")
    print("Maximum length of input box: ", maxlength)

    #fill the text inside the input box
    text_box.fill("John Kenedy")

    #get the input value from the input box
    entered_value=text_box.input_value()
    print("Value entered is: ", entered_value)

    page.wait_for_timeout(5000)