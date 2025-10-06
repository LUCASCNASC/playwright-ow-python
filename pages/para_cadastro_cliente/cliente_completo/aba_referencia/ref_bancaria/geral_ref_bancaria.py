from playwright.sync_api import expect, Page

# Page Object para operações com referência bancária em cadastro de cliente.
class GeneralRefBanking:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba Bancária, dentro de Referências
    def click_aba_ref_banking(self):
        banc_button = self.page.locator('#menu_items_sec > :nth-child(3)')
        expect(banc_button).to_be_visible()
        expect(banc_button).not_to_have_attribute('disabled', 'true')
        self.page.route('**/views/cliente/refEtapaBancariaLista.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/refEtapaBancariaLista.html', timeout=40000)
        banc_button.click()
        response

    # Validar informações da tela antes de adicionar qualquer coisa
    def validate_aba_ref_banking_empty(self):
        title = self.page.locator('h3')
        expect(title).to_be_visible()
        expect(title).to_have_text('Referências / Bancária')
        add_button = self.page.locator('.layout-align-end-end > .md-fab')
        expect(add_button).to_be_visible()
        expect(add_button).not_to_have_attribute('disabled', 'true')
        no_record_message = self.page.locator('.text-align-center')
        expect(no_record_message).to_be_visible()
        expect(no_record_message).to_have_text('Não foi encontrado nenhum registro')
        save_button = self.page.locator('.btn')
        expect(save_button).to_be_visible()
        expect(save_button).not_to_have_attribute('disabled', 'true')

    # Clicar no botão + para adicionar nova referência bancária
    def click_add_new_ref_banking(self):
        self.page.route('**/views/cliente/modalClienteRefBancaria.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/modalClienteRefBancaria.html', timeout=40000)
        self.page.locator('.layout-align-end-end > .md-fab').click()
        response

    # Validar informações do modal Referência Bancária antes de preencher
    def modal_ref_banking_empty(self):
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_have_text('Referência bancária')
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('#txtBancoRefBanc')).to_be_visible()
        expect(self.page.locator('#txtBancoRefBanc')).to_have_value('')
        expect(self.page.locator('#txtBancoRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtBancoRefBanc"]')).to_have_text('Banco')
        expect(self.page.locator('#txtAgenciaRefBanc')).to_be_visible()
        expect(self.page.locator('#txtAgenciaRefBanc')).to_have_value('')
        expect(self.page.locator('#txtAgenciaRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtAgenciaRefBanc"]')).to_have_text('Agência')
        expect(self.page.locator('#txtContaRefBanc')).to_be_visible()
        expect(self.page.locator('#txtContaRefBanc')).to_have_value('')
        expect(self.page.locator('#txtContaRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtContaRefBanc"]')).to_have_text('Conta')
        expect(self.page.locator('.md-datepicker-button')).to_be_visible()
        expect(self.page.locator('.md-datepicker-button')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('input.md-datepicker-input.md-input')).to_be_visible()
        expect(self.page.locator('input.md-datepicker-input.md-input')).to_have_value('')
        expect(self.page.locator('input.md-datepicker-input.md-input')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('#txtBoletoRefBanc')).to_be_visible()
        expect(self.page.locator('#txtBoletoRefBanc')).to_have_value('')
        expect(self.page.locator('#txtBoletoRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtBoletoRefBanc"]')).to_have_text('Boleto')
        expect(self.page.locator('#txtTelefoneRefBanc')).to_be_visible()
        expect(self.page.locator('#txtTelefoneRefBanc')).to_have_value('')
        expect(self.page.locator('#txtTelefoneRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtTelefoneRefBanc"]')).to_have_text('Telefone')
        expect(self.page.locator('#txtGerente')).to_be_visible()
        expect(self.page.locator('#txtGerente')).to_have_value('')
        expect(self.page.locator('#txtGerente')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtGerente"]')).to_have_text('Gerente')
        expect(self.page.locator('#txtEmailRefBanc')).to_be_visible()
        expect(self.page.locator('#txtEmailRefBanc')).to_have_value('')
        expect(self.page.locator('#txtEmailRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtEmailRefBanc"]')).to_have_text('Email')
        expect(self.page.locator('#txtCpfCnpjRefBanc')).to_be_visible()
        expect(self.page.locator('#txtCpfCnpjRefBanc')).to_have_value('')
        expect(self.page.locator('#txtCpfCnpjRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtCpfCnpjRefBanc"]')).to_have_text('CPF/CNPJ correntista')
        expect(self.page.locator('#txtNmCorrentRefBanc')).to_be_visible()
        expect(self.page.locator('#txtNmCorrentRefBanc')).to_have_value('')
        expect(self.page.locator('#txtNmCorrentRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtNmCorrentRefBanc"]')).to_have_text('Nome do correntista')
        expect(self.page.locator('#txtTpContaRefBanc')).to_be_visible()
        expect(self.page.locator('#txtTpContaRefBanc')).to_have_value('')
        expect(self.page.locator('#txtTpContaRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtTpContaRefBanc"]')).to_have_text('Tipo de conta')
        expect(self.page.locator('#txtOperacaoRefBanc')).to_be_visible()
        expect(self.page.locator('#txtOperacaoRefBanc')).to_have_value('')
        expect(self.page.locator('#txtOperacaoRefBanc')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtOperacaoRefBanc"]')).to_have_text('Operação')
        expect(self.page.locator('#txtFrmPag')).to_be_visible()
        expect(self.page.locator('#txtFrmPag')).to_have_value('')
        expect(self.page.locator('#txtFrmPag')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtFrmPag"]')).to_have_text('Forma de pagamento')
        expect(self.page.locator('#txtIdTipoChavePix')).to_be_visible()
        expect(self.page.locator('#txtIdTipoChavePix')).to_have_value('')
        expect(self.page.locator('#txtIdTipoChavePix')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtIdTipoChavePix"]')).to_have_text('Tipo chave PIX')
        expect(self.page.locator('#txtChavePix')).to_be_visible()
        expect(self.page.locator('#txtChavePix')).to_have_value('')
        expect(self.page.locator('#txtChavePix')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtChavePix"]')).to_have_text('Chave PIX')
        expect(self.page.locator('#btnModalAddRefPessoal')).to_have_attribute('disabled', 'true')

    # Clicar para salvar Referencia Bancaria
    def click_save_ref_banking(self):
        save_button_by_id = self.page.locator('#btnModalAddRefPessoal')
        expect(save_button_by_id).to_be_visible()
        expect(save_button_by_id).not_to_have_attribute('disabled', 'true')
        save_button_by_id.click()

    # Mensagem Referencia Bancária incluída com sucesso
    def mess_ref_banking_added_sucess(self):
        toast_success = self.page.locator('.toast-success')
        expect(toast_success).to_be_visible()
        toast_title = self.page.locator('.toast-success > .toast-title')
        expect(toast_title).to_be_visible()
        expect(toast_title).to_have_text('Aviso')
        toast_message = self.page.locator('.toast-success > .toast-message')
        expect(toast_message).to_be_visible()
        expect(toast_message).to_have_text('Referência Bancária incluída com sucesso.')

    # Validar informações que foram adicionadas no cadastro de referencia bancária
    def info_ref_banking_added(self):
        address_card = self.page.locator('.md-whiteframe-2dp')
        expect(address_card).to_be_visible()
        expect(address_card).to_contain_text('aaa')
        expect(address_card).to_contain_text('Agencia:')
        expect(address_card).to_contain_text('Conta:')

    # Mensagem de chave pix telefone inválida
    def mess_ref_banking_key_pix_phone_invalid(self):
        error_card_title = self.page.locator('.toast-error > .toast-title')
        expect(error_card_title).to_be_visible()
        expect(error_card_title).to_have_text('Erro identificado')
        error_message = self.page.locator('.toast-error > .toast-message')
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(
            'Chave Pix Telefone não informada ou inválida. Deve conter o DDD (2 digitos) mais o número do celular (9 dígitos). Informar somente números'
        )

    # Mensagem de chave pix email inválida
    def mess_ref_banking_key_pix_email_invalid(self):
        error_card_title = self.page.locator('.toast-error > .toast-title')
        expect(error_card_title).to_be_visible()
        expect(error_card_title).to_have_text('Erro identificado')
        error_message = self.page.locator('.toast-error > .toast-message')
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text('Chave Pix E-Mail não informada ou inválida.')

    # Mensagem de chave pix CPF/CNPJ inválida
    def mess_ref_banking_key_pix_cpf_cnpj_invalid(self):
        error_card_title = self.page.locator('.toast-error > .toast-title')
        expect(error_card_title).to_be_visible()
        expect(error_card_title).to_have_text('Erro identificado')
        error_message = self.page.locator('.toast-error > .toast-message')
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(
            'Chave Pix CPF/CNPJ não informada ou inválida. Deve conter um CPF ou CNPJ válido. Informar somente números.'
        )

    # Mensagem de chave pix aleatória inválida
    def mess_ref_banking_key_pix_random_invalid(self):
        error_card_title = self.page.locator('.toast-error > .toast-title')
        expect(error_card_title).to_be_visible()
        expect(error_card_title).to_have_text('Erro identificado')
        error_message = self.page.locator('.toast-error > .toast-message')
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(
            'Chave Pix Aleatória não informada ou inválida. A chave aleatória deve ser informada com os traços que separa cada conjunto da chave aleatória, ao todo são 4 traços.'
        )

    # Arrastar referencia bancaria para fazer a edição
    def drag_edit_ref_banking(self):
        address_card = self.page.locator('.md-whiteframe-2dp')
        address_card.hover()
        address_card.dispatch_event('mousedown', button=0)
        address_card.dispatch_event('mousemove', clientX=100, clientY=0)
        address_card.dispatch_event('mouseup')

    # Clicar no lápis para editar referencia bancária
    def click_edit_ref_banking(self):
        pencil_icon = self.page.locator('.btn-remove-item-list > :nth-child(1) > .md-raised > .ng-binding')
        expect(pencil_icon).to_be_visible()
        full_button = self.page.locator('.btn-remove-item-list > :nth-child(1) > .md-raised')
        expect(full_button).to_be_visible()
        expect(full_button).not_to_have_attribute('disabled', 'true')
        full_button.click(force=True)
        self.page.route('**/services/v3/forma_pagamento', lambda route: route.continue_())
        self.page.wait_for_response('**/services/v3/forma_pagamento', timeout=40000)