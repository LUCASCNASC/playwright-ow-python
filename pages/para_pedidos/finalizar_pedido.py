from playwright.sync_api import expect, Page

# Page Object para finalizar e validar pedidos.
class FinishOrder:
    def __init__(self, page: Page):
        self.page = page

    # Valida modal de proposta de crédito gerada.
    def validate_prop_credit_generated(self):
        titulo_pedido_concluido = self.page.locator(':nth-child(5) > .md-transition-in > ._md > .md-toolbar-tools > .flex')
        expect(titulo_pedido_concluido).to_be_visible()
        expect(titulo_pedido_concluido).to_contain_text('Análise de crédito')

        sair_da_aba = self.page.locator(':nth-child(5) > .md-transition-in > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(sair_da_aba).to_be_visible()
        expect(sair_da_aba).not_to_have_attribute('disabled')

        expect(self.page.locator('text=Deseja enviar a proposta #')).to_be_visible()
        expect(self.page.locator('text= para a análise de crédito?')).to_be_visible()

        botao_nao = self.page.locator(':nth-child(5) > .md-transition-in > .layout-align-center-center.layout-row > .md-accent')
        expect(botao_nao).to_be_visible()
        expect(botao_nao).to_have_text(' Não ')
        expect(botao_nao).not_to_have_attribute('disabled')

        botao_sim = self.page.locator(':nth-child(5) > .md-transition-in > .layout-align-center-center.layout-row > .md-primary')
        expect(botao_sim).to_be_visible()
        expect(botao_sim).to_have_text(' Sim ')
        expect(botao_sim).not_to_have_attribute('disabled')
        botao_sim.click(force=True)

    # Valida card de Pedido Concluído - alterado com sucesso.
    def validate_order_changed_sucess(self):
        titulo_pedido_concluido = self.page.locator('.md-toolbar-tools h2.flex')
        expect(titulo_pedido_concluido).to_be_visible()
        expect(titulo_pedido_concluido).to_contain_text('Pedido Concluído')

        sair_da_aba = self.page.locator('.md-content-overflow > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(sair_da_aba).to_be_visible()
        expect(sair_da_aba).not_to_have_attribute('disabled')

        icone_check = self.page.locator('.icon.success.animate')
        expect(icone_check).to_be_visible()
        icone_check_line = icone_check.locator('.line.tip.animateSuccessTip')
        expect(icone_check_line).to_be_visible()

        pedido_gerado = self.page.locator('.padding-10 > .layout-wrap > .flex-sm-50 > :nth-child(1)')
        expect(pedido_gerado).to_be_visible()
        expect(pedido_gerado).to_contain_text('Pedido gerado:')

        pedido_gravado_sucesso = self.page.locator('[ng-show="editarPedido"]')
        expect(pedido_gravado_sucesso).to_be_visible()
        expect(pedido_gravado_sucesso).to_contain_text('Pedido alterado com sucesso')

        numero_pedido_gravado_sucesso = self.page.locator('#pedido-numero')
        expect(numero_pedido_gravado_sucesso).to_be_visible()

        botao_imprimir = self.page.locator('md-dialog-actions.layout-align-center-center > .md-accent')
        expect(botao_imprimir).to_be_visible()
        expect(botao_imprimir).to_contain_text('Imprimir')
        expect(botao_imprimir).not_to_have_attribute('disabled')

        botao_ok = self.page.locator('md-dialog-actions.layout-align-center-center > .md-primary')
        expect(botao_ok).to_be_visible()
        expect(botao_ok).to_contain_text('Ok')
        expect(botao_ok).not_to_have_attribute('disabled')

    # Clica no botão para finalizar o pedido.
    def click_finish_order(self):
        self.page.route('POST', '/services/v3/pedido_finalizar', lambda route: route.continue_())
        api_pedido_finalizar = self.page.wait_for_response('/services/v3/pedido_finalizar')

        botao_finalizar_pedido = self.page.locator('button.md-primary.btn-rounded.md-raised.btn-block.md-default-theme.md-ink-ripple[type="button"][ng-click="confirmarPedido()"]')
        botao_finalizar_pedido.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(botao_finalizar_pedido).to_be_visible()
        expect(botao_finalizar_pedido).not_to_be_disabled()
        expect(botao_finalizar_pedido).to_have_text('Finalizar pedido')
        botao_finalizar_pedido.click(force=True)

        titulo_pedido_concluido = self.page.locator('.md-toolbar-tools h2.flex')
        expect(titulo_pedido_concluido).to_be_visible()
        expect(titulo_pedido_concluido).to_contain_text('Pedido Concluído')

        sair_da_aba = self.page.locator('.md-content-overflow > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(sair_da_aba).to_be_visible()
        expect(sair_da_aba).not_to_have_attribute('disabled')

        girando_carregar = self.page.locator('.layout-column > .md-accent')
        expect(girando_carregar).to_be_visible()

        mensagem_finalizando_pedido = self.page.locator('.layout-column > h4')
        expect(mensagem_finalizando_pedido).to_be_visible()
        expect(mensagem_finalizando_pedido).to_have_text('Finalizando pedido...')

        atencao_label = self.page.locator('.layout-column > p > span')
        expect(atencao_label).to_be_visible()
        expect(atencao_label).to_have_text('ATENÇÃO:')
        expect(atencao_label).to_have_css('color', 'rgb(204, 0, 0)')

        mensagem_nao_atualize = self.page.locator('.layout-column > p')
        expect(mensagem_nao_atualize).to_be_visible()
        expect(mensagem_nao_atualize).to_contain_text('Não atualize a página enquanto o pedido estiver sendo finalizado.')
        expect(mensagem_nao_atualize).to_have_css('color', 'rgb(204, 0, 0)')

        api_pedido_finalizar

    # Valida card de Pedido Concluído - gravado com sucesso.
    def validate_order_generated(self):
        titulo_pedido_concluido = self.page.locator('.md-toolbar-tools h2.flex')
        expect(titulo_pedido_concluido).to_be_visible()
        expect(titulo_pedido_concluido).to_contain_text('Pedido Concluído')

        sair_da_aba = self.page.locator('.md-content-overflow > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(sair_da_aba).to_be_visible()
        expect(sair_da_aba).not_to_have_attribute('disabled')

        icone_check = self.page.locator('.icon.success.animate')
        expect(icone_check).to_be_visible()
        icone_check_line = icone_check.locator('.line.tip.animateSuccessTip')
        expect(icone_check_line).to_be_visible()

        pedido_gerado = self.page.locator('.padding-10 > .layout-wrap > .flex-sm-50 > :nth-child(1)')
        expect(pedido_gerado).to_be_visible()
        expect(pedido_ger