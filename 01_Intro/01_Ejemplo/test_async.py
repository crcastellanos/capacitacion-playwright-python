import asyncio
from playwright.sync_api import sync_playwright

async def main():
    async with async_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.whatismybrowser.com/")
        page.screenshot(path="demo.png")
        browser.close()