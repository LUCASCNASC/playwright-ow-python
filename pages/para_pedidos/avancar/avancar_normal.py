from playwright.sync_api import expect, Page

# Page Object para seleção e pesquisa de clientes no pedido.
class ChooseClient:
    def __init__(self, page: Page):
        self.page = page

    # Escolhe cliente CPF para gerar pedido de venda (com intenções de compra).
    def pedido2(self):
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').wait_for_timeout(500)
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').type('    48976249089{enter}')
        self.page.wait_for_timeout(2000)

        expect(self.page.locator('.md-title')).to_be_visible()
        expect(self.page.locator('.md-title')).to_have_text('Intenções de Compra')
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_have_text('O cliente selecionado possui produtos adicionados nas intenções de compra, deseja acessá-los?')
        expect(self.page.locator('.md-confirm-button')).to_be_visible()
        expect(self.page.locator('.md-confirm-button')).not_to_be_disabled()
        expect(self.page.locator('.md-confirm-button')).to_have_text('Sim')
        expect(self.page.locator('.md-cancel-button')).to_be_visible()
        expect(self.page.locator('.md-cancel-button')).not_to_be_disabled()
        expect(self.page.locator('.md-cancel-button')).to_have_text('Não')
        self.page.locator('.md-cancel-button').click(force=True)

    # Pesquisa e seleciona cliente CPF para o pedido, fluxo com rota.
    def with_route(self):
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').wait_for_timeout(500)
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').type('48976249089 {ArrowDown}')

        self.page.route('**/views/cliente/modalClientes.html', lambda route: route.continue_())
        api_modal_clientes = self.page.wait_for_response('**/views/cliente/modalClientes.html')
        self.page.locator('.md-block > .ng-binding').click()
        api_modal_clientes

        self.page.route('**/consultaclientes/*', lambda route: route.continue_())
        api_consulta_clientes = self.page.wait_for_response('**/consultaclientes/*')
        api_consulta_clientes

        self.page.route('**/services/v3/pedido_validar_cliente', lambda route: route.continue_())
        api_pedido_validar_cliente = self.page.wait_for_response('**/services/v3/pedido_validar_cliente')

        self.page.locator('.md-3-line > div.md-button > .md-no-style').click()
        api_pedido_validar_cliente