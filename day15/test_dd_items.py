import pytest
from playwright.sync_api import  expect, Playwright, Page

search_items = ['laptop', 'Gift card', 'smartphone', 'monitor']  #simple test data for search items

@pytest.mark.parametrize("item", search_items)  #parameterization of test data  #decorator to pass the test data to the test function
def test_search_items(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)  #we need to pass item name 
    page.locator("input[value='Search']").click()

    #Assertion 
    first_result=page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item, ignore_case=True) #to avoid case sensitivity we can use to_contain_text instead of to_have_text aldp ignore_case=True




