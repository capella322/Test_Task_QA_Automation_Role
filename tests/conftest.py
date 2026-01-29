import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

@pytest.fixture(scope="function")
def main_page(page: Page):
    return MainPage(page)

@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def secure_page(page: Page):
    return SecurePage(page)
