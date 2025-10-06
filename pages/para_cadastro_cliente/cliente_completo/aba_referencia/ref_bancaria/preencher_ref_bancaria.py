from ...gerarDados import gerarCpf, gerarNomeAleatorio, gerarEmailAleatorio, gerarTelefoneAleatorio
from ...gerarDadosPIX import (
    gerarChavePixTelefone, gerarChavePixTelefoneErrada, gerarChavePixEmailErrada, gerarChavePixCpfCnpjErrada,
    gerarChavePixEmail, gerarChavePixCPF, gerarChavePixAleatoria
)

# Page Object para preencher campos de referência bancária no cadastro de cliente.
class FillRefBanking:
    def __init__(self, page):
        self.page = page

    def bank(self):
        bank_field = self.page.locator('#txtBancoRefBanc')
        bank_field.click()
        first_option = self.page.locator('text=aaa')
        first_option.click()

    def agency(self):
        agency_field = self.page.locator('#txtAgenciaRefBanc')
        agency_field.click()
        agency_field.type('341')

    def account(self):
        account_field = self.page.locator('#txtContaRefBanc')
        account_field.click()
        account_field.type('12345-1')

    def date_opening(self):
        date_picker_input = self.page.locator('input.md-datepicker-input.md-input')
        date_picker_input.click()
        date_picker_input.type('30/09/2024')

    def ticket(self):
        boleto_field = self.page.locator('#txtBoletoRefBanc')
        boleto_field.click()
        option_sim = self.page.locator('text=Sim')
        option_sim.click(force=True)

    def phone(self):
        numero_telefone = gerarTelefoneAleatorio()
        phone_field = self.page.locator('#txtTelefoneRefBanc')
        phone_field.click()
        phone_field.type(numero_telefone)

    def manager(self):
        nome_gerente = gerarNomeAleatorio()
        manager_field = self.page.locator('#txtGerente')
        manager_field.click()
        manager_field.type(nome_gerente)

    def email(self):
        email_aleatorio = gerarEmailAleatorio()
        email_field = self.page.locator('#txtEmailRefBanc')
        email_field.click()
        email_field.type(email_aleatorio)

    def cpf_account_holder(self):
        cpf = gerarCpf()
        cpf_field = self.page.locator('#txtCpfCnpjRefBanc')
        expect(cpf_field).to_be_visible()
        cpf_field.type(cpf, force=True)

    def name_account_holder(self):
        nome_correntista = gerarNomeAleatorio()
        account_holder_name_field = self.page.locator('#txtNmCorrentRefBanc')
        account_holder_name_field.click()
        account_holder_name_field.type(nome_correntista)

    def type_account(self):
        tipo_conta_field = self.page.locator('#txtTpContaRefBanc')
        tipo_conta_field.click()
        opcao_conta_corrente = self.page.locator('div.md-text.ng-binding', has_text='Conta Corrente')
        opcao_conta_corrente.click(force=True)

    def operation(self):
        operacao_field = self.page.locator('#txtOperacaoRefBanc')
        operacao_field.type('1')

    def form_payment(self):
        forma_pagamento_field = self.page.locator('#txtFrmPag')
        forma_pagamento_field.click()
        opcao_pix = self.page.locator('div.md-text.ng-binding', has_text='PIX')
        opcao_pix.click()

    def type_key_pix_phone(self):
        tipo_chave_pix_field = self.page.locator('#txtIdTipoChavePix')
        tipo_chave_pix_field.click()
        opcao_telefone = self.page.locator('div.md-text.ng-binding', has_text='Telefone')
        opcao_telefone.click()

    def key_pix_phone_wrong(self):
        chave_pix_telefone_errada = gerarChavePixTelefoneErrada()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.type(chave_pix_telefone_errada)

    def type_key_pix_email(self):
        tipo_chave_pix_field = self.page.locator('#txtIdTipoChavePix')
        tipo_chave_pix_field.click()
        opcao_email = self.page.locator('div.md-text.ng-binding', has_text='Email')
        opcao_email.click()

    def key_pix_email_wrong(self):
        chave_pix_email_errada = gerarChavePixEmailErrada()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.type(chave_pix_email_errada)

    def type_key_pix_cpf_cnpj(self):
        tipo_chave_pix_field = self.page.locator('#txtIdTipoChavePix')
        tipo_chave_pix_field.click()
        opcao_cpf_cnpj = self.page.locator('div.md-text.ng-binding', has_text='CPF CNPJ')
        opcao_cpf_cnpj.click()

    def key_pix_cpf_cnpj_wrong(self):
        chave_pix_cpf_cnpj_errada = gerarChavePixCpfCnpjErrada()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.type(chave_pix_cpf_cnpj_errada)

    def type_key_pix_random(self):
        tipo_chave_pix_field = self.page.locator('#txtIdTipoChavePix')
        tipo_chave_pix_field.click()
        opcao_aleatoria = self.page.locator('div.md-text.ng-binding', has_text='Aleatória')
        opcao_aleatoria.click()

    def key_pix_phone(self):
        chave_pix_telefone = gerarChavePixTelefone()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        pix_key_field.clear()
        self.page.wait_for_timeout(200)
        expect(pix_key_field).to_have_value('')
        self.page.wait_for_timeout(200)
        pix_key_field.type(chave_pix_telefone)

    def key_pix_email(self):
        chave_pix_email = gerarChavePixEmail()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        pix_key_field.clear()
        self.page.wait_for_timeout(200)
        expect(pix_key_field).to_have_value('')
        self.page.wait_for_timeout(200)
        pix_key_field.type(chave_pix_email)

    def key_pix_cpf(self):
        chave_pix_cpf = gerarChavePixCPF()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        pix_key_field.clear()
        self.page.wait_for_timeout(200)
        expect(pix_key_field).to_have_value('')
        self.page.wait_for_timeout(200)
        pix_key_field.type(chave_pix_cpf)

    def key_pix_random(self):
        chave_pix_aleatoria = gerarChavePixAleatoria()
        pix_key_field = self.page.locator('#txtChavePix')
        pix_key_field.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        pix_key_field.clear()
        self.page.wait_for_timeout(200)
        expect(pix_key_field).to_have_value('')
        self.page.wait_for_timeout(200)
        pix_key_field.type(chave_pix_aleatoria)