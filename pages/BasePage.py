from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        # Open browser with url
        return self.driver.get(url)

    def find_element(self, locator, time=30):
        # Finds one element by locator
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element with locator {locator}.")

    def find_elements(self, locator, time=30):
        # Finds multiple elements by locator
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements with locator {locator}.")

    def find_clickable_element(self, locator, time=30):
        # Finds clickable element by locator
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find and click to element with locator {locator}.")

    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()
        return button
