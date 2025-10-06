from playwright.sync_api import expect, Page

# Page Object para ações relacionadas a serviços no pedido.
class Service:
    def __init__(self, page: Page):
        self.page = page

    # ------------ ADICIONAR SERVIÇOS ------------

    # Marca garantia "T.A. Garantia Separa Mesmo Processo" - 139
    def garantia_sep_mesmo_proc(self):
        checkbox139 = self.page.locator('#checkbox-139-0 > .md-container')
        expect(checkbox139).not_to_be_disabled()
        checkbox139.click()

    # Marca garantia "T.A. Garantia Não Separa" - 140
    def garantia_nao_sep(self):
        checkbox140 = self.page.locator('#checkbox-140-1 > .md-container')
        expect(checkbox140).to_be_visible()
        expect(checkbox140).not_to_be_disabled()
        checkbox140.click()

    # Marca Garantia separa título em um processo diferente - 141
    def garantia_sep_titulo_proc_dif(self):
        checkbox141 = self.page.locator('#checkbox-141-2 > .md-container')
        expect(checkbox141).to_be_visible()
        expect(checkbox141).not_to_be_disabled()
        checkbox141.click()

    # Marca Mão de Obra "T.A. MO Destaca e Não Separa" - 142
    def mao_obra_dest_nao_sep(self):
        checkbox142 = self.page.locator('#checkbox-142-0 > .md-container')
        expect(checkbox142).to_be_visible()
        expect(checkbox142).not_to_be_disabled()
        checkbox142.click()

    # Marca Mão de Obra "T.A. MO Não Destaca e Separa Mesmo Processo" - 143
    def mao_obra_nao_dest_sep_mesmo_proc(self):
        checkbox143 = self.page.locator('#checkbox-143-1 > .md-container')
        expect(checkbox143).to_be_visible()
        expect(checkbox143).not_to_be_disabled()
        checkbox143.click()

    # Marca Mão de obra que não destaca e separa título em processo diferente - 144
    def mao_obra_nao_dest_sepa_proc_dif(self):
        checkbox144 = self.page.locator('#checkbox-144-2 > .md-container')
        expect(checkbox144).not_to_be_disabled()
        checkbox144.click()

    # ------------ SERVIÇOS VINCULADOS / MODAIS ------------

    # Valida modal de serviços vinculados.
    def validate_modal_serv_linked(self):
        titulo_modal = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_contain_text('Serviços Vinculados')

        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_be_disabled()

        icone_check_verde = self.page.locator('.icon')
        expect(icone_check_verde).to_be_visible()

        mensagem_adicionado_carrinho = self.page.locator('.ng-scope.flex-100 > .layout-wrap > :nth-child(2) > h2')
        expect(mensagem_adicionado_carrinho).to_be_visible()
        expect(mensagem_adicionado_carrinho).to_have_text('O item foi adicionado ao carrinho')

        mensagem_adicionar_servicos = self.page.locator('.ng-scope.flex-100 > .layout-wrap > :nth-child(2) > h4')
        expect(mensagem_adicionar_servicos).to_be_visible()
        expect(mensagem_adicionar_servicos).to_have_text('Aproveite para adicionar os serviços abaixo')

        mensagem_garantias = self.page.locator('p.ng-binding', has_text='Garantias')
        expect(mensagem_garantias).to_be_visible()

        mensagem_mao_de_obra = self.page.locator('p.ng-binding', has_text='Mão de Obra')
        mensagem_mao_de_obra.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(mensagem_mao_de_obra).to_be_visible()

    # Clica no botão OK do modal de serviços vinculados (com intercept).
    def click_ok_service_linked(self):
        self.page.route('POST', '/services/v3/pedido_calcular_frete', lambda route: route.continue_())
        api_pedido_calcular_frete = self.page.wait_for_response('/services/v3/pedido_calcular_frete')
        botao_salvar = self.page.locator('button[ng-click="salvar()"]')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).not_to_be_disabled()
        expect(botao_salvar).to_have_text(' Ok ')
        botao_salvar.click(force=True)
        api_pedido_calcular_frete

    # Clica no botão OK do modal de serviços vinculados de pedidos remotos.
    def click_ok_service_linked_remote(self):
        botao_salvar = self.page.locator('button[ng-click="salvar()"]')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).not_to_be_disabled()
        expect(botao_salvar).to_have_text(' Ok ')
        botao_salvar.click(force=True)

    # Valida modal e clica em OK para seguro prestamista.
    def ok_insurance_prest(self):
        titulo_modal_seguro = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_modal_seguro).to_be_visible()

        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_be_disabled()

        info_modal_seguro = self.page.locator('.white > .md-no-sticky > .md-subheader-inner')
        expect(info_modal_seguro).to_be_visible()

        checkbox_seguro = self.page.locator('.md-container')
        expect(checkbox_seguro).to_be_visible()
        expect(checkbox_seguro).not_to_be_disabled()

        cor_checkbox = self.page.locator('.md-container.md-ink-ripple')
        expect(cor_checkbox).to_have_css('color', 'rgba(37, 202, 19, 0.87)')

        nome_seguro = self.page.locator('.md-no-style > .md-list-item-text > :nth-child(1)')
        expect(nome_seguro).to_be_visible()

        quantidade = self.page.locator('.md-list-item-text > :nth-child(2)')
        expect(quantidade).to_be_visible()
        expect(quantidade).to_contain_text('Quantidade')

        valor_unitario = self.page.locator('.md-list-item-text > :nth-child(3)')
        expect(valor_unitario).to_be_visible()
        expect(valor_unitario).to_contain_text('Valor unitário')

        cifrao_valor = self.page.locator('.md-no-style > .md-secondary-container > :nth-child(1) > .ng-binding > sup')
        expect(cifrao_valor).to_be_visible()
        expect(cifrao_valor).to_contain_text('R$')

        valor = self.page.locator('.md-no-style > .md-secondary-container > :nth-child(1) > .ng-binding')
        expect(valor).to_be_visible()
        expect(valor).to_contain_text('R$')

        botao_ok = self.page.locator('md-dialog-actions.layout-row > .md-primary')
        expect(botao_ok).to_be_visible()
        expect(botao_ok).not_to_be_disabled()
        expect(botao_ok).to_have_text(' Ok ')
        botao_ok.click()

    # Valida mensagem de remoção do prestamista por agrupamento de formas de pagamento.
    def mess_prest_removed(self):
        toast = self.page.locator('.toast')
        expect(toast).to_be_visible()
        toast_title = self.page.locator('.toast-title')
        expect(toast_title).to_be_visible()
        expect(toast_title).to_have_text('Atenção')
        toast_message = self.page.locator('.toast-message')
        expect(toast_message).to_be_visible()
        expect(toast_message).to_have_text('O seguro prestamista será removido, você terá que adicioná-lo novamente')

    # Valida modal e clica para adicionar seguro prestamista.
    def add_insurance_prest(self):
        titulo_modal_seguro = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_modal_seguro).to_be_visible()

        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_be_disabled()

        info_modal_seguro = self.page.locator('.white > .md-no-sticky > .md-subheader-inner')
        expect(info_modal_seguro).to_be_visible()

        checkbox_seguro = self.page.locator('.md-container')
        expect(checkbox_seguro).to_be_visible()
        expect(checkbox_seguro).not_to_be_disabled()

        nome_seguro = self.page.locator('.md-no-style > .md-list-item-text > :nth-child(1)')
        expect(nome_seguro).to_be_visible()

        quantidade = self.page.locator('.md-list-item-text > :nth-child(2)')
        expect(quantidade).to_be_visible()
        expect(quantidade).to_contain_text('Quantidade')

        valor_unitario = self.page.locator('.md-list-item-text > :nth-child(3)')
        expect(valor_unitario).to_be_visible()
        expect(valor_unitario).to_contain_text('Valor unitário')

        cifrao_valor = self.page.locator('.md-no-style > .md-secondary-container > :nth