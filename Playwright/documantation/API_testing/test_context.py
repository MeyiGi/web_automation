from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone11 = p.devices["iPhone 11 Pro"]
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    
    context1 = browser.new_context(
        **iphone11,
        locale="de-DE",
        geolocation={"longitude" : 12.492507, "latitude" : 41.889938},
        permissions=["geolocation"],
    )
    context2 = browser.new_context()
    
    page1 = context1.new_page()
    page1.goto("https://m.youtube.com/results?sp=mAEA&search_query=%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5")
    page2 = context2.new_page()
    page2.goto("https://www.github.com")
    
    browser.close()