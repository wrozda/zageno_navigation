from selenium.webdriver.common.by import By

from elements import Element
from pageObjects.basePage import BasePage


class CatalogPage(BasePage):

    def __init__(self, context):
        super().__init__(context)

        self.product_title = Element(
            By.XPATH, '//a[contains(text(), "{}")]', context
        )

    def find_product_and_open_pdp(self, product_name):
        self.product_title.set_parameters(product_name)
        self.product_title.click()
