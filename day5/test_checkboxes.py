import pytest
from playwright.sync_api import Page, expect

def test_checkbox(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # # 1) selecting specific checkbox (Sunday checkbox)
    # sunday_checkbox=page.get_by_label("Sunday") 
    # sunday_checkbox.check()
    # expect(sunday_checkbox).to_be_checked()
    # page.wait_for_timeout(5000)

    # 2) Counting total number of checkboxes in a webpage 

    #step-1 creating a list collecting /list array 
    days = ['Sunday','Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday']
    checkboxes = []

    #step - 2 
    # for day in days:
    #     checkbox=page.get_by_label(day)
    #     checkboxes.append(checkbox)

    checkboxes=[page.get_by_label(day) for day in days]  #days is a list collection here 
    print("Total number of checkboxes:", len(checkboxes))

    # # # 3) Selecting all the chckboxes and asserting each check box is selected
    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()

    #     page.wait_for_timeout(5000)

    # # 4) unselecting or uncheckinng last three checkboxes 
    # for checkbox in checkboxes[-3:]:  #using slicing operator
    #     checkbox.uncheck()
    #     expect(checkbox).not_to_be_checked()
        
    # page.wait_for_timeout(5000)

    # # 5) Toggle checkboxes 
    # for checkbox in checkboxes:
    #     if checkbox.is_checked():
    #         checkbox.uncheck()
    #         expect(checkbox).not_to_be_checked()
    #     else:
    #         checkbox.check()
    #         expect(checkbox).to_be_checked()

    # page.wait_for_timeout(5000)

    # # 6) Randomly checking the checkboxes - checking 1,3,6 checkboxes
    # indexes = [1,3,6]
    # for i in indexes:
    #     checkboxes[i].check()
    #     expect(checkboxes[i]).to_be_checked()

    # page.wait_for_timeout(5000)

    # 7) selecting checkbox based on the table/input value 
    weekday="Friday"

    for label in days:
        if label == weekday:
            checkbox=page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

