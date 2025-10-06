from playwright.sync_api import expect, Page
from ...gerarDados import gerarCpf, gerarNomeAleatorio, gerarCNPJ, gerarNomeEmpresa

# Page Object para preencher dados pessoais do cliente.
class FillPerson:
    def __init__(self, page: Page):
        self.page = page

    # Validar e preencher campo Data Nascimento
    def date_birth(self):
        expect(self.page.locator('#txtDataNasc > .md-datepicker-button')).to_be_visible()
        expect(self.page.locator('#txtDataNasc > .md-datepicker-button')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtDataNasc"]')).to_have_text('Data Nascimento')
        self.page.wait_for_timeout(200)
        self.page.locator('input[aria-label="Data Nascimento"]').type('30/09/1998')

    # Validar e preencher campo Nome Completo - CPF
    def name_complete(self):
        nome_completo = gerarNomeAleatorio()
        expect(self.page.locator('label[for="txtRazaoSocial"]')).to_have_text('Nome Completo')
        expect(self.page.locator('#txtRazaoSocial')).to_be_visible()
        expect(self.page.locator('#txtRazaoSocial')).to_have_value('')
        self.page.locator('#txtRazaoSocial').type(nome_completo)

    # Validar e preencher campo Nome CNPJ - CPF
    def name_cnpj(self):
        razao_social = gerarNomeEmpresa()
        self.page.locator('#txtRazaoSocial').click()
        expect(self.page.locator('label[for="txtRazaoSocial"]')).to_have_text('Razão Social')
        expect(self.page.locator('#txtRazaoSocial')).to_be_visible()
        expect(self.page.locator('#txtRazaoSocial')).to_have_value('')
        self.page.locator('#txtRazaoSocial').type(razao_social, force=True)

    # Validar e preencher campo CPF
    def cpf_client(self):
        cpf = gerarCpf()
        expect(self.page.locator('label[for="txtCpfCnpj"]')).to_have_text('CPF')
        expect(self.page.locator('#txtCpfCnpj')).to_be_visible()
        expect(self.page.locator('#txtCpfCnpj')).to_have_value('')
        self.page.locator('#txtCpfCnpj').type(cpf, force=True)

    # Validar e preencher campo CNPJ
    def cnpj_client(self):
        cnpj = gerarCNPJ()
        expect(self.page.locator('label[for="txtCpfCnpj"]')).to_have_text('CPF')
        expect(self.page.locator('#txtCpfCnpj')).to_be_visible()
        expect(self.page.locator('#txtCpfCnpj')).to_have_value('')
        self.page.locator('#txtCpfCnpj').type(cnpj, force=True)

    # Validar e preencher campo Nome Fantasia - CPF
    def name_fantasy_cnpj(self):
        nome_cliente_cnpj = "Novo cadastro cliente CNPJ"
        expect(self.page.locator('label[for="txtNomeFantasia"]')).to_have_text('Nome Social')
        expect(self.page.locator('#txtNomeFantasia')).to_be_visible()
        expect(self.page.locator('#txtNomeFantasia')).to_have_value('')
        self.page.locator('#txtNomeFantasia').type(nome_cliente_cnpj, force=True)

    # Validar e preencher campo Nome Social - CPF
    def name_social(self):
        nome_social = gerarNomeAleatorio()
        expect(self.page.locator('label[for="txtNomeFantasia"]')).to_have_text('Nome Social')
        expect(self.page.locator('#txtNomeFantasia')).to_be_visible()
        expect(self.page.locator('#txtNomeFantasia')).to_have_value('')
        self.page.locator('#txtNomeFantasia').type(nome_social)

    # Validar e escolher sexo da pessoa
    def sex_client(self):
        expect(self.page.locator('label[for="txtSexo"]')).to_have_text('Sexo')
        expect(self.page.locator('#txtSexo')).to_be_visible()
        self.page.locator('#txtSexo').click(force=True)
        self.page.locator('.md-text.ng-binding', has_text="Masculino").click(force=True)