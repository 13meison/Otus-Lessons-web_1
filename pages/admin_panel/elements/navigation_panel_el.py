from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class AdminNavPanelEl(BasePage):
    CATALOG_LI = (By.CSS_SELECTOR, '#menu-catalog')
    CATALOG_LI_PRODUCTS = (By.LINK_TEXT, 'Products')

    def go_to_nav_element(self, name, sub_name):
        self.find_element((By.CSS_SELECTOR, name)).click()
        self.find_element((By.LINK_TEXT, sub_name)).click()
        return self

