from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminBasePage(BasePage):
    """
    Сюда буду складывать все методы: логина, навигации и других общих вещей
    """

    PATH_LOGIN = 'admin'
    FIELD_LOGIN = (By.CSS_SELECTOR, 'input[name="username"]')
    FIELD_PASS = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN = 'admin'
    PASSWORD = 'admin'
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.text-right button')

    def input_login(self):
        self.enter_to_field(self.FIELD_LOGIN, self.LOGIN)
        self.enter_to_field(self.FIELD_PASS, self.PASSWORD)
        self.click_button(self.BUTTON_LOGIN)
