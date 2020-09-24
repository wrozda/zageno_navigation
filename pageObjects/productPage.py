from selenium.webdriver.common.by import By

from elements import Element
from pageObjects.basePage import BasePage


class ProductPage(BasePage):

    def __init__(self, context):
        super().__init__(context)

        self.add_to_cart_button = Element(
            By.NAME, 'add_cart', context
        )

        self.pdp_title = Element(
            By.XPATH, '//h3[contains(@class, "pdp__title")]/parent::div', context
        )

    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def check_if_pdp_title_contains_text(self, text):
        self.pdp_title.is_element_visible()
        title = self.pdp_title.text()

        if text not in title:
            raise Exception(f'PDP title: {title} does not contain text: {text}')
