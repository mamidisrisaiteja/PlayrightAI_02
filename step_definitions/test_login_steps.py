
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pytest_bdd import scenarios, given, when, then, parsers
from pages.pages import LoginPage, InventoryPage
import pytest

scenarios('../features/login.feature')

@given('the user is on the login page')
def user_on_login_page(page):
    login_page = LoginPage(page)
    login_page.load()
    pytest.login_page = login_page
    pytest.inventory_page = InventoryPage(page)

@when(parsers.parse('the user logs in with username "{username}" and password "{password}"'))
def user_logs_in(username, password):
    pytest.login_page.login(username, password)

@then('the user should be redirected to the inventory page')
def redirected_to_inventory():
    assert pytest.inventory_page.is_loaded(), "Not redirected to inventory page."

@then('the inventory items should be visible')
def inventory_items_visible():
    items = pytest.inventory_page.get_inventory_items()
    assert len(items) > 0, "No inventory items found."
