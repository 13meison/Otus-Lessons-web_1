import time

from Locators import MainPL, CatalogPL, CardItemPL, RegistrationPL, LoginPL
from pages.BasePage import BasePage


# def test_find_button_card(browser, url):
#     bp = BasePage(browser)
#     bp.open_url(url)

def test_find_button_card(base_page, url):
    base_page.open_url(url)
    base_page.find_element(MainPL.BUTTON_CART)


def test_catalog_find_items(base_page, url):
    base_page.open_url(url + CatalogPL.CATALOG_URL)
    elements = base_page.find_elements(CatalogPL.CART_ITEMS)
    assert len(elements) == 5
    element = elements[3]
    #element.find_element(CatalogPL.CARD_ITEM_ELEMENT_PRICE).text == '$1202.00'



def test_check_price_laptop(base_page, url):
    base_page.open_url(url + CatalogPL.CATALOG_URL)
    base_page.click_button(CatalogPL.CART_ITEMS)
    assert base_page.find_element(CardItemPL.FIELD_PRICE).text == '$122.00'


def test_field_registration(base_page, url):
    base_page.open_url(url + RegistrationPL.REGISTRATION_URL)
    base_page.find_element(RegistrationPL.PRIVACY_POLICY)


def test_login_page(base_page, url):
    base_page.open_url(url + LoginPL.LOGIN_URL)
    base_page.find_element(LoginPL.WINDOWS_LOGIN)
