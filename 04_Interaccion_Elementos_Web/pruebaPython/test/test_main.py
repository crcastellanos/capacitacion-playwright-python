import pytest
import asyncio
from playwright.async_api import async_playwright,expect

@pytest.mark.asyncio
async def test_run_activo():
    mensaje_alerta = ""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo=600)
        context = await browser.new_context(            
            record_video_dir="videos/",
            record_video_size={"width": 1920, "height": 950},
            viewport={"width": 1920, "height": 950},
            device_scale_factor=1.0,
        )
        page = await context.new_page()
        await page.set_viewport_size({"width": 1962, "height": 950})
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
        await page.screenshot(path="capturas/captura_test1.png", full_page=True)
        await page.fill("#nombre", "karmen")
        await page.fill("#apellido", "Lopez")
        await page.fill("input.edad", "45")
        await page.select_option("#genero","femenino")
        await page.check("#activo")
        await page.click("#Mostrar")
        await page.screenshot(path="capturas/captura_test2.png", full_page=True)

        await expect(page.locator("#lblnombre_0")).to_have_text("Nombre: duber garcia ")
        await expect(page.locator("#lblnombre_1")).to_have_text("Nombre: karmen Lopez ")
        assert "Test" in await page.title()
        assert "duber garcia" in mensaje_alerta
        await context.close()
        await browser.close()
