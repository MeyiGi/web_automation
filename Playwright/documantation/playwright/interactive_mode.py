# open terminal wiht python
# Write there theese code

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.youtube.com/")
page.screenshot(path="data/youtube.png")
browser.close()
playwright.stop()