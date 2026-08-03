import pytest
from playwright.sync_api import Page, expect

def test_xpath_locators(page : Page):
    #launch the url
    page.goto("https://demowebshop.tricentis.com/")

    # 1) Absolute XPATH
    logo=page.locator("xpath=/html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    #logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()


    # 2) Relative xpath   #syntax of Rel_Xpath = //tagname[@attrtibute='value']
    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()


    # 3) xpath with contains() 
    
    products=page.locator("//h2//a[contains(@href,'computer')]")
    products_count=products.count()
    print("Products count: ", products_count)
    expect(products).to_have_count(products_count)

    # 4) xpath starts-with()
    building_products=page.locator("//h2//a[starts-with(@href, '/build')]")
    print("Count of building products:" , building_products.count())

    # 5) xpath with text   #text is representing the inner text of the element 
    registration_link=page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()

    # 6)xpath with last  
    #google_button=page.locator("//div[@class='column follow-us']//li[5]")
    google_button=page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_button).to_have_text("Google+")

    # 7) xpath with position
    twitter_link=page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")

    # 8) dynamic xpath 
    page.locator("//button[@name='start' or @name='stop']")
    page.locator("//button[contains(@name,'st')]")
    page.wait_for_timeout(5000)

   