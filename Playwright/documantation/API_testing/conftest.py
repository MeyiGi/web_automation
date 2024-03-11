import pytest
from typing import Dict
from playwright.sync_api import BrowserType

@pytest.fixture(scope="session")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict,
):
    context = browser_type.launch_persistent_context(
        ".foobar",
        ** {
            **browser_type_launch_args,
            **browser_context_args,
            "locale" : "en-GB",
        }
    )
    yield context
    context.close()