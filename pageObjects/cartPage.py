from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from elements import Element
from pageObjects.basePage import BasePage


class CartPage(BasePage):

    def __init__(self, context):
        super().__init__(context)

        self.delete_product_icon = Element(
            By.ID, 'id_form-0-DELETE', context
        )

        self.confirm_deleting_product_button = Element(
            By.XPATH, '//button[contains(text(), "Confirm")]', context
        )
        self.cart_content = Element(
            By.XPATH, '//div[@class="checkout__main-content"]', context
        )

        self.empty_cart_message = Element(
            By.XPATH, '//p[contains(@class, "checkout-container__headline-empty")]', context
        )

        self.empty_cart_message_text = 'Your cart is empty'

    def click_delete_product_icon(self):
        self.delete_product_icon.click()

    def remove_products_from_cart(self):
        self.click_delete_product_icon()
        self.confirm_deleting_product_button.click()

    def check_if_cart_is_not_empty(self):
        self.cart_content.is_element_visible()
        assert_that(self.cart_content.is_element_visible(), equal_to(True), 'Cart is empty!')

    def check_empty_cart_message(self):
        self.empty_cart_message.is_element_visible()
        message = self.empty_cart_message.text()
        assert_that(message,
                    equal_to(self.empty_cart_message_text),
                    f'Message text {message} is not equal to expected text: {self.empty_cart_message_text}')
