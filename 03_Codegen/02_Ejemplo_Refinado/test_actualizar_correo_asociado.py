import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://172.20.1.22/atlantisev1desarrollo/login.aspx")
    page.locator("#vUSUCOD").fill("ADMIN")
    page.locator("#vUSUPASSWORD").fill("S&h.2025")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("link", name="Asociados", exact=True).click()
    page.locator("#vCASOIDE").fill("37752652")
    page.get_by_role("button", name="Buscar").click()
    page.get_by_role("button", name="Actualizar").click()
    valor_previo = page.get_by_role("textbox", name="Email").input_value()
    page.get_by_role("textbox", name="Email").fill("carolina.gomez@solucionessyh.com")
    page.get_by_text("Confirmar").click()
    valor_final = page.get_by_role("textbox", name="Email").input_value()
    print("")
    print("Correo anterior:", valor_previo)
    print("Correo actualizado:", valor_final)
