from playwright.sync_api import expect, Page

# Page Object para ações de agrupamento de recebimento (lançamentos financeiros).
class GroupReceipt:
    def __init__(self, page: Page):
        self.page = page

    # Clica para NÃO agrupar lançamentos com o mesmo processo de recebimento.
    def not_group_releases(self):
        expect(self.page.locator('.md-title')).to_be_visible()
        expect(self.page.locator('.md-title')).to_have_text('Identificamos que já existe um pagamento lançado com esta mesma forma escolhida')
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_have_text('Deseja agrupar este pagamento em um único pagamento?')

        confirm_button = self.page.locator('.md-confirm-button')
        expect(confirm_button).to_be_visible()
        expect(confirm_button).to_have_text('Sim, desejo agrupar este pagamento')
        expect(confirm_button).not_to_be_disabled()
        confirm_button_color = confirm_button.evaluate('el => getComputedStyle(el).color')
        expect(confirm_button_color).to_be('rgb(36, 13, 105)')

        cancel_button = self.page.locator('.md-cancel-button')
        expect(cancel_button).to_be_visible()
        expect(cancel_button).to_have_text('Não, desejo mantê-los individuais')
        expect(cancel_button).not_to_be_disabled()
        cancel_button_color = cancel_button.evaluate('el => getComputedStyle(el).color')
        expect(cancel_button_color).to_be('rgb(36, 13, 105)')

        cancel_button.click()

    # Clica para SIM, agrupar lançamentos com o mesmo processo de recebimento.
    def group_releases(self):
        expect(self.page.locator('.md-title')).to_be_visible()
        expect(self.page.locator('.md-title')).to_have_text('Identificamos que já existe um pagamento lançado com esta mesma forma escolhida')
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_have_text('Deseja agrupar este pagamento em um único pagamento?')

        confirm_button = self.page.locator('.md-confirm-button')
        expect(confirm_button).to_be_visible()
        expect(confirm_button).to_have_text('Sim, desejo agrupar este pagamento')
        expect(confirm_button).not_to_be_disabled()

        cancel_button = self.page.locator('.md-cancel-button')
        expect(cancel_button).to_be_visible()
        expect(cancel_button).to_have_text('Não, desejo mantê-los individuais')
        expect(cancel_button).not_to_be_disabled()

        confirm_button.click()

    # Seleciona dois lançamentos com o mesmo processo de recebimento para clicar no botão AGRUPAR.
    def select_releases_group(self):
        # Primeiro lançamento
        expect(self.page.locator('[ng-show="parcelamentoAutomaticoDisponivel"] > .md-subheader-inner > .md-subheader-content')).to_be_visible()
        expect(self.page.locator('[ng-show="parcelamentoAutomaticoDisponivel"] > .md-subheader-inner > .md-subheader-content')).to_have_text('Lançamentos já realizados')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(2) > span.ng-binding > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(2) > span.ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding > b')).to_have_text('1º Vencimento:')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding > b')).to_have_text('Valor sem juros:')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding > b')).to_have_text('Valor da Parcela:')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding > b')).to_have_text('Subtotal:')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > b')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > b')).to_have_text('Agrupar')
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container')).not_to_be_disabled()
        self.page.locator(':nth-child(1) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container').click()

        # Segundo lançamento
        expect(self.page.locator('[ng-show="parcelamentoAutomaticoDisponivel"] > .md-subheader-inner > .md-subheader-content')).to_be_visible()
        expect(self.page.locator('[ng-show="parcelamentoAutomaticoDisponivel"] > .md-subheader-inner > .md-subheader-content')).to_have_text('Lançamentos já realizados')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(2) > span.ng-binding > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(2) > span.ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding > b')).to_have_text('1º Vencimento:')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(3) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding > b')).to_have_text('Valor sem juros:')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(5) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding > b')).to_have_text('Valor da Parcela:')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(6) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding > b')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding > b')).to_have_text('Subtotal:')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > :nth-child(7) > .ng-binding')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > b')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > b')).to_have_text('Agrupar')
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container')).not_to_be_disabled()
        self.page.locator(':nth-child(2) > .md-whiteframe-2dp > .layout-gt-sm-row > [ng-show="item.opcaoAgrupar && item.permiteAgrupar"] > span > .md-auto-horizontal-margin > .md-container').click()

    # Clica no botão AGRUPAR.
    def click_group(self):
        agrupar_button = self.page.locator('.layout-align-center-end > .flex-gt-sm-50 > .md-primary')
        expect(agrupar_button).to_be_visible()
        expect(agrupar_button).to_have_text('Agrupar')
        agrupar_button.click()

    # Coloca o valor da primeira forma de pagamento no campo "valor a parcelar".
    def first_value_installment(self):
        expect(self.page.locator('label', has_text='Valor a parcelar')).to_be_visible()
        valor_aparcelar_input = self.page.locator('.campoMoeda_valorAparcelar')
        valor_aparcelar_input.clear()
        self.page.wait_for_timeout(200)
        valor_aparcelar_input.type('40000')