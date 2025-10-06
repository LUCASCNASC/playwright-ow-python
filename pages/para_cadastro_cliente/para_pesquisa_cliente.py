from playwright.sync_api import expect, Page

# Page Object para pesquisa e seleção de clientes.
class SearchClient:
    def __init__(self, page: Page):
        self.page = page

    # Validando mensagem "Aguarde carregando..."
    def mess_wait_loading(self):
        self.page.locator('.md-dialog-fullscreen > .carregando').wait_for(state='visible')
        text = self.page.locator('.md-dialog-fullscreen > .carregando').text_content()
        expect(text).to_be(' Aguarde carregando...')

    # Clicando na lupa pesquisa de cliente
    def click_glass_search_client(self):
        self.page.route('**/views/cliente/modalClientes.html', lambda route: route.continue_())
        self.page.locator('.md-block > .ng-binding').wait_for(state='visible')
        self.page.locator('.md-block > .ng-binding').click(force=True)
        self.page.wait_for_response('**/views/cliente/modalClientes.html', timeout=40000)

    # Validando botão X do card cliente
    def card_client_validate(self):
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('.md-dialog-fullscreen')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > ._md-toolbar-transitions > .md-toolbar-tools > .flex')).to_have_text('Clientes')
        expect(self.page.locator('label[for="txtBuscaClienteModal"]')).to_have_text('Digite o nome ou o CPF do cliente para busca')
        expect(self.page.locator('label[for="txtBuscaClienteModal"]')).to_be_visible()
        expect(self.page.locator('[ng-click="novoCliente()"] > .ng-binding')).to_be_visible()
        expect(self.page.locator('[ng-click="novoCliente()"] > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('[ng-click="capturarVozCliente()"] > .ng-binding')).to_be_visible()
        expect(self.page.locator('[ng-click="capturarVozCliente()"] > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('#txtBuscaClienteModal')).to_be_visible()
        input_value = self.page.locator('#txtBuscaClienteModal').input_value()
        assert input_value != ''

    # Validando número e descrição do cliente CPF selecionado
    def number_descrip_cpf_search(self):
        expect(self.page.locator('#lblCpfClienteSelecionado')).to_be_visible()
        expect(self.page.locator('#lblNomeClienteSelecionado')).to_be_visible()

    # Validando número e descrição do cliente CNPJ selecionado
    def number_descrip_cnpj_search(self):
        expect(self.page.locator('#lblCpfClienteSelecionado')).to_be_visible()
        expect(self.page.locator('#lblNomeClienteSelecionado')).to_be_visible()

    # Clicando cliente CPF pesquisado
    def click_cpf_search(self):
        expect(self.page.locator('button[aria-label="CPF AUTOMACAO SABIUM - LUCAS CAMARGO 117.415.410-18   - MARINGA/PR"]')).to_be_visible()
        expect(self.page.locator('button[aria-label="CPF AUTOMACAO SABIUM - LUCAS CAMARGO 117.415.410-18   - MARINGA/PR"]')).not_to_have_attribute('disabled', 'true')
        self.page.locator('button[aria-label="CPF AUTOMACAO SABIUM - LUCAS CAMARGO 117.415.410-18   - MARINGA/PR"]').click()

    # Clicando cliente CNPJ pesquisado
    def click_cnpj_search(self):
        expect(self.page.locator('button[aria-label="CNPJ AUTOMACAO SABIUM - LUCAS CAMARGO 24.468.163/0001-61   - MARINGA/PR"]')).to_be_visible()
        expect(self.page.locator('button[aria-label="CNPJ AUTOMACAO SABIUM - LUCAS CAMARGO 24.468.163/0001-61   - MARINGA/PR"]')).not_to_have_attribute('disabled', 'true')
        self.page.locator('button[aria-label="CNPJ AUTOMACAO SABIUM - LUCAS CAMARGO 24.468.163/0001-61   - MARINGA/PR"]').click()

    # Pesquisar cliente por número de CPF
    def fill_cpf(self):
        numero_cpf = "117.415.410-18"
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').wait_for(state='visible')
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').type(numero_cpf, delay=500)

    # Digitar cliente por número de CPF
    def type_again_cpf(self):
        numero_cpf = "117.415.410-18"
        input_locator = self.page.locator('#txtBuscaClienteModal')
        input_locator.clear()
        self.page.wait_for_timeout(100)
        expect(input_locator).to_have_value('')
        self.page.wait_for_timeout(100)
        input_locator.type(numero_cpf)

    # Pesquisar cliente por número de CNPJ
    def fill_cnpj(self):
        numero_cnpj = "24468163000161"
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').wait_for(state='visible')
        self.page.wait_for_timeout(500)
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').type(numero_cnpj, delay=100)

    # Digitar cliente por número de CNPJ
    def type_again_cnpj(self):
        numero_cnpj = "24468163000161"
        input_locator = self.page.locator('#txtBuscaClienteModal')
        input_locator.clear()
        self.page.wait_for_timeout(100)
        expect(input_locator).to_have_value('')
        self.page.wait_for_timeout(100)
        input_locator.type(numero_cnpj)

    # Pesquisar cliente por descrição de CPF
    def fill_descrip_cpf(self):
        descricao_cpf = "CPF AUTOMAÇÃO SABIUM - LUCAS CAMARGO"
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').click()
        self.page.locator('#txtBuscaCliente').wait_for(state='visible')
        self.page.wait_for_timeout(500)
        self.page.locator('#txtBuscaCliente').type(descricao_cpf, delay=100)

    # Digitar cliente por descrição de CPF
    def type_again_descript_cpf(self):
        descricao_cpf = "CPF AUTOMAÇÃO SABIUM - LUCAS CAMARGO"
        input_locator = self.page.locator('#txtBuscaClienteModal')
        input_locator.clear()
        self.page.wait_for_timeout(100)
        expect(input_locator).to_have_value('')
        self.page.wait_for_timeout(100)
        input_locator.type(descricao_cpf)

    # Pesquisar cliente por descrição de CNPJ
    def fill_descrip_cnpj(self):
        descricao_cnpj = "CNPJ AUTOMAÇÃO SABIUM - LUCAS CAMARGO"
        self.page.locator('.click-cliente > .informe-o-cliente > .cliente-header').click()
        self.page.locator('#txtBuscaCliente').wait_for(state='visible')
        self.page.wait_for_timeout(500)
        self.page.locator('#txtBuscaCliente').type(descricao_cnpj, delay=100)

    # Digitar cliente por descrição de CNPJ
    def type_again_descript_cnpj(self):
        descricao_cnpj = "CNPJ AUTOMAÇÃO SABIUM - LUCAS CAMARGO"
        input_locator = self.page.locator('#txtBuscaClienteModal')
        input_locator.clear()
        self.page.wait_for_timeout(100)
        expect(input_locator).to_have_value('')
        self.page.wait_for_timeout(100)
        input_locator.type(descricao_cnpj)