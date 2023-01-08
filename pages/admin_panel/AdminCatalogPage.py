import time

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminCatalogPage(BasePage):
    NEW_ITEM_BTN = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    DELETE_ITEM_BTN = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
    FIELD_NAME_ITEM = (By.CSS_SELECTOR, "#input-name1")
    FIELD_META_TAG_ITEM = (By.CSS_SELECTOR, "#input-meta-title1")
    FIELD_MODEL_ITEM = (By.CSS_SELECTOR, "#input-model")
    SAVE_ITEM = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    TEST_NAME = 'test_name192-168'
    FILTER_BTN = (By.CSS_SELECTOR, '#button-filter')

    FILTER_NAME = (By.CSS_SELECTOR, 'input[name="filter_name"]')
    CHECKBOX_ITEM = (By.CSS_SELECTOR, 'input[name="selected[]"]')

    'windows'
    TAB_DATA = (By.CSS_SELECTOR, ".nav-tabs a[href='#tab-data']")

    def create_new_item_product(self):
        self.enter_to_field(AdminCatalogPage.FIELD_NAME_ITEM, AdminCatalogPage.TEST_NAME
                            )
        self.enter_to_field(AdminCatalogPage.FIELD_META_TAG_ITEM, 'test_tag')
        self.click_button(AdminCatalogPage.TAB_DATA)
        self.enter_to_field(AdminCatalogPage.FIELD_MODEL_ITEM, '1')
        self.click_button(AdminCatalogPage.SAVE_ITEM)
        return self

    def check_presence_item(self) -> bool:
        self.enter_to_field(AdminCatalogPage.FILTER_NAME, AdminCatalogPage.TEST_NAME)
        self.click_button(AdminCatalogPage.FILTER_BTN)
        answer = self.element_presence(AdminCatalogPage.CHECKBOX_ITEM)
        return answer





