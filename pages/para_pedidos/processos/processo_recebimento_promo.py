from playwright.sync_api import expect, Page

# Page Object para seleção de formas de pagamento em promoções.
class ReceiptPromotion:
    def __init__(self, page: Page):
        self.page = page

    # Promoções para arquivos apenas de promoção e promoção serviço
    def pag_principal(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3860 - T.A. A Receber Futuro   Futuro"]')
        forma_pagamento_promocao.click()

    def receber_prest(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3866 - T.A. A Receber Prestamista   Futuro"]')
        forma_pagamento_promocao.click()

    # Promoções para arquivos apenas de promoção com prestamista

    # Abatimento Valor Fixo 55,90 - processo de inclusão PROMOÇÃO
    def term_fut_with_fees_prest_abat_vf(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3880 - T.A. A Receb Fut com juros - Prest. Valor Fixo   Futuro"]')
        forma_pagamento_promocao.click()

    # Abatimento % - processo de inclusão PROMOÇÃO
    def term_fut_with_fees_prest(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3874 - T.A. A Receber Futuro - para Prestamista   Futuro"]')
        forma_pagamento_promocao.click()

    def term_fut_without_fees_prest(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3876 - T.A. A Receber Futuro - para Prestamista sem juros   Futuro"]')
        forma_pagamento_promocao.click()

    def entry_present_prest(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3875 - T.A.A Receber Presente CDCI - para Prestamista   Presente"]')
        forma_pagamento_promocao.click()

    # Abatimento Valor Fixo 99,30 - Origem Produto - processo de inclusão PROMOÇÃO
    def term_fut_with_fees_prest_abat_vf_os(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3881 - T.A. A Receb Fut com juros - Prest. Origem Produto   Futuro"]')
        forma_pagamento_promocao.click()

    def term_present_with_fees_prest_abat_vf_os(self):
        botao_voltar = self.page.locator('.md-toolbar-tools > [ng-click="modalPromocao()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_modal = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Formas de pagamento')

        botao_x = self.page.locator('#modal-formaPagamento > .md-dialog-fullscreen > .md-primary > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        forma_pagamento_promocao = self.page.locator('button[aria-label="3882 - T.A. A Receb Presen com juros - Prest. Origem Prd   Presente"]')
        forma_pagamento_promocao.click()