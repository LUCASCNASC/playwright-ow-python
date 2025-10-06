from playwright.sync_api import expect, Page

# Page Object para validações finais na tela de pedido.
class ValidaFinal:
    def __init__(self, page: Page):
        self.page = page

    # Valida informações do cliente na última tela sem entrega.
    def info_cliente_sem_entrega(self):
        titulo_cliente = self.page.locator('.flex-gt-xs-100 > .md-primary > .md-toolbar-tools > .flex')
        titulo_cliente.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(titulo_cliente).to_be_visible()
        expect(titulo_cliente).to_have_text('Cliente')

        nome_label = self.page.locator('.cliente > :nth-child(1) > b')
        expect(nome_label).to_be_visible()
        expect(nome_label).to_have_text('Nome:')

        nome_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(1)')
        expect(nome_info).to_be_visible()
        expect(nome_info).to_contain_text('TA CPF AUTOMAÇÃO - COM ROTA')

        cpf_cnpj_label = self.page.locator('.cliente > :nth-child(2) > b')
        expect(cpf_cnpj_label).to_be_visible()
        expect(cpf_cnpj_label).to_have_text('CPF/CNPJ:')

        cpf_cnpj_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(2)')
        expect(cpf_cnpj_info).to_be_visible()
        expect(cpf_cnpj_info).to_contain_text('489.762.490-89')

        tel_fixo_label = self.page.locator('.cliente > :nth-child(3) > b')
        expect(tel_fixo_label).to_be_visible()
        expect(tel_fixo_label).to_have_text('Tel. fixo:')

        tel_fixo_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(3)')
        expect(tel_fixo_info).to_be_visible()
        expect(tel_fixo_info).to_contain_text('(44) 98656-5132')

        tel_celular_label = self.page.locator('.cliente > :nth-child(4) > b')
        expect(tel_celular_label).to_be_visible()
        expect(tel_celular_label).to_have_text('Tel. celular:')

        tel_celular_info = self.page.locator('.cliente > :nth-child(4)')
        expect(tel_celular_info).to_be_visible()
        expect(tel_celular_info).to_contain_text('(44) 98656-5132')

        email_label = self.page.locator('.cliente > :nth-child(5) > b')
        expect(email_label).to_be_visible()
        expect(email_label).to_have_text('E-mail:')

        email_info = self.page.locator('.cliente > :nth-child(5)')
        expect(email_info).to_be_visible()
        expect(email_info).to_contain_text('ta_cpf_automação_com_rota@gmail.com')

    # Valida informações do cliente na última tela com entrega.
    def info_cliente_com_entrega(self):
        titulo_cliente = self.page.locator('.confirmacao > :nth-child(1) > .md-primary > .md-toolbar-tools > .flex')
        titulo_cliente.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(titulo_cliente).to_be_visible()
        expect(titulo_cliente).to_have_text('Cliente')

        nome_label = self.page.locator('.cliente > :nth-child(1) > b')
        expect(nome_label).to_be_visible()
        expect(nome_label).to_have_text('Nome:')

        nome_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(1)')
        expect(nome_info).to_be_visible()
        expect(nome_info).to_contain_text('TA CPF AUTOMAÇÃO - COM ROTA')

        cpf_cnpj_label = self.page.locator('.cliente > :nth-child(2) > b')
        expect(cpf_cnpj_label).to_be_visible()
        expect(cpf_cnpj_label).to_have_text('CPF/CNPJ:')

        cpf_cnpj_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(2)')
        expect(cpf_cnpj_info).to_be_visible()
        expect(cpf_cnpj_info).to_contain_text('489.762.490-89')

        tel_fixo_label = self.page.locator('.cliente > :nth-child(3) > b')
        expect(tel_fixo_label).to_be_visible()
        expect(tel_fixo_label).to_have_text('Tel. fixo:')

        tel_fixo_info = self.page.locator('.padding-10 > :nth-child(1) > .cliente > :nth-child(3)')
        expect(tel_fixo_info).to_be_visible()
        expect(tel_fixo_info).to_contain_text('(44) 98656-5132')

        tel_celular_label = self.page.locator('.cliente > :nth-child(4) > b')
        expect(tel_celular_label).to_be_visible()
        expect(tel_celular_label).to_have_text('Tel. celular:')

        tel_celular_info = self.page.locator('.cliente > :nth-child(4)')
        expect(tel_celular_info).to_be_visible()
        expect(tel_celular_info).to_contain_text('(44) 98656-5132')

        email_label = self.page.locator('.cliente > :nth-child(5) > b')
        expect(email_label).to_be_visible()
        expect(email_label).to_have_text('E-mail:')

        email_info = self.page.locator('.cliente > :nth-child(5)')
        expect(email_info).to_be_visible()
        expect(email_info).to_contain_text('ta_cpf_automação_com_rota@gmail.com')

        email_nfe_label = self.page.locator('.cliente > :nth-child(6) > b')
        expect(email_nfe_label).to_be_visible()
        expect(email_nfe_label).to_have_text('E-mail NF-e:')

        email_nfe_info = self.page.locator('.cliente > :nth-child(6)')
        expect(email_nfe_info).to_be_visible()
        expect(email_nfe_info).to_contain_text('ta_cpf_automação_com_rota@gmail.com')

        botao_editar = self.page.locator('.padding-10 > :nth-child(1) > .cliente > .md-accent')
        expect(botao_editar).to_be_visible()
        expect(botao_editar).not_to_be_disabled()
        expect(botao_editar).to_have_text('Editar')

        consumidor_final_botao = self.page.locator('.flex-100 > .md-auto-horizontal-margin > .md-container')
        expect(consumidor_final_botao).to_be_visible()
        expect(consumidor_final_botao).not_to_be_disabled()

        consumidor_final_label = self.page.locator('.flex-100 > .md-auto-horizontal-margin > .md-label')
        expect(consumidor_final_label).to_be_visible()
        expect(consumidor_final_label).not_to_be_disabled()
        expect(consumidor_final_label).to_contain_text('Consumidor Final')

    # Valida informações do endereço de entrega na última tela.
    def info_entrega(self):
        titulo_endereco_entrega = self.page.locator('h2[ng-show="carrinho.endereco.local == \'entrega\'"]')
        titulo_endereco_entrega.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(titulo_endereco_entrega).to_be_visible()
        expect(titulo_endereco_entrega).to_have_text('Endereço de entrega')

        cep_label = self.page.locator('.endereco > :nth-child(1) > b')
        expect(cep_label).to_be_visible()
        expect(cep_label).to_have_text('CEP:')

        cep_info = self.page.locator('.endereco > :nth-child(1)')
        expect(cep_info).to_be_visible()
        expect(cep_info).to_contain_text('87.065-320')

        endereco_label = self.page.locator('.endereco > :nth-child(2) > b')
        expect(endereco_label).to_be_visible()
        expect(endereco_label).to_have_text('Endereço:')

        endereco_info = self.page.locator('.endereco > :nth-child(2)')
        expect(endereco_info).to_be_visible()
        expect(endereco_info).to_contain_text('RUA TULIPA, 232, PARQUE INDUSTRIAL, MARINGA/PR')

        telefone_label = self.page.locator('.endereco > :nth-child(3) > b')
        expect(telefone_label).to_be_visible()
        expect(telefone_label).to_have_text('Telefone:')

        telefone_info = self.page.locator('.endereco > :nth-child(3) > .ng-binding')
        expect(telefone_info).to_be_visible()
        expect(telefone_info).to_contain_text('(44) 9865-5132')

        rota_label = self.page.locator('[ng-show="(carrinho.frete && carrinho.frete.rota && carrinho.endereco.local == \'entrega\')"] > b')
        expect(rota_label).to_be_visible()
        expect(rota_label).to_have_text('Rota:')

        rota_info = self.page.locator('[ng-show="(carrinho.frete && carrinho.frete.rota && carrinho.endereco.local == \'entrega\')"]')
        expect(rota_info).to_be_visible()
        expect(rota_info).to_contain_text('Rota Maringá, Centro')

        botao_editar_telefone = self.page.locator('.endereco > .md-accent')
        expect(botao_editar_telefone).to_be_visible()
        expect(botao_editar_telefone).not_to_be_disabled()
        expect(botao_editar_telefone).to_have_text('Editar Telefone')

    # Valida campo de "Observações para a nota fiscal" vazio.
    def obs_nota_fiscal_vazio(self):
        observacoes_nota_fiscal_label = self.page.locator(':nth-child(1) > .header-interno > label')
        expect(observacoes_nota_fiscal_label).to_be_visible()
        expect(observacoes_nota_fiscal_label).to_have_text('OBSERVAÇÕES PARA A NOTA FISCAL')
        campo_observacoes = self.page.locator(':nth-child(1) > .col-md-12 > .form-group > .form-control')
        expect(campo_observacoes).to_be_visible()
        expect(campo_observacoes).not_to_be_disabled()
        expect(campo_observacoes).to_have_value('')

    # Valida campo de "Observações para uso interno" vazio.
    def obs_interna_vazio(self):
        observacoes_uso_interno_label = self.page.locator(':nth-child(2) > .header-interno > label')
        expect(observacoes_uso_interno_label).to_be_visible()
        expect(observacoes_uso_interno_label).to_have_text('OBSERVAÇÕES PARA USO INTERNO')
        campo_observacoes_interno = self.page.locator(':nth-child(2) > .col-md-12 > .form-group > .form-control')
        expect(campo_observacoes_interno).to_be_visible()
        expect(campo_observacoes_interno).not_to_be_disabled()
        expect(campo_observacoes_interno).to_have_value('')
        expect(campo_observacoes_interno).to_have_attribute('maxlength', '300')
        limite_caracteres = self.page.locator('.form-group > span')
        expect(limite_caracteres).to_be_visible()
        expect(limite_caracteres).to_have_text('Limite de 300 caracteres')