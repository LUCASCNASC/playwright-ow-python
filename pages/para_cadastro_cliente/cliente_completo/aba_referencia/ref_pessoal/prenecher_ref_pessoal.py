from ...gerarDados import gerarNomeAleatorio, gerarEmailAleatorio, gerarTelefoneAleatorio, gerarRelacionamento

# Page Object para preencher campos de referência pessoal no cadastro de cliente.
class FillRefGuys:
    def __init__(self, page):
        self.page = page

    # referência pessoal - escolher Nome
    def name(self):
        nome = gerarNomeAleatorio()
        self.page.click('#txtNomeRefPes')
        self.page.type('#txtNomeRefPes', nome)

    # referência pessoal - escolher Email
    def email(self):
        email = gerarEmailAleatorio()
        self.page.click('#txtEmailRefPes')
        self.page.type('#txtEmailRefPes', email)

    # referência pessoal - escolher Telefone
    def phone(self):
        numero_telefone = gerarTelefoneAleatorio()
        self.page.click('#txtTelefoneRefPes')
        self.page.type('#txtTelefoneRefPes', numero_telefone)

    # referência pessoal - escolher Relacionamento
    def relationship(self):
        relacionamento = gerarRelacionamento()
        self.page.click('#txtRelacionamentoRefPes')
        self.page.type('#txtRelacionamentoRefPes', relacionamento)