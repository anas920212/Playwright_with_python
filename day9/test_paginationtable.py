import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip  #for skipping the below test function 
def test_paginaton_table(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages=True

    while has_more_pages:
        rows=page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())

        page.wait_for_timeout(3000)
        
        next_button=page.locator("button[aria-label='Next']")
        is_disabled=next_button.get_attribute("class")  #has extracted the value of clas attribute 

        if "disabled" in is_disabled:
            has_more_pages=False
        else:
            next_button.click()

#verifying the filters of the pagination table 
def test_filter_rows(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    dropdwon=page.locator("#dt-length-0")
    dropdwon.select_option(label="25")

    rows=page.locator("#example tbody tr")
    print("Number of rows Filtered: ", rows.count())
    expect(rows).to_have_count(25)
    

