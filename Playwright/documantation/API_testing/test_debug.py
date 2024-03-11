from playwright.async_api import Page

def test_microsoft(page: Page):
    page.goto("https://www.microsoft.com")
    page.get_by_label("Celebrating women this month").click()
    # PWDEBUG=1 pytest test_debug.py -s <-- Only work on wsl