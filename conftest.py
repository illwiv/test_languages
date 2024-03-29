import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: es, ru or other language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()