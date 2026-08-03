from playwright.sync_api import Page,expect

#creating function test_verifyPageUrl
def test_verifyPageUrl(page:Page):   #page fixture form : Page class 
    page.goto("https://automationexercise.com/") #passing url

    myurl = page.url
    print("Url of the application:",myurl)

    expect(page).to_have_url("https://automationexercise.com/")  #validation

#verifying the title of the webpage
def test_verifyTitle(page:Page):
     page.goto("https://automationexercise.com/")

     mytitle=page.title() 
     print("Page title is: ", mytitle)

     expect(page).to_have_title("Automation Exercise")