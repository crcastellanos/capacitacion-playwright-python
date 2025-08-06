import re
from playwright.sync_api import Page, expect


def test_example(browser) -> None:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    page.goto("http://172.20.1.22/atlantisev1desarrollo/login.aspx")
    page.locator("#vUSUCOD").click()
    page.locator("#vUSUCOD").fill("ADMIN")
    page.locator("#vUSUPASSWORD").fill("S&h.2025")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("link", name="Reportes contabilidad").click()
    page.locator("#vOBJOPCOD").select_option("LIBAUXN")
    page.locator("#IMAGE1").click()
    page.locator("#W0029vCUENTAID").click()
    page.locator("#W0029vCUENTAID").fill("243005")
    page.locator("#W0029vCUENTAID").press("Tab")
    page.locator("input[name=\"W0029vFECINI\"]").click()
    page.locator("input[name=\"W0029vFECINI\"]").fill("01012025")
    page.locator("input[name=\"W0029vFECINI\"]").press("Tab")
    page.locator("input[name=\"W0029vFECFIN\"]").click()
    page.locator("input[name=\"W0029vFECFIN\"]").fill("01022025")
    page.locator("input[name=\"W0029vFECFIN\"]").press("Tab")
    page.get_by_role("button", name="Procesar").click()
    page.get_by_role("row", name="243005 Gmf Depósitos de Ahorro BA 0,00 607.464,72 884.819,18 277.354,46", exact=True).get_by_role("link").click()
    page.get_by_role("button", name="Exportar a Excel").click()
    with page.expect_download() as download_info:
        page.locator("#W0029W0089vDESCARGAR_0007").click()
    download = download_info.value
    
    nombre_real = download.suggested_filename
    download.save_as(f"descargas/{nombre_real}.xlsx")