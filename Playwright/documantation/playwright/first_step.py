import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=2000)
#     page = browser.new_page()
#     page.goto("https://playwright.dev/python/")
#     print(page.title())
#     page.close()
    
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=20000)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python/")
        print(await page.title())
        await page.close()
        
asyncio.run(main())