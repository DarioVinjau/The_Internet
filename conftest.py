import os, pytest
from datetime import datetime
from playwright.sync_api import sync_playwright

is_ci = os.environ.get("CI") == "true"

@pytest.fixture
def browser_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_ci)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield browser
        context.tracing.stop(path = f"{datetime.now().strftime("%Y%m%d%H%M%S")}.zip")
        browser.close()
