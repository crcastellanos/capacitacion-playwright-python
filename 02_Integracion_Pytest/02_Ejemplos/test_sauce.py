from playwright.sync_api import Page
#import pytest

def test_sauce_link(page: Page):
    page.goto("https://saucedemo.com/")
    assert page.title() == "Swag Labs"

"""
def test_sauce_implicito(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"
"""

def test_pagina_inventario(page: Page):
    page.goto("https://saucedemo.com/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."