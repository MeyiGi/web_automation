from playwright.sync_api import sync_playwright

def run(playwright):
    device = playwright.devices["Pixel 2"]
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context( **device )
    context2 = browser.new_context(
        viewport={"width" : 1280, "height" : 800},
        locale="de-DE",
        timezone_id="Europe/Berlin",
    )
    page1 = context1.new_page()
    page2 = context2.new_page()
    page1.goto("https://www.discovery.com")
    page2.goto("https://www.youtube.com")
    page1.pause()
    page2.pause()

with sync_playwright() as playwright:
    run(playwright)