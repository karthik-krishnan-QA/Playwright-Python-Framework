import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_login_success(page: Page):
    
    login = LoginPage(page) 
    login.navigate()
    login.login("Admin", "admin123")
    page.wait_for_url("**/dashboard/index")
    assert "dashboard" in page.url
    print("Login Test Passed Successfully yes!")