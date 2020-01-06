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
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome("D:\\Apps\\Drivers\\chromedriver.exe", options=options)
    elif browser_name == "opera":
        print("\nstart opera browser for test..")
        webdriver_service = service.Service('D:\\Apps\\Drivers\\operadriver.exe')
        webdriver_service.start()
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=' + language)
        browser = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or opera, "
                                "language should be in short form (en, uk, ru)")
    yield browser
    print("\nquit browser..")
    browser.quit()
    #fffff