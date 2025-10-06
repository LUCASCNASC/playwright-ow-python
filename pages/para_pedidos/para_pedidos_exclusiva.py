from playwright.sync_api import expect, Page

# Page Object para operações exclusivas de pedidos.
class OrderExclusiva:
    def __init__(self, page: Page):
        self.page = page

    # Aumenta a quantidade a ser vendida para 5 unidades.
    def increase_amount_sale_five(self):
        btn_down = self.page.locator('[ng-click="delItem()"]')
        expect(btn_down).to_be_visible()
        expect(btn_down).not_to_be_disabled()

        campo_qtd = self.page.locator('[ng-model="quantidadeShow"]')
        expect(campo_qtd).to_be_visible()
        expect(campo_qtd).to_be_disabled()
        expect(campo_qtd).to_have_value('1')

        btn_up = self.page.locator('[ng-click="addItem()"]')
        expect(btn_up).to_be_visible()
        expect(btn_up).not_to_be_disabled()

        for _ in range(5):
            btn_up.click()

    # Aumenta a quantidade a ser vendida para 10 unidades.
    def increase_amount_sale_ten(self):
        btn_down = self.page.locator('[ng-click="delItem()"]')
        expect(btn_down).to_be_visible()
        expect(btn_down).not_to_be_disabled()

        campo_qtd = self.page.locator('[ng-model="quantidadeShow"]')
        expect(campo_qtd).to_be_visible()
        expect(campo_qtd).to_be_disabled()
        expect(campo_qtd).to_have_value('1')

        btn_up = self.page.locator('[ng-click="addItem()"]')
        expect(btn_up).to_be_visible()
        expect(btn_up).not_to_be_disabled()

        for _ in range(10):
            btn_up.click()

    # Valida produto remoto com saldo indisponível.
    def balance_remote_receive(self):
        imagem_resultado = self.page.locator('.resultado-imagem')
        expect(imagem_resultado).to_be_visible()

        saldo_disponivel = self.page.locator('.label')
        expect(saldo_disponivel).to_be_visible()
        expect(saldo_disponivel).to_have_text('Saldo disponivel')
        background_color = saldo_disponivel.evaluate('el => getComputedStyle(el).backgroundColor')
        expect(background_color).to_be('rgb(240, 173, 78)')

        nome_produto = self.page.locator('.md-resultado-titulo')
        expect(nome_produto).to_be_visible()

        codigo_produto = self.page.locator('.badge-saldo.ng-binding')
        expect(codigo_produto).to_be_visible()

        simbolo_rs = self.page.locator('sup')
        expect(simbolo_rs).to_be_visible()
        expect(simbolo_rs).to_have_text('R$')

        valor_produto = self.page.locator('.valor-busca')
        expect(valor_produto).to_be_visible()

        check_box = self.page.locator('.expandeIcone')
        expect(check_box).to_be_visible()