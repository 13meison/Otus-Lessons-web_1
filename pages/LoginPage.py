from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_URL = 'index.php?route=account/login'
    WINDOWS_LOGIN = (By.CSS_SELECTOR, '.form-group')

    REGISTRATION_URL = 'index.php?route=account/register'
    PRIVACY_POLICY = (By.CSS_SELECTOR, 'form .pull-right')
