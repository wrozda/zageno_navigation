from behave import step

from testData.credentials import TEST_USER
from testData.products import test_product


@step('I log in to the ZAGENO app')
def step_impl(context):
    context.pages.base_page.open()
    context.pages.base_page.accept_cookie()
    context.pages.base_page.accept_country_modal()
    context.pages.base_page.click_login_button()
    context.pages.login_page.login_user(**TEST_USER)


@step('I search the product using searchbar')
def step_impl(context):
    context.pages.home_page.search_product(test_product)
    context.pages.catalog_page.find_product_and_open_pdp(test_product)


@step('I add the product to cart')
def step_impl(context):
    context.pages.product_page.check_if_pdp_title_contains_text(test_product)
    context.pages.product_page.add_product_to_cart()


@step('Product should have been in cart')
def step_impl(context):
    context.pages.base_page.go_to_checkout()
    context.pages.cart_page.check_if_cart_is_not_empty()


@step('Cart should be empty')
def step_impl(context):
    context.pages.cart_page.remove_products_from_cart()
    context.pages.cart_page.check_empty_cart_message()
