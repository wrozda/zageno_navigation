from selenium.webdriver.common.by import By

from elements import Element
from pageObjects.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, context):
        super().__init__(context)

        self.email_field = Element(
            By.NAME, 'username', context
        )

        self.password_field = Element(
            By.NAME, 'password', context
        )

        self.next_button = Element(
            By.ID, 'idp-discovery-submit', context
        )

        self.login_button = Element(
            By.ID, 'okta-signin-submit', context
        )

    def fill_email_field(self, email):
        self.email_field.value(email)

    def fill_password_field(self, password):
        self.password_field.value(password)

    def click_next_button(self):
        self.next_button.click()

    def click_login_button(self):
        self.login_button.click()

    def login_user(self, **kwargs):
        self.fill_email_field(kwargs['email'])
        self.click_next_button()
        self.fill_password_field(kwargs['password'])
        self.click_login_button()
