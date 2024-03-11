import pytest

@pytest.mark.only_browser("chromium")
def test_skip_browser(page):
    page.goto("https://www.youtube.com")
    
# * Write in cmd "pytest test__only_browser.py --browser chromium --browser webkit --browser --firefox --headed"