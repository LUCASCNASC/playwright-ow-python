from playwright.sync_api import expect, Page

# Page Object para operações com anexos em cadastros de clientes.
class GeneralAnexo:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba de anexos.
    def click_aba_attachment(self):
        expect(self.page.locator('#menu_mais_pri > :nth-child(4)')).to_be_visible()
        expect(self.page.locator('#menu_mais_pri > :nth-child(4)')).not_to_have_attribute('disabled', 'true')
        self.page.route('**/services/v3/dados_tabela/tipoanexo', lambda route: route.continue_())
        self.page.locator('#menu_mais_pri > :nth-child(4)').click()
        self.page.wait_for_response('**/services/v3/dados_tabela/tipoanexo', timeout=40000)

    # Validar informações da tela antes de fazer upload do arquivo anexo.
    def validate_aba_attachment_empty(self):
        expect(self.page.locator('[ng-controller="ListaDeAnexosController"] > :nth-child(1)')).to_be_visible()
        expect(self.page.locator('[ng-controller="ListaDeAnexosController"] > :nth-child(1)')).to_have_text('Anexos')
        expect(self.page.locator('#ComboTipoAnexo')).to_be_visible()
        expect(self.page.locator('#ComboTipoAnexo')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="ComboTipoAnexo"]')).to_have_text('Tipo de anexo')
        expect(self.page.locator('.area-botoes > .md-primary')).to_be_visible()
        expect(self.page.locator('.area-botoes > .md-primary')).to_have_attribute('disabled', 'true')
        expect(self.page.locator('.text-align-center')).to_be_visible()
        expect(self.page.locator('.text-align-center')).to_have_text('Não foi encontrado nenhum registro')
        expect(self.page.locator('.btn')).to_be_visible()
        expect(self.page.locator('.btn')).not_to_have_attribute('disabled', 'true')

    # Seleciona o primeiro tipo de anexo.
    def select_first_type_attachment(self):
        self.page.locator('#ComboTipoAnexo').click()
        self.page.locator('div.md-text.ng-binding', has_text='Assinatura do Termo de Adesão do Titular').click()

    # Confirma envio do arquivo na mensagem "Deseja enviar o arquivo selecionado?".
    def confirm_send_file(self):
        expect(self.page.locator('.md-title')).to_be_visible()
        expect(self.page.locator('.md-title')).to_have_text('Deseja enviar o arquivo selecionado?')
        expect(self.page.locator('.md-cancel-button')).to_be_visible()
        expect(self.page.locator('.md-cancel-button')).to_have_text('Não')
        expect(self.page.locator('.md-confirm-button')).to_be_visible()
        expect(self.page.locator('.md-confirm-button')).to_have_text('Sim')
        self.page.locator('.md-confirm-button').click()

    # Mensagem de anexo incluído com sucesso.
    def mess_attachment_add_success(self):
        expect(self.page.locator('.toast')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_have_text('Aviso')
        expect(self.page.locator('.toast-message')).to_be_visible()
        expect(self.page.locator('.toast-message')).to_have_text('Anexo cadastrado com sucesso!')

    # Validar se o anexo realmente foi adicionado.
    def validate_attachment_added(self):
        from datetime import datetime
        hoje = datetime.now()
        data_atual = hoje.strftime('%d/%m/%Y')
        expect(self.page.locator('.md-whiteframe-2dp')).to_be_visible()
        expect(self.page.locator('small.list-title')).to_be_visible()
        expect(self.page.locator('small.list-title')).to_contain_text('Anexo inserido em')
        expect(self.page.locator('small.list-title')).to_contain_text(data_atual)