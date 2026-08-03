import pytest
from playwright.sync_api import Page, expect

def test_comparisonmethods(page : Page):
    page.goto("https://demowebshop.tricentis.com/")

    products=page.locator(".product-title")

    # 1) inner_text() vs text_content()
    # print("Using inner_text() =====>", products.nth(1).inner_text())  #gives the exact text 
    # print("Using text_content()====>", products.nth(1).text_content())  #returns content with special chars and spaces 

    # count=products.count()
    # for i in range(count):
    #     # product_name = products.nth(1).inner_text()
    #     # print(product_name)

    #     product_name=products.nth(1).text_content()
    #     print(product_name.strip())  #strip() methods remove all the special chars and spaces 

    # 2) all_inner_texts() vs all_text_contents()
        #product_names=products.all_text_contents() #returns the list of product names with spaces and chars
    product_names=products.all_inner_texts()
    print(product_names)



    


