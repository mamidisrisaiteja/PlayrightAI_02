import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.pages import LoginPage, InventoryPage
import logging

scenarios('../features/auth.feature')

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@given('the user is on the login page')
def user_on_login_page(login_page):
    login_page.load()
    logging.info('Navigated to login page')

@when(parsers.parse('the user logs in with username "{username}" and password "{password}"'))
def user_logs_in(login_page, username, password):
    login_page.login(username, password)
    logging.info(f'Attempted login with username: {username}')

@then('the user should be redirected to the inventory page')
def redirected_to_inventory(inventory_page):
    assert inventory_page.is_loaded(), "Not redirected to inventory page."
    logging.info('Redirected to inventory page')

@then('the inventory items should be visible')
def inventory_items_visible(inventory_page):
    items = inventory_page.get_inventory_items()
    assert len(items) > 0, "No inventory items found."
    logging.info(f'Inventory items found: {len(items)}')

@then('an error message should be displayed')
def error_message_displayed(login_page):
    error = login_page.get_error_message()
    assert error is not None and error != '', "Error message not displayed."
    logging.info(f'Error message displayed: {error}')
