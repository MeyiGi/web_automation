import pytest

@pytest.mark.skip_browser("firefox")
def test_skip_browser(page):
    page.goto("https://www.youtube.com")
    
# * Write in cmd "pytest test_skip_browser.py --browser chromium --browser webkit --browser --firefox --headed"