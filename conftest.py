import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def setup_home_page(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.accept_consent()
    return home_page