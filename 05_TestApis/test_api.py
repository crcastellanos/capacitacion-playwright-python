import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_api_success():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        await request_context.dispose()


@pytest.mark.asyncio
async def test_api_failed():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get("https://jsonplaceholder.typicode.com/posts/999999")
        assert response.status == 404
        await request_context.dispose()

@pytest.mark.asyncio
async def test_api_y_ui():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        post = await response.json()
        await request_context.dispose()
        assert post["title"].strip() != ""
        assert post["body"].strip() != ""

        browser = await p.chromium.launch(headless=False, slow_mo=300)
        page = await browser.new_page()

        await page.goto("http://0.0.0.0:5500/")

        await page.evaluate("mostrarPost", post)

        titulo = await page.locator("#titulo").text_content()
        cuerpo = await page.locator("#cuerpo").text_content()
        assert titulo != ""
        assert cuerpo != ""
        assert post["title"] in titulo
        # assert post["body"] in cuerpo
        assert post["body"].replace('\n', '') in cuerpo.replace('\n', '')

        await page.screenshot(path="captura_post.png")
        await browser.close()