import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.BasePage import BasePage

from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default='http://192.168.100.10:8081/')


@pytest.fixture(scope='session')
def url(request):
    url: str = request.config.getoption('url')
    return url


@pytest.fixture(scope='session')
def browser(request):
    browser_name: str = request.config.getoption('browser')

    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif browser_name == 'firefox':
        # driver = webdriver.Firefox(
        #     executable_path='C:\\Users\\13mei\\.wdm\\drivers\\geckodriver\\win64\\0.32\\geckodriver.exe')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError('"--browser" should be "chrome" or "firefox"')

    def final():
        driver.quit()

    request.addfinalizer(final)
    # yield browser
    # browser.quit()
    return driver


@pytest.fixture()
def base_page(browser):
    pb = BasePage(browser)
    return pb
