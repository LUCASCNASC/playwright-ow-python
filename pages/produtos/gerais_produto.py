from playwright.sync_api import expect, Page

# Page Object para ações gerais com produtos.
class GeneralProduct:
    def __init__(self, page: Page):
        self.page = page

    # Seleciona o produto e adiciona ao pedido.
    def choose_product_search(self):
        self.page.route('**/services/v3/produto_tambem_compraram**', lambda route: route.fulfill())
        api_produto_tambem_compraram = self.page.wait_for_response('**/services/v3/produto_tambem_compraram**')
        expect(self.page.locator('.resultado-imagem')).to_be_visible()
        expect(self.page.locator('.md-resultado-titulo')).to_be_visible()
        expect(self.page.locator('.md-list-item-text > .ng-scope')).to_be_visible()
        expect(self.page.locator('.badge-saldo.ng-binding')).to_be_visible()
        cifrao = self.page.locator('sup')
        expect(cifrao).to_be_visible()
        expect(cifrao).to_have_text('R$')
        expect(self.page.locator('.valor-busca')).to_be_visible()
        adicionar_ao_carrinho = self.page.locator('.md-list-item-text')
        expect(adicionar_ao_carrinho).to_be_visible()
        adicionar_ao_carrinho.click(force=True)
        api_produto_tambem_compraram

    # Seleciona a voltagem do produto.
    def click_voltage_product(self):
        self.page.route('**/services/v3/produto_relacionado**', lambda route: route.fulfill())
        api_produto_relacionado_lista = self.page.wait_for_response('**/services/v3/produto_relacionado**')
        mensagem = self.page.locator('md-list.md-default-theme > .btn-rounded > .md-toolbar-tools > .flex')
        expect(mensagem).to_be_visible()
        expect(mensagem).to_have_text('Selecione a cor, a voltagem e o local de saldo')
        expand_btn = self.page.locator('.layout-align-end-center > .md-fab')
        expect(expand_btn).to_be_visible()
        expect(expand_btn).not_to_be_disabled()
        cifrao_card = self.page.locator('.md-secondary-container > div > .ng-binding > sup')
        expect(cifrao_card).to_be_visible()
        expect(cifrao_card).to_have_text('R$')
        card_voltagem = self.page.locator('.md-list-item-inner')
        expect(card_voltagem).to_be_visible()
        expect(card_voltagem).to_contain_text('Cód. Fabricante:')
        expect(card_voltagem).to_contain_text('Filial:')
        expect(card_voltagem).to_contain_text('Saldo Local:')
        expect(card_voltagem).to_contain_text('Saldo Depósito:')
        card_to_click = self.page.locator(':nth-child(1) > md-list.md-default-theme > .md-2-line > div.md-button > .md-no-style')
        card_to_click.click(force=True)
        api_produto_relacionado_lista

    # Clica no botão para adicionar produto após selecionar voltagem.
    def click_add_product(self):
        self.page.route('**/services/v3/produto_servico_vinculado**', lambda route: route.fulfill())
        api_servicos_vinculados = self.page.wait_for_response('**/services/v3/produto_servico_vinculado**')
        btn_add = self.page.locator('[style="padding: 0px 5px;"] > .md-accent')
        btn_add.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(btn_add).to_be_visible()
        expect(btn_add).not_to_be_disabled()
        expect(btn_add).to_contain_text('Adicionar')
        btn_add.click(force=True)
        api_servicos_vinculados