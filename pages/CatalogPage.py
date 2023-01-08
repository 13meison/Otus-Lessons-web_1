from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_URL = 'laptop-notebook'
    CART_ITEMS = (By.CSS_SELECTOR, '.product-thumb .image')
    CARD_ITEM_ELEMENT_PRICE = (By.CSS_SELECTOR, '.caption .price')