import pytest
from pytest_bdd import scenarios, given, when, then
from pages.pages import LoginPage, InventoryPage, CartPage
import logging

scenarios('../features/cart.feature')

@pytest.fixture
def logged_in_inventory(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    assert inventory_page.is_loaded(), "Not redirected to inventory page."
    return inventory_page

@given('the user is logged in')
def user_logged_in(logged_in_inventory):
    logging.info('User logged in and on inventory page')

@when('the user clicks the cart icon')
def user_clicks_cart_icon(logged_in_inventory):
    logged_in_inventory.go_to_cart()
    logging.info('User clicked cart icon')

@then('the cart page should display selected items')
def cart_page_displays_items(page):
    cart_page = CartPage(page)
    assert cart_page.is_loaded(), "Cart page not loaded."
    items = cart_page.get_cart_items()
    assert items is not None, "No items found in cart."
    logging.info(f'Cart page loaded with items: {items}')
