import pytest
from playwright.sync_api import Page, expect

def test_static_web_table(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # 1) counting total number of rows in a table 
    rows=table.locator("tr")  #shortcut which is equal to table[name='BookTable'] tbody
    expect(rows).to_have_count(7)

    row_count=rows.count()
    print("The number of rows in a table: ",row_count)

    # 2) counting the total number of columns or headers in a table 
    columns = table.locator("th")
    expect(columns).to_have_count(4)

    column_count=columns.count()
    print("The number of columns/headers in a table: ",column_count)

    # 3) Reading all the data from second row of the table 
    second_row_data=rows.nth(2).locator("td")  #nth() index starts from 0
    second_row_texts=second_row_data.all_inner_texts()
    print("second row data is :", second_row_texts)

    expect(second_row_data).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])  #specific row and data validation

    #printing all the rows data in each line
    print("Printing second row data:.....")
    for text in second_row_texts:
        print(text)

    # 4) Reading all the data from the table (excluding header)
    all_row_data=rows.all()  #converting all the locatiors into list formats 

    print("Printing data from all the rows and columns: ")
    for row in all_row_data[1:]:
        cols=row.locator("td").all_inner_texts()
        print(cols)


    # 5) Printing the book names whether the author is Mukesh
    print("Printing books name written by Mukesh: ")
    for row in all_row_data[1:]:
            author_name=row.locator("td").nth(1).inner_text()
            if author_name == "Mukesh":
                 book_name=row.locator("td").nth(0).inner_text()
                 print(f"{author_name} wrote {book_name}")

    # 6) calculating total price of all the books 
    total_price=0
    for row in all_row_data[1:]:
        price=row.locator('td').nth(3).inner_text()
        total_price+=int(price)  #typecasting the variable price #totalprice=total_price+int(price)
    print("Total price of all the books are: ",total_price)