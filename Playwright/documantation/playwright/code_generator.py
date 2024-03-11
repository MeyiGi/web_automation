# Write in cmd "playwright codegen"

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("dogs")
    page.get_by_role("link", name="Dogs in warfare Overview of").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
