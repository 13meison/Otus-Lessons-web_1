from selenium.webdriver.common.by import By


class MainPL:
    BUTTON_CART = (By.ID, 'cart')


class CatalogPL:
    CATALOG_URL = 'laptop-notebook'
    CART_ITEMS = (By.CSS_SELECTOR, '.product-thumb')
    CARD_ITEM_ELEMENT_PRICE = (By.CSS_SELECTOR, '.caption .price')


class CardItemPL:
    FIELD_PRICE = (By.CSS_SELECTOR, '#content ul.list-unstyled>li>h2')


class LoginPL:
    LOGIN_URL = 'index.php?route=account/login'
    WINDOWS_LOGIN = (By.CSS_SELECTOR, '.form-group')


class RegistrationPL:
    REGISTRATION_URL = 'index.php?route=account/register'
    PRIVACY_POLICY = (By.CSS_SELECTOR, 'form .pull-right')



