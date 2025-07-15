import pytest
from pytest_bdd import scenarios, given, when, then
from pages.pages import LoginPage, InventoryPage
import logging

scenarios('../features/inventory.feature')

@pytest.fixture
def login_and_inventory(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    assert inventory_page.is_loaded(), "Not redirected to inventory page."
    return inventory_page

@given('the user is logged in')
def user_logged_in(login_and_inventory):
    logging.info('User logged in and on inventory page')

@when('the user is on the inventory page')
def on_inventory_page(login_and_inventory):
    assert login_and_inventory.is_loaded(), "Not on inventory page."
    logging.info('User is on inventory page')

@then('the product grid should be displayed')
def product_grid_displayed(login_and_inventory):
    items = login_and_inventory.get_inventory_items()
    assert len(items) > 0, "Product grid not displayed."
    logging.info(f'Product grid displayed with {len(items)} items')
