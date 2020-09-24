from abc import ABC

from pageObjects.basePage import BasePage
from pageObjects.cartPage import CartPage
from pageObjects.catalogPage import CatalogPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.productPage import ProductPage


class PageObjectsCreator(ABC):

    def __init__(self, context):
        self.base_page = BasePage(context)
        self.cart_page = CartPage(context)
        self.catalog_page = CatalogPage(context)
        self.home_page = HomePage(context)
        self.login_page = LoginPage(context)
        self.product_page = ProductPage(context)
