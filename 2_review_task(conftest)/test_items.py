import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_button_title(browser):
    browser.get(link)
    time.sleep(3)
    add_button_text = browser.find_element_by_css_selector("#add_to_basket_form button").text
    assert add_button_text !=0,  "There is no text in the button for adding to the basket"