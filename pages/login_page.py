from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.locator("input[name='username']")
        self._password = page.locator("input[name='password']")
        self._login_btn = page.locator("button[type='submit']")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, user, pwd):
        self._username.fill(user)
        self._password.fill(pwd)
        self._login_btn.click()