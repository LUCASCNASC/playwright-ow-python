from playwright.sync_api import expect, Page

# Page Object para ações de desconto no pedido (Playwright).
class OrderExclusiva:
    def __init__(self, page: Page):
        self.page = page

    # Valida e clica no botão de desconto (%).
    def clicar_botao_desconto(self):
        desconto_btn = self.page.locator('[ng-click="abrirModalDescontoProduto($index)"]')
        desconto_btn.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(desconto_btn).to_be_visible()
        expect(desconto_btn).not_to_be_disabled()

        desconto_icon = self.page.locator('[ng-click="abrirModalDescontoProduto($index)"] > .ng-scope')
        desconto_icon.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(desconto_icon).to_be_visible()
        expect(desconto_icon).not_to_be_disabled()
        desconto_icon.click(force=True)

    # Valida o modal Sub/Sobre e opções de desconto.
    def validate_modal_sub(self):
        titulo_sub_sobre = self.page.locator('.md-transition-in > ._md > .md-toolbar-tools > .flex')
        expect(titulo_sub_sobre).to_be_visible()
        expect(titulo_sub_sobre).to_have_text('Sub/Sobre')

        botao_x = self.page.locator('.md-transition-in > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        botao_arrasta = self.page.locator('.md-primary > .md-container > .md-bar')
        expect(botao_arrasta).to_be_visible()
        expect(botao_arrasta).not_to_be_disabled()

        expect(self.page.locator('text=Sub (-)')).to_be_visible()
        expect(self.page.locator('text=(+) Sobre')).to_be_visible()

        expect(self.page.locator('button:has-text("R$")')).to_be_visible()
        expect(self.page.locator('button:has-text("R$")')).not_to_be_disabled()

        expect(self.page.locator('button:has-text("%")')).to_be_visible()
        expect(self.page.locator('button:has-text("%")')).not_to_be_disabled()

        expect(self.page.locator('button:has-text("VALOR FIXO")')).to_be_visible()
        expect(self.page.locator('button:has-text("VALOR FIXO")')).not_to_be_disabled()

        expect(self.page.locator('md-icon')).to_be_visible()

        campo_desconto = self.page.locator('input.campoMoeda_desconto.md-input')
        expect(campo_desconto).to_be_visible()
        expect(campo_desconto).to_have_value('0')

        botao_aplicar = self.page.locator('button[ng-click="aplicarSubSobre()"]')
        expect(botao_aplicar).to_be_visible()
        expect(botao_aplicar).to_contain_text('Aplicar')
        expect(botao_aplicar).not_to_be_disabled()

    # Arrasta a forma de pagamento escolhida para aparecer desconto.
    def drag_form_payment(self):
        drag_target = self.page.locator('.md-whiteframe-2dp')
        drag_target.dispatch_event('mousedown', button=0)
        drag_target.dispatch_event('mousemove', clientX=100, clientY=0)
        drag_target.dispatch_event('mouseup')

    # Clica no botão R$ para desconto.
    def click_change_value(self):
        botao_completo = self.page.locator('.btn-remove-item-list > :nth-child(1) > .md-raised')
        expect(botao_completo).to_be_visible()
        expect(botao_completo).not_to_be_disabled()

        icone_dentro_botao = self.page.locator('.btn-remove-item-list > :nth-child(1) > .md-raised > .ng-scope')
        expect(icone_dentro_botao).to_be_visible()
        expect(icone_dentro_botao).not_to_be_disabled()
        icone_dentro_botao.click(force=True)

    # Valida o modal de alteração de valor.
    def modal_change_value(self):
        titulo_alterar_valor = self.page.locator('.md-transition-in > ._md > .md-toolbar-tools > .flex')
        expect(titulo_alterar_valor).to_be_visible()
        expect(titulo_alterar_valor).to_have_text('Alterar o valor')

        botao_x = self.page.locator('.md-transition-in > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        expect(self.page.locator('text=Valor da parcela')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoValor"]')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoValor"]')).to_be_enabled()

        expect(self.page.locator('text=Numero de parcelas')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoQtdVezes"]')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoQtdVezes"]')).to_be_disabled()

        expect(self.page.locator('text=Subtotal')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoSubtotal"]')).to_be_visible()
        expect(self.page.locator('[ng-model="formaPgtoSubtotal"]')).to_be_enabled()

        botao_aplicar = self.page.locator('button.md-raised.md-primary')
        expect(botao_aplicar).to_be_visible()
        expect(botao_aplicar).to_contain_text(' Aplicar ')

    # Altera valor para baixo (por exemplo: 136000).
    def change_value_to_low(self):
        campo_valor_parcela = self.page.locator('[ng-model="formaPgtoValor"]')
        campo_valor_parcela.fill('')
        self.page.wait_for_timeout(200)
        campo_valor_parcela.type('136000')

        campo_subtotal = self.page.locator('[ng-model="formaPgtoSubtotal"]')
        campo_subtotal.fill('')
        self.page.wait_for_timeout(200)
        campo_subtotal.type('136000')

        self.page.locator('button[ng-click="aplicarAlterarValor()"]').click(force=True)

    # Altera valor para cima (por exemplo: 137000).
    def change_value_to_top(self):
        campo_valor_parcela = self.page.locator('[ng-model="formaPgtoValor"]')
        campo_valor_parcela.fill('')
        self.page.wait_for_timeout(200)
        campo_valor_parcela.type('137000')

        campo_subtotal = self.page.locator('[ng-model="formaPgtoSubtotal"]')
        campo_subtotal.fill('')
        self.page.wait_for_timeout(200)
        campo_subtotal.type('137000')

        self.page.locator('button[ng-click="aplicarAlterarValor()"]').click(force=True)

    # Aplica desconto Sub(-) com R$.
    def apply_discount_rs(self):
        valor_desconto_rs = '1000'
        self.page.locator('button:has-text("R$")').click(force=True)
        self.page.locator('#txtReajusteReal_0').type(valor_desconto_rs)
        self.page.locator('button[ng-click="aplicarSubSobre()"]').click(force=True)

    # Aplica desconto Sub(-) com %.
    def apply_discount_percentage(self):
        valor_desconto_porcentagem = '2'
        self.page.locator('button:has-text("%")').click(force=True)
        self.page.locator('#txtReajustePorc_0').type(valor_desconto_porcentagem)
        self.page.locator('button[ng-click="aplicarSubSobre()"]').click(force=True)

    # Aplica desconto Sub(-) com VALOR FIXO.
    def apply_discount_vf(self):
        valor_desconto_valor_fixo = '280000'
        self.page.locator('button:has-text("VALOR FIXO")').click(force=True)
        campo_valor_desconto = self.page.locator('#txtReajusteFixo_0')
        campo_valor_desconto.fill('')
        self.page.wait_for_timeout(100)
        campo_valor_desconto.type(valor_desconto_valor_fixo)
        self.page.locator('button[ng-click="aplicarSubSobre()"]').click(force=True)