import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Remote
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.BasePage import BasePage
from pages.admin_panel.AdminBasePage import AdminBasePage

from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default='http://192.168.1.70:8081/')
    parser.addoption('--remote', action='store_true')
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def url(request):
    url: str = request.config.getoption('url')
    return url


@pytest.fixture(scope='session')
def browser(request):
    browser_name: str = request.config.getoption('browser')
    remote: bool = request.config.getoption('remote')

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    if request.config.getoption('headless'):
        chrome_options.add_argument('headless')
    if remote:
        driver = Remote(
            command_executor='',
            desired_capabilities={"browserName": "chrome", "javascriptEnabled": True},
            options=chrome_options
        )
    else:
        if browser_name == 'chrome':
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



