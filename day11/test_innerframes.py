import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_inner_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #frame-3
    #frame3=page.frame_locator("frame[src='frame_3.html']")
    frame3=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")  #grabbing the frame3 with url

    frame3.locator("input[name='mytext3']").fill("Welcome") #getting the inputbox from frame3 and providing the text

    child_frames=frame3.child_frames
    print("Number of child frames inside the frame3:", len(child_frames))

    innerframe=child_frames[0]

    radio_button=innerframe.get_by_label("I am a human")
    radio_button.check()
    expect(radio_button).to_be_checked()  #validation 


    page.wait_for_timeout(5000)
