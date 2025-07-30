from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.whatismybrowser.com/")
    page.screenshot(path="repo/Capacitacion-Playwright-Python/01_Intro/01_Ejemplodemo.png")
    browser.close()