import pytest
from playwright.sync_api import Page

@pytest.mark.only_browser("chromium")
def test_informacion_asociado(page: Page):
    # 1. Ingresar al sitio y loguearse
    page.goto("http://172.20.1.22/atlantisev1desarrollo/login.aspx")
    page.locator("#vUSUCOD").fill("ADMIN")
    page.locator("#vUSUPASSWORD").fill("S&h.2025")
    page.get_by_role("button", name="Confirmar").click()

    # 2. Navegar a Información del asociado
    page.get_by_role("link", name="Información del asociado").click()
    page.locator("#W0018vCASOIDE").click()
    page.locator("#W0018vCASOIDE").fill("63453708")
    page.get_by_role("button", name="Buscar Asociado").click()

    # 3. Acceder a la pestaña y visualizar datos
    page.locator('[id="004Tab"]').click()
    page.locator("#W0021W0013vVISUALIZAR_0001").click()

    # 4. Esperar a que aparezca el popup
    page.wait_for_selector("div.PopupBorder", state="visible", timeout=15000)

    # 5. Localizar iframe del popup
    iframe_handle = page.wait_for_selector(
        'div.PopupBorder div.PopupContent iframe[src*="wpvispag.aspx"]',
        state="attached",
        timeout=15000
    )
    frame = iframe_handle.content_frame()
    assert frame is not None, "No se pudo obtener el contentFrame"

    # 6. Esperar a que la tabla tenga filas de datos
    frame.wait_for_function(
        "document.querySelectorAll('#Grid1ContainerTbl tbody tr[gxrow]').length > 0",
        timeout=15000
    )

    # 7. Extraer las celdas visibles
    tabla = frame.eval_on_selector_all(
        "#Grid1ContainerTbl tbody tr[gxrow]",
        """rows => rows.map(row =>
            Array.from(row.querySelectorAll('td'))
                .filter(td => getComputedStyle(td).display !== 'none')
                .map(td => td.innerText.trim())
        )"""
    )

    # 8. Mostrar las filas en consola
    for fila in tabla:
        print(" | ".join(fila))

    # 9. (Opcional) Cerrar popup
    page.locator('div.PopupBorder span[id$="_cls"]').click()

    # 10. Pausar para inspección manual (debug)
    #page.pause()
