from playwright.sync_api import expect, Page

# Page Object para validações de saldo de produto (local, CD, indisponível).
class ValidateBalance:
    def __init__(self, page: Page):
        self.page = page

    # Valida produto com saldo disponível local (verde).
    def with_balance(self):
        resultado_imagem = self.page.locator('.resultado-imagem')
        expect(resultado_imagem).to_be_visible()

        saldo_disponivel = self.page.locator('.label')
        expect(saldo_disponivel).to_be_visible()
        expect(saldo_disponivel).to_have_text('Saldo disponivel')
        color = saldo_disponivel.evaluate('node => getComputedStyle(node).backgroundColor')
        expect(color).to_be('rgb(92, 184, 92)')

        nome_produto = self.page.locator('.md-resultado-titulo')
        expect(nome_produto).to_be_visible()

        codigo_produto = self.page.locator('.badge-saldo.ng-binding')
        expect(codigo_produto).to_be_visible()

        rs_card = self.page.locator('sup')
        expect(rs_card).to_be_visible()
        expect(rs_card).to_have_text('R$')

        valor_produto = self.page.locator('.valor-busca')
        expect(valor_produto).to_be_visible()

    # Valida produto com saldo disponível no CD (amarelo).
    def with_balance_cd(self):
        resultado_imagem = self.page.locator('.resultado-imagem')
        expect(resultado_imagem).to_be_visible()

        saldo_disponivel = self.page.locator('.label')
        expect(saldo_disponivel).to_be_visible()
        expect(saldo_disponivel).to_have_text('Saldo disponivel')
        color = saldo_disponivel.evaluate('node => getComputedStyle(node).backgroundColor')
        expect(color).to_be('rgb(240, 173, 78)')

        nome_produto = self.page.locator('.md-resultado-titulo')
        expect(nome_produto).to_be_visible()

        codigo_produto = self.page.locator('.badge-saldo.ng-binding')
        expect(codigo_produto).to_be_visible()

        rs_card = self.page.locator('sup')
        expect(rs_card).to_be_visible()
        expect(rs_card).to_have_text('R$')

        valor_produto = self.page.locator('.valor-busca')
        expect(valor_produto).to_be_visible()

    # Valida produto com saldo indisponível (vermelho).
    def without_balance(self):
        resultado_imagem = self.page.locator('.resultado-imagem')
        expect(resultado_imagem).to_be_visible()

        saldo_indisponivel = self.page.locator('.label')
        expect(saldo_indisponivel).to_be_visible()
        expect(saldo_indisponivel).to_have_text('Saldo indisponivel')
        color = saldo_indisponivel.evaluate('node => getComputedStyle(node).backgroundColor')
        expect(color).to_be('rgb(217, 83, 79)')

        nome_produto = self.page.locator('.md-resultado-titulo')
        expect(nome_produto).to_be_visible()

        codigo_produto = self.page.locator('.badge-saldo.ng-binding')
        expect(codigo_produto).to_be_visible()

        rs_card = self.page.locator('sup')
        expect(rs_card).to_be_visible()
        expect(rs_card).to_have_text('R$')

        valor_produto = self.page.locator('.valor-busca')
        expect(valor_produto).to_be_visible()