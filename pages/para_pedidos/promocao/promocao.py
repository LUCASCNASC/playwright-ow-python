from playwright.sync_api import expect, Page

# Page Object para ações e validações relacionadas a promoções.
class Promotion:
    def __init__(self, page: Page):
        self.page = page

    # Seleciona a primeira promoção do produto.
    def select_first_promo_product(self):
        botao_voltar = self.page.locator('[ng-click="modalSaldo()"] > .ng-binding')
        expect(botao_voltar).to_be_visible()
        expect(botao_voltar).not_to_be_disabled()

        titulo_promocoes = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_promocoes).to_be_visible()
        expect(titulo_promocoes).to_contain_text('Promoções')

        botao_x = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > [ng-click="cancel()"] > .ng-binding')
        expect(botao_x).to_be_visible()
        expect(botao_x).not_to_be_disabled()

        botao_nao_usar_promocao = self.page.locator('#dialogContent_137 > [style="padding: 0 5px"] > .md-primary')
        expect(botao_nao_usar_promocao).to_be_visible()
        expect(botao_nao_usar_promocao).not_to_be_disabled()

        promocao_sim = self.page.locator('.md-3-line > div.md-button > .md-no-style')
        expect(promocao_sim).to_be_visible()
        expect(promocao_sim).not_to_be_disabled()

        promocao_sim.click()

    # Valida produtos com ticket vermelho "PROMOÇÃO".
    def ticket_promotion(self):
        etiqueta_inteira = self.page.locator('.md-secondary-container > div > .ng-scope')
        expect(etiqueta_inteira).to_be_visible()
        expect(etiqueta_inteira).not_to_be_disabled()

        etiqueta_promocao = self.page.locator('span[ng-if="(gradeAtual.tempromocao)"]')
        expect(etiqueta_promocao).to_have_text('PROMOÇÃO')
        expect(etiqueta_promocao).to_be_visible()
        expect(etiqueta_promocao).to_have_css('background-color', 'rgb(255, 0, 0)')
        expect(etiqueta_promocao).to_have_css('color', 'rgb(255, 255, 255)')

    # Valida modal de carregamento "Adicionando produtos/serviços...".
    def mess_add_products_services(self):
        icone_carregamento = self.page.locator('.conteudo > .layout-align-center-center > .md-accent')
        expect(icone_carregamento).to_be_visible()

        mensagem_carregamento = self.page.locator('h3')
        expect(mensagem_carregamento).to_be_visible()
        expect(mensagem_carregamento).to_have_text('Adicionando produtos/serviços...')

    # Valida e prepara adição do serviço prestamista.
    def add_prestamista(self):
        icone_servico = self.page.locator('.btn-remove-item-list > :nth-child(2) > .md-raised > .ng-scope')
        expect(icone_servico).to_be_visible()
        expect(icone_servico).not_to_be_disabled()

        botao_servico = self.page.locator('.btn-remove-item-list > :nth-child(2) > .md-raised')
        expect(botao_servico).to_be_visible()
        expect(botao_servico).not_to_be_disabled()
        botao_servico.click(force=True)

        titulo_modal_seguro = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_modal_seguro).to_be_visible()
        expect(titulo_modal_seguro).to_have_text('Seguro prestamista')

        botao_x_modal_seguro = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_x_modal_seguro).to_be_visible()
        expect(botao_x_modal_seguro).not_to_be_disabled()

        subtitulo_modal_seguro = self.page.locator('.md-subheader-content')
        expect(subtitulo_modal_seguro).to_be_visible()
        expect(subtitulo_modal_seguro).to_contain_text('Seguro Prestamista')

        nome_seguro_prestamista = self.page.locator('.md-no-style > .md-list-item-text > :nth-child(1)')
        expect(nome_seguro_prestamista).to_be_visible()

        quantidade_seguro_prestamista = self.page.locator('.md-list-item-text > :nth-child(2)')
        expect(quantidade_seguro_prestamista).to_be_visible()
        expect(quantidade_seguro_prestamista).to_contain_text('Quantidade')

        valor_unitario_seguro_prestamista = self.page.locator('.md-list-item-text > :nth-child(3)')
        expect(valor_unitario_seguro_prestamista).to_be_visible()
        expect(valor_unitario_seguro_prestamista).to_contain_text('Valor unitário')

        valor_rs = self.page.locator('.md-no-style > .md-secondary-container > :nth-child(1) > .ng-binding > sup')
        expect(valor_rs).to_be_visible()
        expect(valor_rs).to_contain_text('R$')

        valor_seguro_prestamista = self.page.locator('.md-no-style > .md-secondary-container > :nth-child(1) > .ng-binding')
        expect(valor_seguro_prestamista).to_be_visible()

    # Valida tipo "Tipo(s) Serviço(s) Isento(s):" dentro do modal Promoções.
    def type_service_free_validate(self):
        tipo_servico_isento = self.page.locator('text=Tipo(s) Serviço(s) Isento(s):')
        expect(tipo_servico_isento).to_be_visible()
        garantias = self.page.locator('text=Garantias')
        expect(garantias).to_be_visible()