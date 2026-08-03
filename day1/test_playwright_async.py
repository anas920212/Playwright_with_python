#prerequisite for asynchronous execution 
#install pytest-asyncio
#command: pip install pytest-asyncio

from playwright.async_api import Page,expect,async_playwright
import pytest 

@pytest.mark.asyncio
async def test_verifyPageUrl(): 
    async with async_playwright() as p:    #p is an alias of this function
        browser = await p.chromium.launch()
        mypage=await browser.new_page()
        await mypage.goto("https://automationexercise.com/")
        await expect(mypage).to_have_url("https://automationexercise.com/") 