from playwright.sync_api import expect, Page

# Page Object para operações com telefones de clientes.
class GeneralRefPhone:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba Telefone
    def click_aba_phone(self):
        expect(self.page.locator('#menu_items_pri > :nth-child(4)')).to_be_visible()
        expect(self.page.locator('#menu_items_pri > :nth-child(4)')).to_have_text('Telefones')
        self.page.route('**/services/v3/dados_tabela/tipotelefone', lambda route: route.continue_())
        api_cliente_completo_telefones = self.page.wait_for_response('**/services/v3/dados_tabela/tipotelefone')
        self.page.click('#menu_items_pri > :nth-child(4)')
        api_cliente_completo_telefones

    # Botão + para adicionar um novo Telefone
    def click_added_new_phone(self):
        expect(self.page.locator('.layout-align-end-end > .md-fab')).to_be_visible()
        expect(self.page.locator('.layout-align-end-end > .md-fab')).not_to_have_attribute('disabled', 'true')
        self.page.route('**/views/cliente/ModalClienteTelefone.html', lambda route: route.continue_())
        api_ModalClienteTelefone = self.page.wait_for_response('**/views/cliente/ModalClienteTelefone.html')
        self.page.click('.layout-align-end-end > .md-fab')
        api_ModalClienteTelefone

    # Validar informações do modal Telefone enquanto ainda está vazio
    def modal_phone_empty_validade(self):
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_have_text('Telefone')
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtTpTel"]')).to_have_text('Tipo de telefone')
        expect(self.page.locator('#txtTpTel')).to_be_visible()
        expect(self.page.locator('#txtTpTel')).to_have_value('')
        expect(self.page.locator('label[for="txtNumTel"]')).to_have_text('Número')
        expect(self.page.locator('#txtNumTel')).to_be_visible()
        expect(self.page.locator('#txtNumTel')).to_have_value('')
        expect(self.page.locator('label[for="txtRamalTel"]')).to_have_text('Ramal')
        expect(self.page.locator('#txtRamalTel')).to_be_visible()
        expect(self.page.locator('#txtRamalTel')).to_have_value('')
        expect(self.page.locator('#btnModalAddTel')).to_be_visible()
        expect(self.page.locator('#btnModalAddTel')).not_to_have_attribute('disabled', 'true')

    # Clicar no botão salvar telefone
    def click_save_phone(self):
        expect(self.page.locator('#btnModalAddTel')).to_be_visible()
        expect(self.page.locator('#btnModalAddTel')).not_to_have_attribute('disabled', 'true')
        self.page.click('#btnModalAddTel', force=True)

    # Validando informações que foram adicionadas no cadastro de telefone
    def info_phone_added(self):
        expect(self.page.locator('.md-whiteframe-2dp')).to_be_visible()
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('Padrão')
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('(44)')
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('435')

    # Validar mensagem de telefone incluído com sucesso
    def mess_phone_added_sucess(self):
        expect(self.page.locator('.toast-success')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_have_text('Aviso')
        expect(self.page.locator('.toast-success > .toast-message')).to_be_visible()
        expect(self.page.locator('.toast-success > .toast-message')).to_have_text('Telefone incluído com sucesso.')