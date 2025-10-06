from playwright.sync_api import expect, Page

class CommandsGeneral:
    def __init__(self, page: Page):
        self.page = page

    # Faz login no sistema.
    def login(self):
        self.page.goto('/')
        self.page.fill('#txtusername', 'sabium.automacao')
        self.page.fill('#txtpassword', '123.automacao')
        self.page.route('**/images/icons/discount.svg', lambda route: route.continue_())
        api_discount_promise = self.page.wait_for_response('**/images/icons/discount.svg')
        self.page.click('.test_btnSalvarCliente')
        expect(self.page.locator('.ng-scope > .ng-binding')).to_contain_text('Entrando no sistema')
        api_discount_promise
        expect(self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header')).to_contain_text('Cliente')

    # Valida se a URL contém '/' após login.
    def url_apos_login(self):
        expect(self.page).to_have_url(r'/\/+/')

    # Valida o título da página.
    def titulo_pagina(self):
        expect(self.page).to_have_title('Sabium Mobile')

    # Seleciona um produto de busca e adiciona no carrinho.
    def select_product_search(self):
        self.page.route('**/services/v3/produto_tambem_compraram**', lambda route: route.continue_())
        api_produto_tambem_compraram_promise = self.page.wait_for_response('**/services/v3/produto_tambem_compraram**')
        expect(self.page.locator('.resultado-imagem')).to_be_visible()
        expect(self.page.locator('.md-resultado-titulo')).to_be_visible()
        expect(self.page.locator('.md-list-item-text > .ng-scope')).to_be_visible()
        expect(self.page.locator('.badge-saldo.ng-binding')).to_be_visible()
        expect(self.page.locator('sup')).to_be_visible()
        expect(self.page.locator('sup')).to_have_text('R$')
        expect(self.page.locator('.valor-busca')).to_be_visible()
        expect(self.page.locator('.md-list-item-text')).to_be_visible()
        self.page.locator('.md-list-item-text').click(force=True)
        api_produto_tambem_compraram_promise

    # Seleciona a voltagem do produto.
    def click_voltage_product(self):
        voltage_modal = self.page.locator('md-list.md-default-theme > .btn-rounded > .md-toolbar-tools > .flex')
        expect(voltage_modal).to_be_visible()
        expect(voltage_modal).to_have_text('Selecione a cor, a voltagem e o local de saldo')
        expand_button = self.page.locator('.layout-align-end-center > .md-fab')
        expect(expand_button).to_be_visible()
        expect(expand_button).not_to_be_disabled()
        voltage_card_symbol = self.page.locator('.md-secondary-container > div > .ng-binding > sup')
        expect(voltage_card_symbol).to_be_visible()
        expect(voltage_card_symbol).to_have_text('R$')
        voltage_card = self.page.locator('.md-list-item-inner')
        expect(voltage_card).to_be_visible()
        expect(voltage_card).to_contain_text('Cód. Fabricante:')
        expect(voltage_card).to_contain_text('Filial:')
        expect(voltage_card).to_contain_text('Saldo Local:')
        expect(voltage_card).to_contain_text('Saldo Depósito:')
        self.page.locator(':nth-child(1) > md-list.md-default-theme > .md-2-line > div.md-button > .md-no-style').click(force=True)
        self.page.route('**/services/v3/produto_relacionado_lista**', lambda route: route.continue_())
        self.page.wait_for_response('**/services/v3/produto_relacionado_lista**', timeout=40000)

    # Clica no botão adicionar produto após selecionar voltagem.
    def click_add_product(self):
        self.page.route('**/services/v3/produto_servico_vinculado**', lambda route: route.continue_())
        api_servicos_vinculados_promise = self.page.wait_for_response('**/services/v3/produto_servico_vinculado**')
        add_button = self.page.locator('[style="padding: 0px 5px;"] > .md-accent')
        add_button.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(add_button).to_be_visible()
        expect(add_button).not_to_be_disabled()
        expect(add_button).to_contain_text('Adicionar')
        add_button.click(force=True)
        api_servicos_vinculados_promise