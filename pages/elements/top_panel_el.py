from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class TopPanelEl(BasePage):
    BUTTON_CART = (By.ID, 'cart')
