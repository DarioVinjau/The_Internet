import os
import pytest
from playwright.sync_api import sync_playwright

is_ci = os.environ.get("CI") == "true"

@pytest.fixture
def browser_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_ci)
        yield browser
        browser.close()
