import pytest
from playwright.async_api import Page

@pytest.mark.asyncio
async def test_async_navegador(page: Page):
    await page.goto("https://www.whatismybrowser.com/")
    await page.screenshot(path="demo.png")
    titulo = await page.title()
    print(titulo)
    assert "What browser? My browser? Is my browser out of date?" in titulo