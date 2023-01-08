import pytest

from pages.admin_panel.AdminBasePage import AdminBasePage
from pages.admin_panel.elements.navigation_panel_el import AdminNavPanelEl
from pages.admin_panel.AdminCatalogPage import AdminCatalogPage
from pages.BasePage import BasePage
import time

from selenium.webdriver.common.by import By

'''tests_for_administration_panel'''


@pytest.mark.admin_products
def test_added_new_item(browser, url):
    BasePage(browser) \
        .open_url(url, AdminBasePage.PATH_LOGIN)
    AdminBasePage(browser) \
        .input_login()
    AdminNavPanelEl(browser) \
        .go_to_nav_element('#menu-catalog', 'Products')
    AdminCatalogPage(browser) \
        .click_button(AdminCatalogPage.NEW_ITEM_BTN) \
        .create_new_item_product()
    assert AdminCatalogPage(browser).check_presence_item() is True
    # .enter_to_field(AdminCatalogPage.FILTER_NAME, AdminCatalogPage.TEST_NAME) \
    # .click_button(AdminCatalogPage.FILTER_BTN)


@pytest.mark.admin_products
def test_delete_item(browser, url):
    BasePage(browser) \
        .open_url(url, AdminBasePage.PATH_LOGIN)
    AdminBasePage(browser) \
        .input_login()
    AdminNavPanelEl(browser) \
        .go_to_nav_element('#menu-catalog', 'Products')
    assert AdminCatalogPage(browser).check_presence_item() is True, 'Данного товара нет'
    AdminCatalogPage(browser)\
        .click_button(AdminCatalogPage.CHECKBOX_ITEM)\
        .click_button(AdminCatalogPage.DELETE_ITEM_BTN)\
        .handler_alert()
    time.sleep(5)
    assert AdminCatalogPage(browser).check_presence_item() is False

