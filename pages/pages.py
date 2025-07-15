
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[data-test="username"]')
        self.password_input = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def load(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        if self.error_message.is_visible():
            return self.error_message.inner_text()
        return None

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator('[data-test="inventory-container"]')
        self.inventory_items = page.locator('.inventory_item')
        self.cart_icon = page.locator('.shopping_cart_link')

    def is_loaded(self):
        return self.page.url.endswith('/inventory.html') and self.inventory_container.is_visible()

    def get_inventory_items(self):
        return self.inventory_items.all_text_contents()

    def go_to_cart(self):
        self.cart_icon.click()

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_list = page.locator('.cart_list')

    def is_loaded(self):
        return self.page.url.endswith('/cart.html') and self.cart_list.is_visible()

    def get_cart_items(self):
        return self.cart_list.all_text_contents()
