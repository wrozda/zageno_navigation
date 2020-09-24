from selenium.webdriver.common.by import By

from elements import Element


class BasePage:
    URL = ""

    def __init__(self, context):
        self.context = context

        # MENU OPTIONS
        self.login_button = Element(
            By.XPATH, '//div[contains(@class, "header-menu__logged-out")]', context
        )

        self.cart_icon = Element(
            By.XPATH, '//div[contains(@class,"js-cart-menu-container")]', context
        )

        self.go_to_checkout_button = Element(
            By.XPATH, '//a[contains(text(),"Go to Checkout")]', context
        )

        self.cookie_button = Element(
            By.XPATH, '//input[@value="Agree and Proceed"]', context
        )

        self.country_modal_accept_button = Element(
            By.XPATH, '//a[contains(text(),"I understand")]', context
        )

    def open(self):
        self.context.browser.get(self.context.base_e2e_url + self.URL)

    def click_login_button(self):
        self.login_button.click()

    def accept_cookie(self):
        self.cookie_button.click()

    def accept_country_modal(self):
        self.country_modal_accept_button.click()

    def go_to_checkout(self):
        self.cart_icon.mouse_hoover()
        self.go_to_checkout_button.click()
