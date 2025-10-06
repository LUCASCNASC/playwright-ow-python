from playwright.sync_api import expect, Page

# Page Object para operações com referência comercial em cadastro de cliente.
class GeneralRefCommercial:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba Comercial, dentro de Referencias
    def click_aba_ref_commercial(self):
        botao_comercial = self.page.locator('#menu_items_sec > .on')
        expect(botao_comercial).to_be_visible()
        expect(botao_comercial).not_to_have_attribute('disabled')
        self.page.route('**/views/cliente/refEtapaComercialLista.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/refEtapaComercialLista.html', timeout=40000)
        self.page.locator('#menu_items_sec > :nth-child(2)').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações da tela antes de adicionar qualquer coisa - aba referencia Comercial
    def validade_ref_commercial_empty(self):
        titulo_comercial = self.page.locator('h3')
        expect(titulo_comercial).to_be_visible()
        expect(titulo_comercial).to_have_text('Referências / Comercial')
        botao_adicionar = self.page.locator('.layout-align-end-end > .md-fab')
        expect(botao_adicionar).to_be_visible()
        expect(botao_adicionar).not_to_have_attribute('disabled')
        mensagem_sem_registro = self.page.locator('.text-align-center')
        expect(mensagem_sem_registro).to_be_visible()
        expect(mensagem_sem_registro).to_have_text('Não foi encontrado nenhum registro')
        botao_salvar = self.page.locator('.btn')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).not_to_have_attribute('disabled')

    # Clicar no botão + para adicionar uma nova referencia Comercial
    def click_add_new_ref_commercial(self):
        self.page.route('**/views/cliente/modalClienteRefComercial.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/modalClienteRefComercial.html', timeout=40000)
        self.page.locator('.layout-align-end-end > .md-fab').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações do modal Referencia Comercial antes de preencher as informações
    def modal_ref_commercial_empty(self):
        titulo_modal = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_have_text('Referência comercial')
        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_have_attribute('disabled')
        campo_empresa = self.page.locator('#txtEmpresaRefCom')
        expect(campo_empresa).to_be_visible()
        expect(campo_empresa).to_have_value('')
        expect(campo_empresa).not_to_have_attribute('disabled')
        info_campo_empresa = self.page.locator('label[for="txtEmpresaRefCom"]')
        expect(info_campo_empresa).to_have_text('Empresa')
        campo_contato = self.page.locator('#txtContatoRefCom')
        expect(campo_contato).to_be_visible()
        expect(campo_contato).to_have_value('')
        expect(campo_contato).not_to_have_attribute('disabled')
        info_campo_contato = self.page.locator('label[for="txtContatoRefCom"]')
        expect(info_campo_contato).to_have_text('Contato')
        campo_telefone = self.page.locator('#txtTelefoneRefCom')
        expect(campo_telefone).to_be_visible()
        expect(campo_telefone).to_have_value('')
        expect(campo_telefone).not_to_have_attribute('disabled')
        info_campo_telefone = self.page.locator('label[for="txtTelefoneRefCom"]')
        expect(info_campo_telefone).to_have_text('Telefone')
        campo_email = self.page.locator('#txtEmailRefCom')
        expect(campo_email).to_be_visible()
        expect(campo_email).to_have_value('')
        expect(campo_email).not_to_have_attribute('disabled')
        info_campo_email = self.page.locator('label[for="txtEmailRefCom"]')
        expect(info_campo_email).to_have_text('Email')
        campo_observacao = self.page.locator('#txtObsRefCom')
        expect(campo_observacao).to_be_visible()
        expect(campo_observacao).to_have_value('')
        expect(campo_observacao).not_to_have_attribute('disabled')
        info_campo_observacao = self.page.locator('label[for="txtObsRefCom"]')
        expect(info_campo_observacao).to_have_text('Observação')
        botao_salvar = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).to_have_attribute('disabled')

    # Clicar para salvar Referencia Comercial
    def click_save_ref_commercial(self):
        botao_salvar = self.page.locator('button', has_text='Salvar')
        expect(botao_salvar).to_be_visible()
        botao_salvar_habilitado = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar_habilitado).to_be_visible()
        expect(botao_salvar_habilitado).not_to_have_attribute('disabled')
        botao_salvar_habilitado.click()

    # Mensagem Referencia Comercial incluída com sucesso
    def mess_ref_commercial_added_sucess(self):
        toast_success = self.page.locator('.toast-success')
        expect(toast_success).to_be_visible()
        toast_title = self.page.locator('.toast-success > .toast-title')
        expect(toast_title).to_be_visible()
        expect(toast_title).to_have_text('Aviso')
        toast_message = self.page.locator('.toast-success > .toast-message')
        expect(toast_message).to_be_visible()
        expect(toast_message).to_have_text('Referência Comercial incluída com sucesso.')

    # Validando informações que foram adicionadas no cadastro de referencia Comercial
    def info_ref_commercial_added(self):
        nome_pessoa = self.page.locator('.md-whiteframe-2dp > .ng-scope > :nth-child(1) > .ng-binding')
        expect(nome_pessoa).to_be_visible()
        contato = self.page.locator('[ng-show="(item.contato)"]')
        expect(contato).to_be_visible()
        telefone = self.page.locator('[ng-show="(item.telefone)"]')
        expect(telefone).to_be_visible()
        email = self.page.locator('[ng-show="(item.email)"]')
        expect(email).to_be_visible()