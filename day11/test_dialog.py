import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)

    #Approach-1 (not preffered)
    #registering an event by defining a function
    def handle_dialog(dialog):
        dialog.accept()

    #before clicking on the we have to register an event page.on()
    page.on("dialog", handle_dialog)

    page.locator("#alertBtn").click()  #clicking on the button which will open the dialog

    page.wait_for_timeout(5000)

@pytest.mark.skip
#testing simple dialog 
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)

    #Approach-2 (mostly preffered)

    #lambda function
    page.on("dialog", lambda dialog:dialog.accept())  #lambda parameters : expression 
    page.wait_for_timeout(3000)

    page.locator("#alertBtn").click()  #clicking on the button which will open the dialog

    page.wait_for_timeout(5000)

@pytest.mark.skip
#testing confirmation dialog 
def test_confirmation_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #page.on("dialog", lambda dialog:dialog.accept())  #lambda parameters : expression 
    page.on("dialog", lambda dialog:dialog.dismiss())
    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()  #clicking on the button which will open the dialog

    page.wait_for_timeout(5000)

    text=page.locator("#demo").inner_text()
    print("Output text is: ",text)

    #expect(page.locator("#demo")).to_have_text("You pressed OK!")  #this is the output for OK button
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")  #this is the output for Cancel button
    page.wait_for_timeout(5000)


#Testing prompt dialog/alert 
def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialog:dialog.accept("John"))  # passing the parameter
    page.locator("#promptBtn").click()  #clicking on the button which will open the dialog
    page.wait_for_timeout(3000)

    text=page.locator("#demo").inner_text()
    print("Output text: ", text)

    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")
    #expect(page.locator("#demo")).to_contain_text("John")

    page.wait_for_timeout(5000)

    

  

