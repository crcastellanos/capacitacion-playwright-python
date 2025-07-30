import pytest
import asyncio
from playwright.async_api import async_playwright,expect

@pytest.mark.asyncio
async def test_run_activo():
    mensaje_alerta = ""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo=500)
        context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()
        await page.set_viewport_size({"width": 1962, "height": 1080})
        async def manejar_alerta(dialog):
            nonlocal mensaje_alerta
            mensaje_alerta = dialog.message
            await dialog.accept()
        page.once("dialog", manejar_alerta)
        await page.goto("http://127.0.0.1:5502/formularioTest/index.html")
        await page.fill("#nombre", "duber")
        await page.fill("#apellido", "garcia")
        await page.fill("input.edad", "22")
        await page.select_option("#genero","masculino")
        await page.check("#activo")
        await page.click("#Mostrar")
        await page.screenshot(path="capturas/captura_test.png", full_page=True)
        await expect(page.locator("#listaUsuarios").locator("#lblnombre")).to_be_visible()
        await expect(page.locator("#listaUsuarios").locator("#lbledad")).to_be_visible()
        await expect(page.locator("#listaUsuarios").locator("#lblgenero")).to_be_visible()
        await expect(page.locator("#listaUsuarios").locator("#lblestado")).to_be_visible()
        assert "Test" in await page.title()
        assert "duber garcia" in mensaje_alerta
        context.close()
        await browser.close()
