from playwright.sync_api import sync_playwright

playwright_instance = sync_playwright().start()
browser = playwright_instance.chromium.launch(headless=False)

def test_abtest(browser_instance):
    page = browser_instance.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.click("text=A/B Testing")
    print("Titolo della pagina:", page.title())
    print(page.text_content("//p"))
    page.close()

def test_add_remove_elements(browser_instance):
    page = browser_instance.new_page()
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.click("//button[contains(text(),'Add Element')]")
    print("Elemento aggiunto")
    page.wait_for_timeout(1000)
    page.click("//button[contains(text(),'Delete')]")
    print("Elemento eliminato")
    page.wait_for_timeout(1000)
    page.close()

try:
    test_abtest(browser)
    #test_add_remove_elements(browser)
finally:
    browser.close()
    playwright_instance.stop()