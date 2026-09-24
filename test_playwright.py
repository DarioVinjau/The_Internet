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

#qua dovrebbe andare in modalità incognito
def test_basic_auth(browser_instance):
    context = browser_instance.new_context(
        http_credentials={
            "username": "admin",
            "password": "admin"
        }
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_timeout(1000)
    page.get_by_text("Congratulations! You must have the proper credentials.")
    print("Testo trovato")
    page.close()
    context.close()
