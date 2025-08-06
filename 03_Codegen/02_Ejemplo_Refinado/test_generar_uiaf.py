import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.set_default_timeout(600000)
    page.goto("http://172.20.1.22/atlantisev1desarrollo/login.aspx")
    page.locator("#vUSUCOD").fill("ADMIN")
    page.locator("#vUSUPASSWORD").fill("S&h.2025")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("link", name="Otros reportes").click()
    page.get_by_role("cell", name="UIAF", exact=True).click()
    page.get_by_text("PRODUCTOS DE ASOCIADOS").click()
    page.locator("#W0037vOBJOPCOD").select_option("E")
    page.locator("#W0037vOBJOPCOD").select_option("E")
    page.locator("#W0037vOBJOPCOD").select_option("E")
    page.locator("#W0037vFECCORTE").fill("31072025")
    page.locator("#W0037vFECCORTE").press("Tab")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Procesar").click()

    def manejar_alerta(dialog):
        assert dialog.message() == "Archivo Generado"
        print("Mensaje del alert:", dialog.message())
        dialog.accept()

    page.on("dialog", manejar_alerta)

    with page.expect_download() as download_info:
        page.locator("#W0043vDESCARGAR_0004").click()
    download = download_info.value

    nombre_real = download.suggested_filename
    download.save_as(f"descargas/{nombre_real}.xlsx")