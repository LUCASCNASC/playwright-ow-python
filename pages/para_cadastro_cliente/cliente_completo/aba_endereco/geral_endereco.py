from playwright.sync_api import expect, Page

# Page Object para operações com endereço de cliente.
class GeneralAdress:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba ENDEREÇO
    def click_aba_adress(self):
        expect(self.page.locator('#menu_items_pri > :nth-child(2)')).to_be_visible()
        expect(self.page.locator('#menu_items_pri > :nth-child(2)')).to_have_text('Endereço')
        self.page.route('**/services/v3/dados_tabela/tipoendereco', lambda route: route.continue_())
        self.page.locator('#menu_items_pri > :nth-child(2)').scroll_into_view_if_needed()
        self.page.locator('#menu_items_pri > :nth-child(2)').click(force=True)
        self.page.wait_for_response('**/services/v3/dados_tabela/tipoendereco', timeout=40000)

    # Mensagem Endereço Incluído com sucesso
    def mess_adress_added_success(self):
        expect(self.page.locator('.toast-success')).to_be_visible()
        expect(self.page.locator('.toast-success > .toast-title')).to_be_visible()
        expect(self.page.locator('.toast-success > .toast-title')).to_have_text('Aviso')
        expect(self.page.locator('.toast-success > .toast-message')).to_be_visible()
        expect(self.page.locator('.toast-success > .toast-message')).to_have_text('Endereço incluído com sucesso.')

    # Botão + para adicionar um novo endereço
    def click_add_new_adress(self):
        expect(self.page.locator('.layout-align-end-end > .md-fab')).to_be_visible()
        expect(self.page.locator('.layout-align-end-end > .md-fab')).not_to_have_attribute('disabled', 'true')
        self.page.route('**/views/cliente/ModalClienteEndereco.html', lambda route: route.continue_())
        self.page.locator('.layout-align-end-end > .md-fab').click()
        self.page.wait_for_response('**/views/cliente/ModalClienteEndereco.html', timeout=40000)

    # Validar informações do modal Endereço enquanto ainda está vazio
    def modal_adress_empty_validate(self):
        expect(self.page.locator('label[for="txtCepEndereco"]')).to_have_text('CEP')
        expect(self.page.locator('#txtCepEndereco')).to_be_visible()
        expect(self.page.locator('#txtCepEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtRuaEndereco"]')).to_have_text('Endereço')
        expect(self.page.locator('#txtRuaEndereco')).to_be_visible()
        expect(self.page.locator('#txtRuaEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtNumEndereco"]')).to_have_text('Número')
        expect(self.page.locator('#txtNumEndereco')).to_be_visible()
        expect(self.page.locator('#txtNumEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtComplEndereco"]')).to_have_text('Complemento')
        expect(self.page.locator('#txtComplEndereco')).to_be_visible()
        expect(self.page.locator('#txtComplEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtBairroEndereco"]')).to_have_text('Bairro')
        expect(self.page.locator('#txtBairroEndereco')).to_be_visible()
        expect(self.page.locator('#txtBairroEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtCxPostEndereco"]')).to_have_text('Caixa Postal')
        expect(self.page.locator('#txtCxPostEndereco')).to_be_visible()
        expect(self.page.locator('#txtCxPostEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtUfEndereco"]')).to_have_text('Estado')
        expect(self.page.locator('#txtUfEndereco')).to_be_visible()
        expect(self.page.locator('#txtUfEndereco')).to_have_value('')
        expect(self.page.locator('label[for="txtCidEndereco"]')).to_have_text('Cidade')
        expect(self.page.locator('#txtCidEndereco')).to_be_visible()
        expect(self.page.locator('#txtCidEndereco')).to_have_value('')

    # Clicar para abrir opções de tipo endereço
    def click_open_type_adress(self):
        self.page.locator('#txtTpEndereco').click(force=True)

    # Validando informações que foram adicionadas no endereço
    def info_adress_added(self):
        expect(self.page.locator('.md-whiteframe-2dp')).to_be_visible()
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('Padrão')
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('RUA PETÚNIA - 66 - PARQUE INDUSTRIAL')
        expect(self.page.locator('.md-whiteframe-2dp')).to_contain_text('87065-300')

    # Clicar no botão salvar endereço
    def click_save_adress(self):
        self.page.locator('#btnModalAddEndereco').click()

    # Validando card endereço antes de preencher os campos
    def card_adress_empty_validate(self):
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_have_text('Endereço')
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('#btnModalAddEndereco')).to_be_visible()
        expect(self.page.locator('#btnModalAddEndereco')).not_to_have_attribute('not.disabled', 'true')
        expect(self.page.locator('label[for="txtTpEndereco"]')).to_have_text('Tipo de Endereço')
        expect(self.page.locator('#txtTpEndereco')).to_be_visible()
        expect(self.page.locator('#txtTpEndereco')).to_have_value('')