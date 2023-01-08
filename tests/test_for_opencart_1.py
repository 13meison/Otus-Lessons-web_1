from pages.LoginPage import LoginPage
from pages.CardItemPage import CardItemPage
from pages.elements.top_panel_el import TopPanelEl
from pages.CatalogPage import CatalogPage
from pages.BasePage import BasePage

'''tests_for_top_panel'''


# def test_find_button_card(browser, url):
#     base_page = BasePage(browser)
#     base_page.open_url(url)
#     base_page.find_element(TopPanelEl.BUTTON_CART)
def test_find_button_card(browser, url):
    base_page = BasePage(browser) \
        .open_url(url) \
        .find_element(TopPanelEl.BUTTON_CART)


def test_changed_currency(browser, url):
    pass


'''tests_for_catalog_and_items'''


def test_catalog_find_items(browser, url):
    elements = BasePage(browser) \
        .open_url(url + CatalogPage.CATALOG_URL) \
        .find_elements(CatalogPage.CART_ITEMS)
    assert len(elements) == 5
    element = elements[3]
    # element.find_element(CatalogPL.CARD_ITEM_ELEMENT_PRICE).text == '$1202.00'


def test_check_price_laptop(browser, url):
    base_page = BasePage(browser) \
        .open_url(url + CatalogPage.CATALOG_URL) \
        .click_button(CatalogPage.CART_ITEMS)
    assert base_page.find_element(CardItemPage.FIELD_PRICE).text == '$122.00'


'''tests_for_registration_and_login'''


def test_field_registration(browser, url):
    BasePage(browser) \
        .open_url(url + LoginPage.REGISTRATION_URL) \
        .find_element(LoginPage.PRIVACY_POLICY)


def test_registration_new_user(browser, url):
    pass


def test_login_page(browser, url):
    BasePage(browser) \
        .open_url(url + LoginPage.LOGIN_URL) \
        .find_element(LoginPage.WINDOWS_LOGIN)
