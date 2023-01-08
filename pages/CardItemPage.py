from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CardItemPage(BasePage):
    FIELD_PRICE = (By.CSS_SELECTOR, '#content ul.list-unstyled>li>h2')