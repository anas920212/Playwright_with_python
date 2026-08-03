# tag id (tag#id)
# tag class (tag.class)
# tag attribute (tag[attribute])
# tag class attribute ()

import pytest
from playwright.sync_api import Page, expect

def test_verify_css_locators(page : Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    #tag and id 
    # page.locator("input#small-searchterms").fill("T-Shirts")  #tag is optional here, you can only use #small-searchterms
    # #page.locator("#small-searchterms").fill("T-shirts")  #its another way to use tag and id 
    # page.wait_for_timeout(5000)

    #tag and class
    #page.locator("input.search-box-text").fill("T-Shirts")  #you can ignore the second word of the class value 
    #page.locator(".search-box-text").fill("T-Shirts")

    #tag and attribute 
    #page.locator("input[name=q]").fill("T-Shirts")
    # page.locator("[name=q]").fill("T-Shirts")
    # page.wait_for_timeout(5000)
    

    #tag class and attribute 
    #page.locator("input.search-box-text[name=q]").fill("T-Shirts")
    #page.locator(".search-box-text[name=q]").fill("T-Shirts")
    page.locator("input.search-box-text[value='Search store']").fill("T-Shirts")   #using another attribute 




    page.wait_for_timeout(5000)