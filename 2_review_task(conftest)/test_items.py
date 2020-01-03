import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    add_button_text = browser.find_element_by_css_selector("#add_to_basket_form").text
    assert add_button_text,  "There is no button 'Add to basket'"