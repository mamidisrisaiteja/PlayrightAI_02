from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[data-test="username"]')
        self.password_input = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')

    def load(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator('[data-test="inventory-container"]')
        self.inventory_items = page.locator('.inventory_item')

    def is_loaded(self):
        return self.page.url.endswith('/inventory.html') and self.inventory_container.is_visible()

    def get_inventory_items(self):
        return self.inventory_items.all_text_contents()
