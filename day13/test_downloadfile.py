import pytest
import os
from playwright.sync_api import sync_playwright, expect, Page

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    # # Approach 1
    # #Register an event 
    def handle_download(download):
        download.save_as("/Users/anasmahdi/Desktop/PLaywright_with_Python/downloads/testfile1.txt")

    page.on("download", handle_download)

    # # Approach 2
    # page.on("download", lambda download: download.save_as("/Users/anasmahdi/Desktop/PLaywright_with_Python/downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(5000)

    #validation
    if os.path.exists("/Users/anasmahdi/Desktop/PLaywright_with_Python/downloads/testfile.txt"):
        print("File exists! ")
    else:
        print("File does not exist! ")


