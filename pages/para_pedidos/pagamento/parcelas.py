from playwright.sync_api import expect, Page

# Page Object para seleção de parcelas no recebimento.
class ChooseInstallmentReceipt:
    def __init__(self, page: Page):
        self.page = page

    # Seleciona a opção "1X" (uma parcela).
    def one(self):
        parcela1x = self.page.locator('.active > md-collapsible-body > .layout-column > [style="position: relative"] > :nth-child(1) > div.ng-binding')
        expect(parcela1x).to_be_visible()
        expect(parcela1x).not_to_be_disabled()
        parcela1x.click(force=True)

    # Seleciona a opção "2X" (duas parcelas).
    def two(self):
        parcela2x = self.page.locator('.active > md-collapsible-body > .layout-column > [style="position: relative"] > :nth-child(2) > div.ng-binding')
        expect(parcela2x).to_be_visible()
        expect(parcela2x).not_to_be_disabled()
        parcela2x.click(force=True)

    # Seleciona a opção "4X" (quatro parcelas).
    def for_(self):
        self.page.locator('[style="position: relative"] > :nth-child(4) > div.ng-binding').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        parcela4x = self.page.locator('[style="position: relative"] > :nth-child(4) > div.ng-binding')
        expect(parcela4x).to_be_visible()
        expect(parcela4x).not_to_be_disabled()
        self.page.route('GET', '/views/carrinho/modalSeguroPrestamista.html', lambda route: route.fulfill())
        parcela4x.click(force=True)
        self.page.wait_for_response(
            lambda response: '/views/carrinho/modalSeguroPrestamista.html' in response.url and response.status == 200,
            timeout=40000
        )