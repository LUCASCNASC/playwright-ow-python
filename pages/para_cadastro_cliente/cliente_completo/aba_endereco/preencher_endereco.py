from playwright.sync_api import expect, Page

# Page Object para preencher dados do endereço do cliente.
class FillAdress:
    def __init__(self, page: Page):
        self.page = page

    # Selecionar tipo de endereço
    def type_adress(self):
        self.page.locator('.md-text.ng-binding:has-text("Padrão")').click(force=True)

    # Preencher campo CEP no cadastro de endereço e pesquisar
    def cep_adress(self):
        cep_cadastro = "87065300"
        self.page.locator('#txtCepEndereco').type(cep_cadastro, force=True)
        expect(self.page.locator('.md-icon-float > .ng-binding')).to_be_visible()
        self.page.route('**/services/v3/cidade?uf=PR', lambda route: route.continue_())
        self.page.locator('.md-icon-float > .ng-binding').click(force=True)
        self.page.wait_for_response('**/services/v3/cidade?uf=PR', timeout=40000)

    # Preencher campo Número no cadastro de endereço
    def number_adress(self):
        numero_endereco = "66"
        self.page.locator('#txtNumEndereco').type(numero_endereco, force=True)