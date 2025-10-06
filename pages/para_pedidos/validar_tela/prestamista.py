from playwright.sync_api import expect, Page

# Page Object para validação do serviço prestamista no fluxo do pedido.
class TicketPrestamista:
    def __init__(self, page: Page):
        self.page = page

    # Valida adição do serviço prestamista após clicar para adicionar.
    def adicionado(self):
        servicos_item = self.page.locator('[ng-repeat="itemAtual in item.servicos track by $index"] > ul')
        servicos_item.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(servicos_item).to_be_visible()
        nome_servico = self.page.locator('ul > :nth-child(1) > .ng-binding')
        expect(nome_servico).to_be_visible()
        cifrao_servico = self.page.locator('ul > :nth-child(1) > sup')
        expect(cifrao_servico).to_be_visible()
        expect(cifrao_servico).to_have_text('R$')
        vendedor_label = self.page.locator(':nth-child(2) > b')
        expect(vendedor_label).to_be_visible()
        expect(vendedor_label).to_have_text('Vendedor:')
        nome_vendedor = self.page.locator('[ng-repeat="itemAtual in item.servicos track by $index"] > ul > :nth-child(2)')
        expect(nome_vendedor).to_be_visible()
        icone_lapis = self.page.locator('ul > :nth-child(2) > .md-primary')
        expect(icone_lapis).to_be_visible()
        expect(icone_lapis).not_to_be_disabled()

    # Valida adição do prestamista na página de finalizar o pedido.
    def pagina_final(self):
        ng_scope_item = self.page.locator('.ng-scope > ul')
        ng_scope_item.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(ng_scope_item).to_be_visible()
        nome_servico = self.page.locator('ul > :nth-child(1) > .ng-binding')
        expect(nome_servico).to_be_visible()
        cifrao_servico = self.page.locator('ul > :nth-child(1) > sup')
        expect(cifrao_servico).to_be_visible()
        expect(cifrao_servico).to_have_text('R$')
        vendedor_label = self.page.locator('ul > :nth-child(2) > b')
        expect(vendedor_label).to_be_visible()
        expect(vendedor_label).to_have_text('Vendedor:')
        nome_vendedor = self.page.locator('.ng-scope > ul > :nth-child(2)')
        expect(nome_vendedor).to_be_visible()

    # Valida adição do serviço prestamista após agrupar lançamentos.
    def adicionado_receb_agrupado(self):
        prestamista_item = self.page.locator('b.ng-binding', has_text='T.A. Prestamista Não separa Com juros - Futuro')
        expect(prestamista_item).to_be_visible()