import pytest
from playwright.sync_api import Page, expect

def test_radio_buttons(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    male_radio=page.locator("#male")

    #visibility and enability
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    #negative testing of checking whether the readio button is not checked
    expect(male_radio).not_to_be_checked()

    #select or check radio button - action
    male_radio.check()

    #after checking to check whether the radio button is checked - validation 
    expect(male_radio).to_be_checked()

    page.wait_for_timeout(5000)
