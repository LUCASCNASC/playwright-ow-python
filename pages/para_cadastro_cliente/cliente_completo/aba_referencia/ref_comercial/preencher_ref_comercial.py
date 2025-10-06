from ...gerarDados import gerarEmailAleatorio, gerarTelefoneAleatorio, gerarNomeEmpresa, gerarObservação

# Page Object para preencher campos de referência comercial no cadastro de cliente.
class FillRefCommercial:
    def __init__(self, page):
        self.page = page

    # referência Comercial - Empresa
    def enterprise(self):
        empresa = gerarNomeEmpresa()
        campo_empresa = self.page.locator('#txtEmpresaRefCom')
        campo_empresa.type(empresa)

    # referência Comercial - Contato
    def contact(self):
        contato = gerarTelefoneAleatorio()
        campo_contato = self.page.locator('#txtContatoRefCom')
        campo_contato.type(contato)

    # referência Comercial - Telefone
    def phone(self):
        telefone = gerarTelefoneAleatorio()
        campo_telefone = self.page.locator('#txtTelefoneRefCom')
        campo_telefone.type(telefone)

    # referência Comercial - Email
    def email(self):
        email = gerarEmailAleatorio()
        campo_email = self.page.locator('#txtEmailRefCom')
        campo_email.type(email)

    # referência Comercial - Observação
    def observation(self):
        observacao = gerarObservação()
        campo_observacao = self.page.locator('#txtObsRefCom')
        campo_observacao.type(observacao)