import asyncio
from playwright.async_api import async_playwright
import time

async def abrir_pagina(nombre_prueba, url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=150000)
        page = await browser.new_page()
        print(f"⏳ Iniciando prueba {nombre_prueba}")
        start = time.time()
        await page.goto(url)
        await page.wait_for_timeout(2000)
        await page.screenshot(path=f"{nombre_prueba}.png")
        await browser.close()
        print(f"✅ Finalizó {nombre_prueba} en {time.time() - start:.2f} seg\n")

async def main():
    tareas = [
        abrir_pagina("prueba1", "https://example.com"),
        abrir_pagina("prueba2", "https://playwright.dev"),
        abrir_pagina("prueba3", "https://www.wikipedia.org")
    ]
    await asyncio.gather(*tareas)

if __name__ == "__main__":
    asyncio.run(main())
