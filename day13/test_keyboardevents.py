import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_keyboardactions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#input1")

    # 1) focus on input1
    input1.focus()

    # 2) provide the text in input1
    page.keyboard.insert_text("Welcome")

    # 3) ctrl+A
    page.keyboard.press("Meta+A")

    # 4) ctrl+C
    page.keyboard.press("Meta+C")

    # 5) pressing Tab button two times 
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 6) ctrl+V - Paste the text inside the second input box
    page.keyboard.press("Meta+V")

    # 7) pressing Tab button two times 
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 8) ctrl+V - Paste the text inside the third input box
    page.keyboard.press("Meta+V")

    input2=page.locator("#input2")
    input3=page.locator("#input3")

    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")

    page.wait_for_timeout(5000)
