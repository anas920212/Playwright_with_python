import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #counting and showing the number of frames inside the page (showing in a list)
    frames=page.frames
    print("Number of frames on a page: ", len(frames))  #total 7 pages are there 

    #frame 1
    #frame1=page.frame("name attribute of the frame") #currently we dont have it on the webpage element #way3 using name
    #frame1 = page.frame_locator("frame[src='frame_1.html']")  #getting the frame #way1 using css 
    frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1") #getting thr frame #way2 using url
    inputbox=frame1.locator("input[name='mytext1']")
    inputbox.fill("Welcome")  #passing value into frame1

    expect(inputbox).to_have_value("Welcome")  #validation

    page.wait_for_timeout(5000)