from selenium.webdriver.common.by import By

from elements import Element
from pageObjects.basePage import BasePage


class HomePage(BasePage):

    def __init__(self, context):
        super().__init__(context)

        self.search_field = Element(
            By.NAME, 'search', context
        )

        self.find_products_button = Element(
            By.XPATH, '//button[contains(@class, "js-search-btn")]', context
        )

    def click_search_button(self):
        self.find_products_button.click()

    def search_product(self, product):
        self.search_field.value(product)
        self.click_search_button()