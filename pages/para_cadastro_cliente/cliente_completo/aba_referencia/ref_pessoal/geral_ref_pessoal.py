from playwright.sync_api import expect, Page
from datetime import datetime

# Page Object para operações com referência pessoal em cadastro de cliente.
class GeneralRefGuys:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba Pessoal, dentro de Referencias
    def click_aba_ref_guys(self):
        botao_pessoal = self.page.locator('#menu_items_sec > .on')
        expect(botao_pessoal).to_be_visible()
        expect(botao_pessoal).not_to_have_attribute('disabled')
        self.page.route('**/views/cliente/refEtapaBancariaLista.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/refEtapaBancariaLista.html', timeout=40000)
        self.page.locator('#menu_items_sec > :nth-child(3)').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações da tela antes de adicionar qualquer coisa - aba referencia Pessoal
    def validate_aba_empty(self):
        titulo_aba_pessoal = self.page.locator('h3')
        expect(titulo_aba_pessoal).to_be_visible()
        expect(titulo_aba_pessoal).to_have_text('Referências / Pessoal')
        botao_adicionar = self.page.locator('.layout-align-end-end > .md-fab')
        expect(botao_adicionar).to_be_visible()
        expect(botao_adicionar).not_to_have_attribute('disabled')
        mensagem_nenhum_registro = self.page.locator('.text-align-center')
        expect(mensagem_nenhum_registro).to_be_visible()
        expect(mensagem_nenhum_registro).to_have_text('Não foi encontrado nenhum registro')
        botoes_genericos = self.page.locator('.btn')
        expect(botoes_genericos).to_be_visible()
        expect(botoes_genericos).not_to_have_attribute('disabled')

    # Clicar no botão + para adicionar uma nova referencia pessoal
    def click_add_new(self):
        self.page.route('**/views/cliente/modalClienteRefPessoal.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/modalClienteRefPessoal.html', timeout=40000)
        self.page.locator('.layout-align-end-end > .md-fab').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações do modal Referencia Pessoal antes de preencher as informações
    def modal_empty(self):
        titulo_modal = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_have_text('Referência pessoal')
        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_have_attribute('disabled')
        campo_nome = self.page.locator('#txtNomeRefPes')
        expect(campo_nome).to_be_visible()
        expect(campo_nome).not_to_have_attribute('disabled')
        informativo_nome = self.page.locator('label[for="txtNomeRefPes"]')
        expect(informativo_nome).to_have_text('Nome')
        campo_email = self.page.locator('#txtEmailRefPes')
        expect(campo_email).to_be_visible()
        expect(campo_email).not_to_have_attribute('disabled')
        informativo_email = self.page.locator('label[for="txtEmailRefPes"]')
        expect(informativo_email).to_have_text('Email')
        campo_telefone = self.page.locator('#txtTelefoneRefPes')
        expect(campo_telefone).to_be_visible()
        expect(campo_telefone).not_to_have_attribute('disabled')
        informativo_telefone = self.page.locator('label[for="txtTelefoneRefPes"]')
        expect(informativo_telefone).to_have_text('Telefone')
        campo_relacionamento = self.page.locator('#txtRelacionamentoRefPes')
        expect(campo_relacionamento).to_be_visible()
        expect(campo_relacionamento).not_to_have_attribute('disabled')
        informativo_relacionamento = self.page.locator('label[for="txtRelacionamentoRefPes"]')
        expect(informativo_relacionamento).to_have_text('Relacionamento')
        campo_data_inclusao = self.page.locator('#txtDtInclusaoRefPes')
        expect(campo_data_inclusao).to_be_visible()
        expect(campo_data_inclusao).to_have_attribute('disabled')
        informativo_data_inclusao = self.page.locator('label[for="txtDtInclusaoRefPes"]')
        expect(informativo_data_inclusao).to_have_text('Data inclusão')
        botao_salvar_desabilitado = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar_desabilitado).to_be_visible()
        expect(botao_salvar_desabilitado).to_have_attribute('disabled')

    # Clicar para salvar Referencia Pessoal
    def click_save(self):
        botao_salvar = self.page.locator('button:has-text("Salvar")')
        expect(botao_salvar).to_be_visible()
        botao_salvar_habilitado = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar_habilitado).to_be_visible()
        expect(botao_salvar_habilitado).not_to_have_attribute('disabled')
        botao_salvar_habilitado.click()

    # Mensagem Referencia Pessoal incluída com sucesso
    def mess_ref_guys_added_sucess(self):
        toast_success = self.page.locator('.toast-success')
        expect(toast_success).to_be_visible()
        toast_title = toast_success.locator('.toast-title')
        expect(toast_title).to_be_visible()
        expect(toast_title).to_have_text('Aviso')
        toast_message = toast_success.locator('.toast-message')
        expect(toast_message).to_be_visible()
        expect(toast_message).to_have_text('Referência Pessoal incluída com sucesso.')

    # Validar informações que foram adicionadas no cadastro de referencia Pessoal
    def info_added(self):
        hoje = datetime.now()
        data_atual = hoje.strftime('%d/%m/%Y')
        nome_pessoa = self.page.locator('.flex-gt-sm-70 > :nth-child(1) > .ng-binding')
        expect(nome_pessoa).to_be_visible()
        relacionamento = self.page.locator('.flex-gt-sm-70 > :nth-child(3)')
        expect(relacionamento).to_be_visible()
        telefone = self.page.locator('[ng-show="(item.telefone)"]')
        expect(telefone).to_be_visible()
        email = self.page.locator('[ng-show="(item.email)"]')
        expect(email).to_be_visible()
        data_inclusao = self.page.locator('.layout-align-gt-sm-center-end > .list-title > b')
        expect(data_inclusao).to_be_visible()
        valor_data_inclusao = self.page.locator('.layout-align-gt-sm-center-end > .list-title')
        expect(valor_data_inclusao).to_be_visible()
        expect(valor_data_inclusao).to_contain_text(data_atual)

    # Validar modal vazio da referência pessoal
    def modal_ref_guys_empty(self):
        self.modal_empty()