# write in terminal "PLAYWRIGHT_BROWSER_PATH=0 playwright install chromium"

# In my case nothing changed maybe in your will be some staff

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.youtube.com/")
page.screenshot(path="data/youtube.png")
browser.close()
playwright.stop()