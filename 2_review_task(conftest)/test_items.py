import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_checker(browser):
    browser.get(link)
    time.sleep(3)
    add_button_text = browser.find_element_by_css_selector("#add_to_basket_form").text
    assert add_button_text,  "There is no button 'Add to basket'"