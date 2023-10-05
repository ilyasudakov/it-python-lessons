import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def authenticated_page(page: Page):
    url = "http://localhost:8000"

    page.goto(f"{url}/admin")
    page.get_by_label("Username:").fill("ilya")
    page.get_by_label("Password:").fill("123456")
    page.get_by_text("Log in").click()

    expect(page.get_by_text("Django administration")).to_be_visible()

    return page
