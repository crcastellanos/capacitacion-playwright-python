from playwright.sync_api import sync_playwright
import time

def abrir_pagina(nombre_prueba, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        print(f"⏳ Iniciando prueba {nombre_prueba}")
        start = time.time()
        page.goto(url)
        page.wait_for_timeout(2000)
        page.screenshot(path=f"{nombre_prueba}.png")
        browser.close()
        print(f"✅ Finalizó {nombre_prueba} en {time.time() - start:.2f} seg\n")

def main():
    abrir_pagina("prueba1", "https://example.com")
    abrir_pagina("prueba2", "https://playwright.dev")
    abrir_pagina("prueba3", "https://www.wikipedia.org")

main()
