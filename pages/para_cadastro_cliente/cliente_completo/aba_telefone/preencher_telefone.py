from ...gerarDados import gerarTelefoneAleatorio

# Page Object para preencher campos do telefone em cadastro de cliente.
class FillRefPhone:
    def __init__(self, page):
        self.page = page

    # Selecionar tipo de telefone na aba telefone
    def type_phone(self):
        self.page.locator('#txtTpTel').click(force=True)
        self.page.locator('.md-text.ng-binding', has_text='Padrão').click(force=True)

    # Preencher campo Número no cadastro de telefone
    def number_phone(self):
        numero_telefone = gerarTelefoneAleatorio()
        self.page.locator('#txtNumTel').type(numero_telefone)

    # Preencher campo Ramal no cadastro de telefone
    def ramal_phone(self):
        ramal_telefone = "435"
        self.page.locator('#txtRamalTel').type(ramal_telefone)