import unittest
import pytest
from playwright.sync_api import Page

class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page : Page):
        self.page = page
        
    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        assert self.page.evaluate("1 + 1") == 2