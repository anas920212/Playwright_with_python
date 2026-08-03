import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.skip
def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading single file 
    page.locator("#singleFileInput").set_input_files("/Users/anasmahdi/Desktop/PLaywright_with_Python/uploads/Test1.txt")
    page.locator("button:has-text('Upload Single File')").click()

    #validation
    msg=page.locator("#singleFileStatus")
    expect(msg).to_contain_text("Test1.txt")

    print("File upload successful....!")

    page.wait_for_timeout(5000)

def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading mutliple files
    files=["/Users/anasmahdi/Desktop/PLaywright_with_Python/uploads/Test1.txt","/Users/anasmahdi/Desktop/PLaywright_with_Python/uploads/Test2.pdf"]

    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    #validation
    msgloc=page.locator("#multipleFilesStatus")

    expect(msgloc).to_contain_text("Test1.txt")
    expect(msgloc).to_contain_text("Test2.pdf")

    print("Multiple files are uploaded successfully...!")

    page.wait_for_timeout(5000)

    