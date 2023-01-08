from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, driver):
        self.browser = driver

    def open_url(self, url, path=''):
        # Open browser with url
        self.browser.get(url + path)
        return self

    def find_element(self, locator, time=10):
        # Finds one element by locator
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                           message=f"Can't find element with locator {locator}.")
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(locator))

    def find_elements(self, locator, time=10):
        # Finds multiple elements by locator
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator),
                                                           message=f"Can't find elements with locator {locator}.")
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(locator))

    def find_clickable_element(self, locator, time=10):
        # Finds clickable element by locator
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                       message=f"Can't find and click to element with locator{locator}")

    def element_presence(self, locator, time=10):
        try:
            WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()
        return self

    def enter_to_field(self, locator, text):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(text)
        return self

    def handler_alert(self, flag=True):
        alert = Alert(self.browser)
        if flag == True:
            alert.accept()
        else:
            alert.dismiss()

    def save_screenshot(self):
        self.browser.save_screenshot('screenshot.png')
