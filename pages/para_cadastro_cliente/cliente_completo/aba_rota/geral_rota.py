from playwright.sync_api import expect, Page

# Page Object para operações com rotas do cadastro de cliente.
class GeneralRefRoute:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba ROTA
    def click_aba_route(self):
        expect(self.page.locator('#menu_items_pri > :nth-child(3)')).to_be_visible()
        expect(self.page.locator('#menu_items_pri > :nth-child(3)')).to_have_text('Rotas')
        self.page.route('**/views/cliente/clienteRotasLista.html', lambda route: route.continue_())
        api_cliente_completo_rota = self.page.wait_for_response('**/views/cliente/clienteRotasLista.html')
        self.page.click('#menu_items_pri > :nth-child(3)')
        api_cliente_completo_rota

    # Botão + para adicionar uma nova Rota
    def click_added_new_route(self):
        expect(self.page.locator('.layout-align-end-end > .md-fab')).to_be_visible()
        expect(self.page.locator('.layout-align-end-end > .md-fab')).not_to_have_attribute('disabled', 'true')
        self.page.click('.layout-align-end-end > .md-fab')

    # Validar informações do modal rota enquanto ainda está vazio
    def modal_route_empty_validade(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Rotas')
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtTpEnderecoRota"]')).to_have_text('Tipo de endereço')
        expect(self.page.locator('#txtTpEnderecoRota')).to_be_visible()
        expect(self.page.locator('#txtTpEnderecoRota')).to_have_value('')
        expect(self.page.locator('#txtRota')).to_be_visible()
        expect(self.page.locator('#txtRota')).to_have_value('')
        expect(self.page.locator('.layout-gt-sm-column > .md-block > .ng-binding')).to_be_visible()

    # Mensagem Rota Incluída com sucesso
    def mess_route_added_success(self):
        expect(self.page.locator('#toast-container > :nth-child(1)')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_have_text('Aviso')
        expect(self.page.locator(':nth-child(1) > .toast-message')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-message')).to_have_text('Rota incluída com sucesso.')

    # Validar informações que foram adicionadas no cadastro de rota
    def info_route_added(self):
        expect(self.page.locator('.md-whiteframe-2dp')).to_be_visible()
        # Pode incluir aqui validações de texto se necessário