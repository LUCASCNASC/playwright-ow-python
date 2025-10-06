from playwright.sync_api import expect, Page

# Page Object para preencher dados de rota no cadastro de cliente.
class FillRefRoute:
    def __init__(self, page: Page):
        self.page = page

    # Preencher rota no cadastro de rota e escolher as opções certas
    def routa_complete(self):
        rota_cadastro = "560"
        expect(self.page.locator('label[for="txtRota"]')).to_have_text('Rota')
        self.page.type('#txtRota', rota_cadastro)
        self.page.wait_for_timeout(200)

        self.page.route('**/services/v3/rota?idrota=560', lambda route: route.continue_())
        api_rota_560 = self.page.wait_for_response('**/services/v3/rota?idrota=560')
        self.page.click('.layout-gt-sm-column > .md-block > .ng-binding', force=True)
        api_rota_560
        self.page.click('v-pane-header.ng-scope > div', force=True)
        self.page.wait_for_timeout(200)

        self.page.route('**/services/v3/local_entrega?rota=560', lambda route: route.continue_())
        api_local_entrega_560 = self.page.wait_for_response('**/services/v3/local_entrega?rota=560')
        self.page.click('text=560 - T.A. ROTA AUTOMAÇÃO MARINGÁ')
        self.page.click('text=560 - T.A. CIDADE AUTOMAÇÃO')
        api_local_entrega_560

    # Selecionar tipo de endereço do modal de rota Padrão
    def type_adress_route(self):
        self.page.click('#txtTpEnderecoRota', force=True)
        self.page.locator('.md-text.ng-binding', has_text='Padrão').click(force=True)