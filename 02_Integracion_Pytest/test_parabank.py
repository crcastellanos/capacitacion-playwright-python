from playwright.sync_api import Page
import pytest

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

@pytest.mark.only_browser("chromium")
def test_homepage(page: Page):
    page.goto(BASE_URL)
    assert page.title() == "ParaBank | Welcome | Online Banking"

def test_login_exitoso(page: Page):
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "john")
    page.fill('input[name="password"]', "demo")
    page.click('input[value="Log In"]')
    assert page.inner_text("h1.title") == "Accounts Overview"

def test_login_fallido(page: Page):
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "usuario_invalido")
    page.fill('input[name="password"]', "clave_invalida")
    page.click('input[value="Log In"]')
    assert "could not be verified" in page.inner_text("p.error")

def test_registro_usuario(page: Page):
    page.goto(BASE_URL)
    page.click("a[href*='register.htm']")
    assert "/register.htm" in page.url
    assert page.inner_text("h1.title") == "Signing up is easy!"

def test_logout(page: Page):
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "john")
    page.fill('input[name="password"]', "demo")
    page.click('input[value="Log In"]')
    page.click("a[href*='logout.htm']")
    assert page.url == "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"
    assert page.is_visible("input[value='Log In']")
