from playwright.sync_api import Playwright, sync_playwright

# TODO: after you run this code write in cmd "playwright show-trace data/tracing/trace.zip"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    
    # !: Trace viewer starting here !
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page.get_by_label("Top languages").click()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("language")
    page.get_by_label("Search Wikipedia").press("Enter")
    page.get_by_role("link", name="Study", exact=True).click()
    page.get_by_role("link", name="Early history").click()
    page.get_by_role("link", name="comparative method").nth(1).click()
    
    # !: Trace viewer ending here !
    context.tracing.stop(path="data/tracing/trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)