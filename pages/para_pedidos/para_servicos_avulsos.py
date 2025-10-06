from playwright.sync_api import expect, Page

# Page Object para operações de serviços avulsos no pedido.
class OrderServiceLoose:
    def __init__(self, page: Page):
        self.page = page

    # Escolhe cliente CPF para gerar pedido de venda - pesquisa por cliente.
    def choose_client_order(self):
        campo_cliente = self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header')
        self.page.wait_for_timeout(500)
        campo_cliente.type('48976249089 {ArrowDown}')
        self.page.wait_for_timeout(200)

        lupa_pesquisa_clientes = self.page.locator('.md-block > .ng-binding')
        expect(lupa_pesquisa_clientes).to_be_visible()
        lupa_pesquisa_clientes.click()

        self.page.wait_for_timeout(1500)
        cliente_selecionado = self.page.locator('.md-3-line > div.md-button > .md-no-style')
        expect(cliente_selecionado).to_be_visible()
        cliente_selecionado.click()

    # Valida e clica no menu de opções.
    def icon_menu_options(self):
        icone_menu_opcoes = self.page.locator('[aria-label="Menu de opções"] > .ng-binding')
        expect(icone_menu_opcoes).to_be_visible()
        expect(icone_menu_opcoes).not_to_have_attribute('disabled', '')
        icone_menu_opcoes.click(force=True)

    # Valida a opção Cliente Completo no menu e clica nela.
    def client_complete_option_menu(self):
        icone_cliente_completo = self.page.locator('md-icon[md-svg-src="images/icons/cliente_completo.svg"]')
        icone_cliente_completo.scroll_into_view_if_needed()
        expect(icone_cliente_completo).to_be_visible()

        opcao_cliente_completo = self.page.locator('a[aria-label="Cliente completo"]')
        expect(opcao_cliente_completo).to_be_visible()
        expect(opcao_cliente_completo).not_to_have_attribute('disabled', '')
        expect(opcao_cliente_completo).to_have_attribute('aria-label', 'Cliente completo')
        opcao_cliente_completo.click(force=True)

    # Insere número do pedido no campo Cliente ou pedido.
    def search_order_number(self, nome_cliente_cpf):
        label_campo_cliente_ou_pedido = self.page.locator('label[for="input_96"]')
        expect(label_campo_cliente_ou_pedido).to_have_text('Cliente ou pedido')

        campo_cliente_ou_pedido = self.page.locator('#input_96')
        expect(campo_cliente_ou_pedido).to_be_visible()
        expect(campo_cliente_ou_pedido).to_have_value('')
        campo_cliente_ou_pedido.type(nome_cliente_cpf, force=True)

    # Valida e clica no menu dentro do cadastro de cliente completo.
    def click_menu_client_complete(self):
        menu_click_pri = self.page.locator('#menu_click_pri')
        expect(menu_click_pri).to_be_visible()
        expect(menu_click_pri).not_to_have_attribute('disabled', '')
        menu_click_pri.click(force=True)

    # Valida e clica na opção Serviços.
    def click_option_services(self):
        elemento_validacao = self.page.locator('div[ng-repeat="tab in tabs"][ng-if="tab.checked"]')
        expect(elemento_validacao).to_be_visible()
        expect(elemento_validacao).to_contain_text('Serviços')
        expect(elemento_validacao).not_to_have_attribute('disabled', '')

        elemento_clique = self.page.locator('#menu_mais_pri > :nth-child(3)')
        elemento_clique.click(force=True)

    # Aguarda mensagem de carregamento da aba de serviços.
    def wait_loading_service(self):
        icone_carregamento = self.page.locator('.layout-align-center-center > .md-accent')
        expect(icone_carregamento).to_be_visible()
        mensagem_carregando = self.page.locator('.carregando')
        expect(mensagem_carregando).to_be_visible()
        expect(mensagem_carregando).to_have_text('Aguarde carregando...')

    # Valida o botão "Adicionar Mão de Obra".
    def button_add_mao_obra(self):
        elemento = self.page.locator('[ng-show="filtroShow(pedidoAtual)"][aria-hidden="false"] > .md-list-item-text > .prodServicoUl > :nth-child(1) > .md-default')
        expect(elemento).to_be_visible()
        expect(elemento).to_contain_text('Adicionar Mão de Obra')
        expect(elemento).not_to_have_attribute('disabled', '')

    # Valida o botão "Adicionar Garantias".
    def button_add_garantias(self):
        elemento = self.page.locator('[ng-show="filtroShow(pedidoAtual)"][aria-hidden="false"] > .md-list-item-text > .prodServicoUl > :nth-child(2) > .md-default')
        expect(elemento).to_be_visible()
        expect(elemento).to_contain_text('Adicionar Garantias')
        expect(elemento).not_to_have_attribute('disabled', '')

    # Clica no botão "Adicionar Mão de Obra".
    def click_add_mao_obra(self):
        elemento = self.page.locator('[ng-show="filtroShow(pedidoAtual)"][aria-hidden="false"] > .md-list-item-text > .prodServicoUl > :nth-child(1) > .md-default')
        elemento.click(force=True)

    # Clica no botão "Adicionar Garantias".
    def click_add_garantias(self):
        elemento = self.page.locator('[ng-show="filtroShow(pedidoAtual)"][aria-hidden="false"] > .md-list-item-text > .prodServicoUl > :nth-child(2) > .md-default')
        elemento.click(force=True)

    # Validações do modal de serviços vinculados apenas com Garantias.
    def modal_garantias_services_linked(self):
        titulo = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo).to_be_visible()
        expect(titulo).to_contain_text('Serviços Vinculados')
        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_be_disabled()
        mensagem = self.page.locator('p.ng-binding', has_text='Garantias')
        expect(mensagem).to_be_visible()

    # Validações do modal de serviços vinculados com "Mão de Obra".
    def modal_mao_obra_services_linked(self):
        titulo = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo).to_be_visible()
        expect(titulo).to_contain_text('Serviços Vinculados')
        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_be_disabled()
        mensagem = self.page.locator('p.ng-binding', has_text='Mão de Obra')
        mensagem.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(mensagem).to_be_visible()

    # Clica no botão OK do modal de serviços vinculados.
    def ok_services_linked(self):
        botao_salvar = self.page.locator('button[ng-click="salvar()"]')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).not_to_be_disabled()
        expect(botao_salvar).to_have_text(' Ok ')
        botao_salvar.click(force=True)

    # Valida mensagem de "Item adicionado com sucesso!".
    def mess_linked_added_sucess(self):
        toast_card = self.page.locator('.toast')
        expect(toast_card).to_be_visible()
        toast_aviso = self.page.locator('.toast-title')
        expect(toast_aviso).to_be_visible()
        expect(toast_aviso).to_have_text('Aviso')
        toast_mensagem = self.page.locator('.toast-message')
        expect(toast_mensagem).to_be_visible()
        expect(toast_mensagem).to_have_text('Item adicionado com sucesso!')

    # Clica no botão SALVAR.
    def button_save_service(self):
        botao_salvar_completo = self.page.locator('.btn')
        expect(botao_salvar_completo).to_be_visible()
        expect(botao_salvar_completo).not_to_be_disabled()
        expect(botao_salvar_completo).to_contain_text(' SALVAR ')
        botao_salvar_icone = self.page.locator('.btn > .ng-scope')
        expect(botao_salvar_icone).to_be_visible()
        expect(botao_salvar_icone).not_to_be_disabled()
        botao_salvar_completo.click(force=True)

    # Valida mensagem de carregamento após clicar em SALVAR.
    def mess_wait_loading(self):
        icone_giratorio = self.page.locator('svg')
        expect(icone_giratorio).to_be_visible()
        mensagem_aguarde = self.page.locator('text=Aguarde carregando...')
        expect(mensagem_aguarde).to_have_count(1)

    # Valida mensagem de "Registro salvo com sucesso!".
    def mess_resgistration_save_sucess(self):
        card_registro_salvo = self.page.locator('[style="display: block;"]')
        expect(card_registro_salvo).to_be_visible()
        aviso_registro_salvo = self.page.locator(':nth-child(1) > .toast-title')
        expect(aviso_registro_salvo).to_be_visible()
        expect(aviso_registro_salvo).to_have_text('Aviso')
        mensagem_registro_salvo = self.page.locator(':nth-child(1) > .toast-message')
        expect(mensagem_registro_salvo).to_be_visible()
        expect(mensagem_registro_salvo).to_have_text('Registro salvo com sucesso!')

    # Valida mensagem de "O Serviço Garantias já foi adicionado à esse produto."
    def mess_garantia_added(self):
        card_servico_garantias = self.page.locator('.toast-warning')
        expect(card_servico_garantias).to_be_visible()
        aviso_servico_garantias = self.page.locator('.toast-warning > .toast-title')
        expect(aviso_servico_garantias).to_be_visible()
        expect(aviso_servico_garantias).to_have_text('Atenção')
        expect(card_servico_garantias).to_contain_text('O Serviço Garantias já foi adicionado à esse produto.')

    # Clica no carrinho de compras.
    def click_cart_shopping(self):
        self.page.route('**/images/icons/brazil-real-symbol.svg', lambda route: route.continue_())
        api_produto_carrinho_compra = self.page.wait_for_response('**/images/icons/brazil-real-symbol.svg')
        botao_carrinho = self.page.locator('#test_btnCarrinho > .md-icon-button > .ng-binding')
        expect(botao_carrinho).to_be_visible()
        botao_carrinho.click(force=True)
        api_produto_carrinho_compra

    # Clica no botão AVANÇAR.
    def button_advance_order(self):
        botao_avancar = self.page.locator('.flex-gt-sm-50 > .md-primary')
        botao_avancar.scroll_into_view_if_needed()
        expect(botao_avancar).to_be_visible()
        expect(botao_avancar).not_to_be_disabled()
        expect(botao_avancar).to_have_text(' Avançar ')
        self.page.route('**/services/v3/pedido_forma_pagamento_lista', lambda route: route.continue_())
        api_pedido_forma_pagamento_lista = self.page.wait_for_response('**/services/v3/pedido_forma_pagamento_lista')
        botao_avancar.click(force=True)
        api_pedido_forma_pagamento_lista

    # Clica no botão "GERAR PARCELAS".
    def button_generate_installments_services(self):
        botao_gerar_parcelas = self.page.locator('.gerar-parcelas > .layout-wrap > [style="padding: 0 5px"] > .md-primary')
        botao_gerar_parcelas.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(botao_gerar_parcelas).to_have_count(1)
        expect(botao_gerar_parcelas).to_have_text('Gerar parcelas')
        self.page.route('**/views/carrinho/modalFormasPgto.html', lambda route: route.continue_())
        api_modal_forma_pagamento = self.page.wait_for_response('**/views/carrinho/modalFormasPgto.html')
        botao_gerar_parcelas.click(force=True)
        api_modal_forma_pagamento

    # Escolhe serviço para vender - código 144.
    def product_service_loose(self):
        codigo_servico = '144'
        self.page.route(r'/\/consultaprodutos\/.*144.*/', lambda route: route.continue_())
        api_consulta_produtos = self.page.wait_for_response(r'/\/consultaprodutos\/.*144.*/')
        campo_buscar_produto = self.page.locator('#searchText')
        expect(campo_buscar_produto).to_be_visible()
        expect(campo_buscar_produto).not_to_be_disabled()
        label_buscar_produto = self.page.locator('label[for="searchText"]')
        expect(label_buscar_produto).to_have_text('Buscar produtos')
        campo_buscar_produto.fill(codigo_servico)
        self.page.wait_for_timeout(100)
        expect(campo_buscar_produto).to_have_value(codigo_servico)
        api_consulta_produtos

    # Valida serviço com saldo disponível local.
    def balance_available_service(self):
        imagem_resultado = self.page.locator('.resultado-imagem')
        expect(imagem_resultado).to_be_visible()
        saldo_disponivel_label = self.page.locator('.label')
        expect(saldo_disponivel_label).to_be_visible()
        expect(saldo_disponivel_label).to_have_text('Saldo disponivel')
        background_color = saldo_disponivel_label.evaluate('el => getComputedStyle(el).backgroundColor')
        expect(background_color).to_be('rgb(92, 184, 92)')
        titulo_servico = self.page.locator('.md-resultado-titulo')
        expect(titulo_servico).to_be_visible()
        codigo_servico = self.page.locator('.badge-saldo.ng-binding')
        expect(codigo_servico).to_be_visible()
        simbolo_real = self.page.locator('sup')
        expect(simbolo_real).to_be_visible()
        expect(simbolo_real).to_have_text('R$')
        valor_servico = self.page.locator('.valor-busca')
        expect(valor_servico).to_be_visible()

    # Clica para selecionar o produto para adicionar ao pedido.
    def choose_service_search(self):
        expect(self.page.locator('.resultado-imagem')).to_be_visible()
        expect(self.page.locator('.md-resultado-titulo')).to_be_visible()
        expect(self.page.locator('.md-list-item-text > .ng-scope')).to_be_visible()
        expect(self.page.locator('.badge-saldo.ng-binding')).to_be_visible()
        expect(self.page.locator('sup')).to_be_visible()
        expect(self.page.locator('sup')).to_have_text('R$')
        expect(self.page.locator('.valor-busca')).to_be_visible()
        self.page.route('**/services/v3/produto_servico/*', lambda route: route.continue_())
        api_produto_servico = self.page.wait_for_response('**/services/v3/produto_servico/*')
        adicionar_carrinho = self.page.locator('.md-list-item-text')
        expect(adicionar_carrinho).to_be_visible()
        adicionar_carrinho.click(force=True)
        api_produto_servico

    # Valida mensagem de "Item adicionado com sucesso!".
    def mess_item_added_sucess(self):
        card_servico_garantias = self.page.locator('.toast')
        expect(card_servico_garantias).to_be_visible()
        aviso_servico_garantias = self.page.locator('.toast-title')
        expect(aviso_servico_garantias).to_be_visible()
        expect(aviso_servico_garantias).to_have_text('Aviso')
        mensagem_servico_garantias = self.page.locator('.toast-message')
        expect(mensagem_servico_garantias).to_be_visible()
        expect(mensagem_servico_garantias).to_contain_text('Item adicionado com sucesso!')

    # Valida que o serviço foi adicionado ao carrinho.
    def service_added_cart(self):
        card_completo = self.page.locator('.servicos > .noscroll')
        expect(card_completo).to_be_visible()
        expect(self.page.locator('span.list-title')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(2) > b')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(2) > b')).to_have_text('Quantidade:')
        expect(self.page.locator('.flex-60 > :nth-child(2)')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(3) > b')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(3) > b')).to_have_text('Vendedor:')
        expect(self.page.locator('.flex-60 > :nth-child(3)')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(3) > .md-primary')).to_be_visible()
        expect(self.page.locator('.flex-60 > :nth-child(3) > .md-primary')).not_to_be_disabled()
        expect(self.page.locator('input[ng-model="servAtual.valorFinal"]')).to_be_visible()
        expect(self.page.locator('.btn-remove-item-list > .md-button')).to_be_visible()
        expect(self.page.locator('.btn-remove-item-list > .md-button')).not_to_be_disabled()

    # Escolhe serviço host para vender - código 104.
    def product_service_host(self):
        codigo_servico_host = '104'
        campo_buscar_produto = self.page.locator('#searchText')
        expect(campo_buscar_produto).to_be_visible()
        expect(campo_buscar_produto).not_to_be_disabled()
        mensagem_campo_buscar_produto = self.page.locator('label[for="searchText"]')
        expect(mensagem_campo_buscar_produto).to_have_text('Buscar produtos')
        campo_buscar_produto.type(codigo_servico_host)
        self.page.wait_for_timeout(100)
        expect(campo_buscar_produto).to_have_value(codigo_servico_host)

    # Valida e clica na opção Serviços do menu de opções.
    def click_service_menu(self):
        opcao_servicos_menu = self.page.locator('a[aria-label="Serviços"]')
        expect(opcao_servicos_menu).to_be_visible()
        expect(opcao_servicos_menu).not_to_have_attribute('disabled', '')
        expect(opcao_servicos_menu).to_have_attribute('aria-label', 'Serviços')
        icone_servicos = self.page.locator('[role="listitem"][href="#!/servicos"] > div.md-button > .md-no-style')
        icone_servicos.scroll_into_view_if_needed()
        expect(icone_servicos).to_be_visible()
        icone_servicos.click(force=True)

    # Modal para selecionar faixa de preço para o serviço.
    def choose_value_recharge(self):
        titulo_modal_preco = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')
        expect(titulo_modal_preco).to_be_visible()
        expect(titulo_modal_preco).to_contain_text('Selecione uma faixa de preço para o serviço')
        botao_fechar_modal = self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar_modal).to_be_visible()
        expect(botao_fechar_modal).not_to_be_disabled()
        garantia_celular_host = self.page.locator('.md-subheader-content')
        expect(garantia_celular_host).to_be_visible()
        expect(garantia_celular_host).to_contain_text('Recarga Celular HOST')
        expect(self.page.locator('h3.ng-binding')).to_be_visible()
        valor_servico_card = self.page.locator('.md-no-style > .md-list-item-text > p.ng-binding')
        expect(valor_servico_card).to_be_visible()
        expect(valor_servico_card).to_contain_text('Valor:')
        valor_recarga = self.page.locator('.md-secondary-container > :nth-child(1)')
        expect(valor_recarga).to_be_visible()
        expect(valor_recarga).to_contain_text('Valor')
        caixa_escolha_valor = self.page.locator('.md-text.ng-binding', has_text='2,00').locator('..').locator('md-select-value')
        caixa_escolha_valor.click()
        valor_recarga_selecionado = self.page.locator('.md-text.ng-binding', has_text='10,00')
        valor_recarga_selecionado.click(force=True)
        self.page.wait_for_timeout(200)
        botao_ok = self.page.locator('.layout-align-end-end > .md-raised')
        expect(botao_ok).to_be_visible()
        expect(botao_ok).not_to_be_disabled()
        expect(botao_ok).to_have_text(' Ok ')
        botao_ok.click(force=True)