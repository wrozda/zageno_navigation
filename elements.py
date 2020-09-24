import os
from time import sleep

from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Element:
    """
    Element class initialize attributes inherited by other elements and contains common selenium methods which we
    can perform on elements.
    """

    element_collection = []

    def __init__(self, locator, selector, context):
        self.locator = locator
        self.selector = selector
        self.browser = context.browser
        self.context = context
        self.original_selector = selector
        self.logger = context.logger

    def __str__(self):
        return f"Element located by {self.locator} '{self.selector}'"

    @property
    def element(self):
        """ Use selenium wait in order to page loading and take element from DOM."""
        self.logger.info(f"Getting element: {self.locator} {self.selector}")

        return WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located((self.locator, self.selector))
        )

    # Waits on element
    def is_element_clickable(self, timeout: int = 7) -> bool:
        """Check if element is clickable."""
        try:
            element_is_clickable = WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable((self.locator, self.selector))
            )
            self.logger.debug(f"{self.locator} {self.selector} is clickable")
        except TimeoutException:
            element_is_clickable = False
            self.logger.warning(f"{self.selector} isn't clickable")

        return bool(element_is_clickable)

    def is_element_visible(self, timeout: int = 7) -> bool:
        """Check if element is visible."""
        try:
            element_is_visible = WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((self.locator, self.selector))
            )
            self.logger.debug(f"{self.locator} {self.selector} is visible")
        except TimeoutException:
            element_is_visible = False
            self.logger.warning(f"{self.selector} isn't visible")

        return bool(element_is_visible)

    # Actions on elements
    def mouse_hoover(self, timeout=7) -> None:
        """Hover the mouse over element."""
        if not self.is_element_visible(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't visible.")

        try:
            webdriver.ActionChains(self.browser).move_to_element(self.element).perform()
            self.logger.debug(f"Mouse is over the {self.locator}")
        except Exception as e:
            self.logger.exception(f"Mouse isn't over the {self.__str__()}. Exception: {e}")

    def click(self, timeout=7) -> None:
        """Click on element."""
        if not self.is_element_visible(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't visible.")

        if not self.is_element_clickable(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't clickable.")

        try:
            self.mouse_hoover(timeout=timeout)
            self.element.click()
            self.logger.debug(f"{self.locator} is clicked")
        except Exception as e:
            self.logger.exception(f"{self.__str__()} isn't clicked. Exception: {e}")

    # Values of elements
    def value(self, value: str, timeout=7) -> None:
        """Set value of element (i.e TextField)."""
        if not self.is_element_visible(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't visible.")

        if not self.is_element_clickable(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't clickable.")

        self._clear_element()
        try:
            self.element.send_keys(value)
            self.logger.debug(f"{self.selector} has value: {value}")
        except Exception as e:
            self.logger.exception(f"{self.selector} does not have value: {value}. Exception: {e}")

    def text(self, timeout=7) -> str:
        """Return element's text."""
        text = ""

        if not self.is_element_visible(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't visible.")

        if not self.is_element_clickable(timeout=timeout):
            self.logger.error(f" {self.__str__()} isn't clickable.")

        try:
            text = self.element.text
            self.logger.debug(f"Element {self.locator} has text: {text}")
        except Exception as e:
            self.logger.exception(f"Element {self.selector} could not get text. Exception: {e}")
        return text

    def set_parameters(self, *args):
        """Take a single string or array of strings and add them as parameter to selector string."""
        self.selector = self.original_selector.format(*args)
        return self

    # Private functions
    def _clear_element(self) -> None:
        """Clearing elements text area."""
        try:
            self.element.clear()
            self.logger.debug(f"{self.element} is clean")
        except Exception as e:
            self.logger.warning(f"{self.element} isn't clean. Exception: {e}")

    def _get_selector_with_text(self, row_text: str, row_number=None) -> str:
        """Get element by text in table row."""
        if row_number is not None:
            text_selector = "//tr['{}']//*[contains(text(),'{}')]".format(row_number, row_text)
        else:
            text_selector = "//tr//*[contains(text(),'{}')]".format(row_text)
        return self.selector + text_selector