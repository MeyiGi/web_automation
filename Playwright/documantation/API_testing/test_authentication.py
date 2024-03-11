from playwright.async_api import Page

def test_auth(page: Page):
    page.goto("https://github.com/login")
    page.get_by_label("Username or email address").fill("****")
    page.get_by_label("Password").fill("****")
    page.get_by_role("button", name="Sign in", exact=True).click()
    page.wait_for_url("https://github.com/")