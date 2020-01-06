import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Add user language: es, fr, ukr, ru, etc.")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose web browser: chrome or opera")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    browser = None

    yield browser
    print("\nquit browser..")
    browser.quit()