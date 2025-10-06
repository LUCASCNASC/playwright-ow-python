from playwright.sync_api import expect, Page

# Page Object para ações gerais em pedidos.
class GeneralOrder:
    def __init__(self, page: Page):
        self.page = page

    # Troca a filial de faturamento de local para remota.
    def change_branch_invoicing(self):
        filial_local = '50 - PR - EMISSÃO NFe/NFCe'
        filial_remota = '6 - GAZIN - IND. E COM. DE MÓVEIS E ELETROD. LTDA.'

        icone_filial_saldo = self.page.locator('[ng-click="openModalFilial(itemClicado.grade, false);"] > .ng-binding')
        expect(icone_filial_saldo).to_be_visible()

        botao_filial_faturamento = self.page.locator('[ng-click="openModalFilial(itemClicado.grade, false);"]')
        expect(botao_filial_faturamento).to_be_visible()
        expect(botao_filial_faturamento).to_contain_text(filial_local)
        botao_filial_faturamento.click(force=True)

        titulo_filial = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')
        expect(titulo_filial).to_be_visible()
        expect(titulo_filial).to_have_text('Filial')

        sair_card_filial = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(sair_card_filial).to_be_visible()

        filial50 = self.page.locator('p.ng-binding', has_text=filial_local)
        expect(filial50).to_be_visible()
        expect(filial50).not_to_be_disabled()

        filial6 = self.page.locator('p.ng-binding', has_text=filial_remota)
        expect(filial6).to_be_visible()
        expect(filial6).not_to_be_disabled()

        clicar_filial6 = self.page.locator('.white > md-list.md-default-theme > :nth-child(2) > div.md-button > .md-no-style')
        clicar_filial6.click()

    # Valida a composição do kit.
    def composition_kit(self):
        composicao_kit_titulo = self.page.locator('.is-expanded > v-pane-header.ng-scope > div')
        composicao_kit_titulo.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(composicao_kit_titulo).to_be_visible()
        expect(composicao_kit_titulo).to_contain_text('Composição deste KIT')

    # Clica no botão de editar parcelas da forma de pagamento.
    def click_edit_installments(self):
        icone_lapis_edicao = self.page.locator('.btn-remove-item-list > :nth-child(3) > .md-raised')
        icone_lapis_edicao.click(force=True)

    # Compara valores numéricos de Subtotal e Total Financeiro.
    def compare_subtotal_total_financial(self, span1_selector, span2_selector):
        locator1 = self.page.locator(span1_selector)
        locator2 = self.page.locator(span2_selector)

        def get_numeric_value(locator):
            text = locator.text_content()
            cleaned_text = ''.join([c for c in text if c.isdigit() or c in ',.'])
            return float(cleaned_text.replace(',', '.'))

        valor1_numerico = get_numeric_value(locator1)
        valor2_numerico = get_numeric_value(locator2)

        expect(valor1_numerico).to_be(valor2_numerico)