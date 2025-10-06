from playwright.sync_api import expect, Page

# Page Object para validações e interações do menu de opções.
class MenuOpcoes:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar no menu de opções.
    def icone_menu_opcoes(self):
        menu_opcoes_icone = self.page.locator('[aria-label="Menu de opções"] > .ng-binding')
        expect(menu_opcoes_icone).to_be_visible()
        expect(menu_opcoes_icone).not_to_have_attribute('disabled')
        menu_opcoes_icone.click(force=True)

    # Validando topo da página - parte colorida.
    def topo_pagina(self):
        return self.icone_menu_opcoes()

    # Validar imagem no início do modal menu.
    def image_menu(self):
        imagem_modal_menu = self.page.locator('.md-primary > .logo > .md-default-theme > img')
        expect(imagem_modal_menu).to_be_visible()
        expect(imagem_modal_menu).not_to_have_attribute('disabled')

    # Ícone do computador para validar se realmente saiu do pedido web.
    def icone_computador_login(self):
        icone_computador = self.page.locator('[ng-click="clienteStatsOpen()"] > .ng-binding')
        expect(icone_computador).to_be_visible()
        expect(icone_computador).not_to_have_attribute('disabled')
        campo_buscar_produto = self.page.locator('#searchText')
        expect(campo_buscar_produto).to_be_visible()
        expect(campo_buscar_produto).not_to_be_disabled()
        label_buscar_produto = self.page.locator('label[for="searchText"]')
        expect(label_buscar_produto).to_have_text('Buscar produtos')

    # Validando opção Início, do menu de opções.
    def inicio_opcao_menu(self):
        icone_inicio = self.page.locator('md-icon[md-svg-src="images/icons/home.svg"]')
        icone_inicio.scroll_into_view_if_needed()
        self.page.wait_for_timeout(300)
        expect(icone_inicio).to_be_visible()
        opcao_inicio_menu = self.page.locator('a[aria-label="Início"]')
        expect(opcao_inicio_menu).to_be_visible()
        expect(opcao_inicio_menu).not_to_have_attribute('disabled')
        expect(opcao_inicio_menu).to_have_attribute('aria-label', 'Início')
        opcao_inicio_menu.click(force=True)

    # Validando opção Departamentos, do menu de opções.
    def departamento_opcao_menu(self):
        icone_departamentos = self.page.locator('md-icon[md-svg-src="images/icons/departamentos.svg"]')
        icone_departamentos.scroll_into_view_if_needed()
        expect(icone_departamentos).to_be_visible()
        opcao_departamentos_menu = self.page.locator('a[aria-label="Departamentos"]')
        expect(opcao_departamentos_menu).to_be_visible()
        expect(opcao_departamentos_menu).not_to_have_attribute('disabled')
        expect(opcao_departamentos_menu).to_have_attribute('aria-label', 'Departamentos')
        opcao_departamentos_menu.click(force=True)
        breadcrumb_departamentos = self.page.locator('.breadcrumbDepartamentos')
        expect(breadcrumb_departamentos).to_be_visible()
        expect(breadcrumb_departamentos).to_contain_text('Departamentos')

    # Validando opção Serviços, do menu de opções.
    def servicos_opcao_menu(self):
        icone_servicos = self.page.locator('md-icon[md-svg-src="images/icons/services.svg"]')
        icone_servicos.scroll_into_view_if_needed()
        expect(icone_servicos).to_be_visible()
        opcao_servicos_menu = self.page.locator('a[aria-label="Serviços"]')
        expect(opcao_servicos_menu).to_be_visible()
        expect(opcao_servicos_menu).not_to_have_attribute('disabled')
        expect(opcao_servicos_menu).to_have_attribute('aria-label', 'Serviços')
        opcao_servicos_menu.click(force=True)
        ordenar_servicos = self.page.locator('[ng-click="alterarOrdenacaoPorDescricao()"]')
        expect(ordenar_servicos).to_be_visible()
        expect(ordenar_servicos).not_to_have_attribute('disabled')

    # Validando opção Pedidos Pendentes, do menu de opções.
    def pedidos_pendentes_opcao_menu(self):
        icone_pedidos_pendentes = self.page.locator('md-icon[md-svg-src="images/icons/pedido.svg"]')
        icone_pedidos_pendentes.scroll_into_view_if_needed()
        expect(icone_pedidos_pendentes).to_be_visible()
        opcao_pedidos_pendentes_menu = self.page.locator('a[aria-label="Pedidos pendentes"]')
        expect(opcao_pedidos_pendentes_menu).to_be_visible()
        expect(opcao_pedidos_pendentes_menu).not_to_have_attribute('disabled')
        expect(opcao_pedidos_pendentes_menu).to_have_attribute('aria-label', 'Pedidos pendentes')
        opcao_pedidos_pendentes_menu.click(force=True)
        header_pedidos_pendentes = self.page.locator('.header')
        expect(header_pedidos_pendentes).to_be_visible()
        expect(header_pedidos_pendentes).to_contain_text('PEDIDOS PENDENTES')

    # Validando opção Cliente, do menu de opções.
    def cliente_opcao_menu(self):
        icone_cliente = self.page.locator('md-icon[md-svg-src="images/icons/cliente.svg"]')
        icone_cliente.scroll_into_view_if_needed()
        expect(icone_cliente).to_be_visible()
        opcao_cliente_menu = self.page.locator('a[aria-label="Cliente"]')
        expect(opcao_cliente_menu).to_be_visible()
        expect(opcao_cliente_menu).not_to_have_attribute('disabled')
        expect(opcao_cliente_menu).to_have_attribute('aria-label', 'Cliente')
        opcao_cliente_menu.click(force=True)
        cliente_page_element = self.page.locator('.md-default')
        expect(cliente_page_element).to_be_visible()
        expect(cliente_page_element).not_to_have_attribute('disabled')

    # Validando opção Cliente Completo, do menu de opções.
    def cliente_completo_opcao_menu(self):
        icone_cliente_completo = self.page.locator('md-icon[md-svg-src="images/icons/cliente_completo.svg"]')
        icone_cliente_completo.scroll_into_view_if_needed()
        expect(icone_cliente_completo).to_be_visible()
        opcao_cliente_completo_menu = self.page.locator('a[aria-label="Cliente completo"]')
        expect(opcao_cliente_completo_menu).to_be_visible()
        expect(opcao_cliente_completo_menu).not_to_have_attribute('disabled')
        expect(opcao_cliente_completo_menu).to_have_attribute('aria-label', 'Cliente completo')
        opcao_cliente_completo_menu.click(force=True)
        menu_cliente_completo = self.page.locator('#menu_items_pri > .on')
        expect(menu_cliente_completo).to_be_visible()
        expect(menu_cliente_completo).not_to_have_attribute('disabled')

    # Validando opção Pós Venda, do menu de opções.
    def pos_venda_opcao_menu(self):
        icone_pos_venda = self.page.locator('md-icon[md-svg-src="images/icons/pos-venda.svg"]')
        icone_pos_venda.scroll_into_view_if_needed()
        expect(icone_pos_venda).to_be_visible()
        opcao_pos_venda_menu = self.page.locator('a[aria-label="Pós-venda"]')
        expect(opcao_pos_venda_menu).to_be_visible()
        expect(opcao_pos_venda_menu).not_to_have_attribute('disabled')
        expect(opcao_pos_venda_menu).to_have_attribute('aria-label', 'Pós-venda')
        opcao_pos_venda_menu.click(force=True)
        header_pos_venda = self.page.locator('.header')
        expect(header_pos_venda).to_be_visible()

    # Validando opção Intenção de compra, do menu de opções.
    def intencao_compra_opcao_menu(self):
        icone_intencao_compra = self.page.locator('md-icon[md-svg-src="images/icons/intencao.svg"]')
        icone_intencao_compra.scroll_into_view_if_needed()
        expect(icone_intencao_compra).to_be_visible()
        opcao_intencao_compra_menu = self.page.locator('button[aria-label="Intenção de compra"]')
        expect(opcao_intencao_compra_menu).to_be_visible()
        expect(opcao_intencao_compra_menu).not_to_have_attribute('disabled')
        expect(opcao_intencao_compra_menu).to_have_attribute('aria-label', 'Intenção de compra')
        opcao_intencao_compra_menu.click(force=True)
        header_intencao_compra = self.page.locator('.header')
        expect(header_intencao_compra).to_be_visible()

    # Validando opção Proposta de crédito, do menu de opções.
    def proposta_credito_opcao_menu(self):
        icone_proposta_credito = self.page.locator('md-icon[md-svg-src="images/icons/aprovacao_credito.svg"]')
        icone_proposta_credito.scroll_into_view_if_needed()
        expect(icone_proposta_credito).to_be_visible()
        opcao_proposta_credito_menu = self.page.locator('a[aria-label="Proposta de crédito"]')
        expect(opcao_proposta_credito_menu).to_be_visible()
        expect(opcao_proposta_credito_menu).not_to_have_attribute('disabled')
        expect(opcao_proposta_credito_menu).to_have_attribute('aria-label', 'Proposta de crédito')
        opcao_proposta_credito_menu.click(force=True)
        header_proposta_credito = self.page.locator('.header')
        expect(header_proposta_credito).to_be_visible()

    # Validando opção Configurações, do menu de opções.
    def configuracoes_opcao_menu(self):
        icone_configuracoes = self.page.locator('md-icon[md-svg-src="images/icons/settings.svg"]')
        icone_configuracoes.scroll_into_view_if_needed()
        expect(icone_configuracoes).to_be_visible()
        opcao_configuracoes_menu = self.page.locator('a[aria-label="Configurações"]')
        expect(opcao_configuracoes_menu).to_be_visible()
        expect(opcao_configuracoes_menu).not_to_have_attribute('disabled')
        expect(opcao_configuracoes_menu).to_have_attribute('aria-label', 'Configurações')
        opcao_configuracoes_menu.click(force=True)
        view_configuracoes = self.page.locator('ui-view.ng-scope > :nth-child(2)')
        expect(view_configuracoes).to_be_visible()

    # Validando opção Minha performance, do menu de opções.
    def minha_performance_opcao_menu(self):
        icone_minha_performance = self.page.locator('md-icon[md-svg-src="images/icons/performance.svg"]')
        icone_minha_performance.scroll_into_view_if_needed()
        expect(icone_minha_performance).to_be_visible()
        opcao_minha_performance_menu = self.page.locator('a[aria-label="Minha performance"]')
        expect(opcao_minha_performance_menu).to_be_visible()
        expect(opcao_minha_performance_menu).not_to_have_attribute('disabled')
        expect(opcao_minha_performance_menu).to_have_attribute('aria-label', 'Minha performance')
        opcao_minha_performance_menu.click(force=True)
        header_minha_performance = self.page.locator('.header')
        expect(header_minha_performance).to_be_visible()

    # Validando opção Sair, já fora do menu de opções.
    def botao_sair(self):
        opcao_minha_performance = self.page.locator('.rodape > ._md-button-wrap > div.md-button > .md-no-style')
        expect(opcao_minha_performance).to_be_visible()
        expect(opcao_minha_performance).not_to_have_attribute('disabled')
        expect(opcao_minha_performance).to_have_attribute('aria-label', 'Sair')
        opcao_minha_performance.click(force=True)