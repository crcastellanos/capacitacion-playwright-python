from playwright.sync_api import Page

def test_navegador(page: Page):

    page.goto("https://www.whatismybrowser.com/")
    page.screenshot(path="01_Ejemplodemo.png")
    assert "WhatIsMyBrowser" in page.title()
    print("Finalizado")
