import sys
import re
import csv
import time
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

def test_abtest():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/")

        #try:
        #    page.get_by_role("button", name="Accetta tutto").click(timeout=3000)
        #except:
        #    pass
        #assert page.is_visible(google_text)
        #page.fill(google_text,"hello world")
        page.wait_for_timeout(5000)

        print("Titolo della pagina:", page.title())

        browser.close()


if __name__ == "__main__":
    test_abtest()