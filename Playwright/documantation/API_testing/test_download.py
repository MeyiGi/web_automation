from playwright.async_api import Page

def test_download(page: Page):
    page.goto("https://www.jetbrains.com/pycharm/download/?section=windows")
    
    with page.expect_download() as download_info:
        page.get_by_role("button", name=".exe").first.click()
        
    download = download_info.value
    print(download.path())
    download.save_as("C:\Information Technology\python\Playwright\course\API_testing\ecompony.txt")