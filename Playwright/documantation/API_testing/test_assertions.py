import pytest
from playwright.sync_api import Page, expect

def test_submitted(page: Page) -> None:
    page.goto("https://www.google.com")
    page.locator(selector="button[role=\"button\"]:has-text(\"Settings\")")
    expect(page.locator(selector="text=Search settings")).to_have_text("Search settings")
        
def test_visible(page: Page) -> None:
    page.goto("https://www.google.com")
    page.locator(selector="button[role=\"button\"]:has-text(\"Settings\")")
    expect(page.locator(selector="text=Terms")).to_be_visible()