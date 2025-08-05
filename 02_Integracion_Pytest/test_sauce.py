from playwright.sync_api import Page
import pytest

@pytest.mark.only_browser("chromium")
def test_sauce_link(page: Page):
    page.goto("https://saucedemo.com/")
    assert page.title() == "Swag Labs"

"""
def test_sauce_implicito(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"
"""

def test_pagina_inventario(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."

def test_login_exitoso(page: Page):
    page.goto("/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    assert "/inventory.html" in page.url
    assert page.locator(".title").inner_text() == "Products"

def test_login_fallido(page: Page):
    page.goto("/")
    page.fill('[data-test="username"]', "locked_out_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')

    assert "Epic sadface: Sorry, this user has been locked out." in page.inner_text('[data-test="error"]')

def test_ordenamiento_productos_precio(page: Page):
    page.goto("/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    
    page.select_option('[data-test="product-sort-container"]', 'lohi')
    prices = [float(p.inner_text().replace("$", "")) for p in page.locator(".inventory_item_price").all()]
    assert prices == sorted(prices)
    print(prices)

def test_cierre_sesion(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    
    assert "/" in page.url
    assert page.locator('[data-test="login-button"]').is_visible()