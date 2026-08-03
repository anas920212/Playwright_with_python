import pytest
from playwright.sync_api import Page, expect

def test_bootstrapdropdown(page : Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #login steps
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()

    page.wait_for_timeout(3000)

    #click on PIM
    page.get_by_text("PIM").click()

    #click on the job title dropdown
    page.locator("form i").nth(3).click()  #nth method pf playwright, which will open options from the dropdown
    page.wait_for_timeout(3000)

    #capture all the options from dropdown
    options=page.locator("div[role='listbox'] span")
    count=options.count()
    print("Number of options in the dropdown:", count)
    expect(options).to_have_count(count)  #assertion for counting the options 

    page.wait_for_timeout(5000)

    #print all the options from the dropdown
    print("All the options from the dropdown:", options.all_text_contents())

    #print all the options test using loop
    # for i in range(count):
    #     print(options.nth(i).text_content())

    #select/click on specific option
    for i in range(count):
        text=options.nth(i).inner_text()
        print("Option to be selected:", text)
        if text == 'Marketing':
            print("Matching successful")
            options.nth(i).click()
            break

    page.wait_for_timeout(5000)
