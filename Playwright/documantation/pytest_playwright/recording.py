def test_skip_browser(page):
    page.goto("https://www.youtube.com")
    
# * Write in cmd "pytest recording.py --browser chromium --headed --video on"