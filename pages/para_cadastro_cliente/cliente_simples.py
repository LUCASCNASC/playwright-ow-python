from ..gerarDados import gerarCpf, gerarNomeAleatorio, gerarCNPJ, gerarNomeEmpresa
from playwright.sync_api import expect, Page

# Page Object para preencher dados do cliente simples (formulário).
class FillClientSimple:
    def __init__(self, page: Page):
        self.page = page

    # Campo Data Nascimento - validar e preencher
    def date_birth(self):
        expect(self.page.locator(':nth-child(3) > .layout-xs-column > .md-block > .validaData > .md-datepicker-button')).to_be_visible()
        expect(self.page.locator(':nth-child(3) > .layout-xs-column > .md-block > .validaData > .md-datepicker-button')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[aria-hidden="false"]')).to_have_text('Data de nascimento')
        expect(self.page.locator('input[ng-focus="ctrl.setFocused(true)"]')).to_be_visible()
        expect(self.page.locator('input[ng-focus="ctrl.setFocused(true)"]')).to_have_value('')
        self.page.wait_for_timeout(200)
        self.page.locator('input[ng-focus="ctrl.setFocused(true)"]').fill('30/09/1998', force=True)

    # Preencher campo CPF com CPF
    def cpf_client(self):
        cpf = gerarCpf()
        expect(self.page.locator('label[for="txtCpf"]')).to_have_text('CPF')
        expect(self.page.locator('#txtCpf')).to_be_visible()
        expect(self.page.locator('#txtCpf')).to_have_value('')
        self.page.locator('#txtCpf').fill(cpf, force=True)

    # Preencher campo CNPJ com CNPJ
    def cnpj_client(self):
        cnpj = gerarCNPJ()
        expect(self.page.locator('label[for="txtCNPJ"]')).to_have_text('CNPJ')
        expect(self.page.locator('#txtCNPJ')).to_be_visible()
        expect(self.page.locator('#txtCNPJ')).to_have_value('')
        self.page.locator('#txtCNPJ').fill(cnpj, force=True)

    # Campo Nome completo - cliente CPF
    def name_complete_cpf(self):
        nome_completo = gerarNomeAleatorio()
        expect(self.page.locator('label[for="txtNomeCompleto"]')).to_have_text('Nome Completo')
        expect(self.page.locator('#txtNomeCompleto')).to_be_visible()
        expect(self.page.locator('#txtNomeCompleto')).to_have_value('')
        self.page.locator('#txtNomeCompleto').fill(nome_completo, force=True)

    # Campo Nome completo - cliente CNPJ
    def name_complete_cnpj(self):
        nome_completo_empresa = gerarNomeEmpresa()
        expect(self.page.locator('label[for="txtNomeCompleto"]')).to_have_text('Nome Completo')
        expect(self.page.locator('#txtNomeCompleto')).to_be_visible()
        expect(self.page.locator('#txtNomeCompleto')).to_have_value('')
        self.page.wait_for_timeout(200)
        self.page.locator('#txtNomeCompleto').fill(nome_completo_empresa, force=True)

    # Selecionar sexo da pessoa física
    def sex_person_physical(self):
        self.page.locator('.md-default-theme[ng-model="cliente.idtiposexo"]').scroll_into_view_if_needed()
        expect(self.page.locator('.md-default-theme[ng-model="cliente.idtiposexo"]')).to_be_visible()
        expect(self.page.locator('.md-default-theme[ng-model="cliente.idtiposexo"]')).to_have_value('')
        self.page.locator('.md-default-theme[ng-model="cliente.idtiposexo"]').click(force=True)
        self.page.locator('.md-text.ng-binding', has_text='Masculino').click(force=True)

    # Campo CEP - inserir e pesquisar
    def search_cep(self):
        cep_cadastro = "87065300"
        expect(self.page.locator('label[for="txtCep"]')).to_have_text('CEP')
        self.page.locator('#txtCep').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(self.page.locator('#txtCep')).to_be_visible()
        expect(self.page.locator('#txtCep')).to_have_value('')
        self.page.locator('#txtCep').fill(cep_cadastro, force=True)
        expect(self.page.locator('.md-icon-float > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-icon-float > .ng-binding')).not_to_have_attribute('disabled', 'true')
        # No Python Playwright não existe .as, então use o padrão de espera
        self.page.route('**/services/v3/cidade?uf=PR', lambda route: route.continue_())
        self.page.locator('.md-icon-float > .ng-binding').click(force=True)
        self.page.wait_for_response('**/services/v3/cidade?uf=PR', timeout=40000)

    # Campo Número - validar e preencher
    def number_adress(self):
        numero_rendereco = '66'
        expect(self.page.locator('label[for="txtNumero"]')).to_have_text('Número')
        expect(self.page.locator('#txtNumero')).to_be_visible()
        expect(self.page.locator('#txtNumero')).to_have_value('')
        self.page.locator('#txtNumero').fill(numero_rendereco, force=True)

    # Preenchendo rota do cadastro de cliente
    def route_client(self):
        rota = '560'
        expect(self.page.locator('label[for="codigo_rota"]')).to_have_text('Código da rota')
        self.page.route('**/views/carrinho/modalRotas.html', lambda route: route.continue_())
        expect(self.page.locator('.rota-frete > .md-icon-right > .ng-binding')).to_be_visible()
        expect(self.page.locator('.rota-frete > .md-icon-right > .ng-binding')).to_have_value('')
        self.page.locator('.rota-frete > .md-icon-right > .ng-binding').fill(rota, force=True)
        self.page.wait_for_response('**/views/carrinho/modalRotas.html', timeout=40000)
        expect(self.page.locator('.rota-frete > .md-icon-right > .ng-binding')).to_be_visible()
        expect(self.page.locator('.rota-frete > .md-icon-right > .ng-binding')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('label[for="txtBuscaRotaModal"]')).to_have_text('Rota')
        expect(self.page.locator('#txtBuscaRotaModal')).to_be_visible()
        expect(self.page.locator('#txtBuscaRotaModal')).to_have_value('')
        self.page.locator('#txtBuscaRotaModal').fill(rota, force=True)
        self.page.keyboard.press('ArrowDown')
        expect(self.page.locator('md-icon[aria-label="Pesquisar"]')).to_be_visible()
        expect(self.page.locator('md-icon[aria-label="Pesquisar"]')).not_to_have_attribute('disabled', 'true')
        self.page.route('**/services/v3/rota?idrota=560', lambda route: route.continue_())
        self.page.locator('md-icon[ng-click="pesquisar()"]').click(force=True)
        self.page.wait_for_response('**/services/v3/rota?idrota=560', timeout=40000)
        self.page.locator('text=560 - T.A. ROTA AUTOMAÇÃO MARINGÁ').click()
        self.page.route('**/services/v3/local_entrega?rota=560', lambda route: route.continue_())
        self.page.locator('text=560 - T.A. CIDADE AUTOMAÇÃO').click()
        self.page.wait_for_response('**/services/v3/local_entrega?rota=560', timeout=40000)

# Page Object para operações com cliente simples.
class GeneralClientSimple:
    def __init__(self, page: Page):
        self.page = page

    # Clica no ícone do menu de opções.
    def icon_menu_options(self):
        expect(self.page.locator('[aria-label="Menu de opções"] > .ng-binding')).to_be_visible()
        expect(self.page.locator('[aria-label="Menu de opções"] > .ng-binding')).not_to_have_attribute('disabled', 'true')
        self.page.click('[aria-label="Menu de opções"] > .ng-binding', force=True)

    # Escolhe a opção cliente no menu de opções.
    def option_client_simple(self):
        expect(self.page.locator('a[aria-label="Cliente"]')).to_have_attribute('aria-label', 'Cliente')
        self.page.locator('a[aria-label="Cliente"]').scroll_into_view_if_needed()
        self.page.click('a[aria-label="Cliente"]', force=True)

    # Clica no botão SALVAR do cliente simples.
    def save_client_simple(self):
        self.page.locator('.layout-align-end-center > .md-raised').scroll_into_view_if_needed()
        expect(self.page.locator('.layout-align-end-center > .md-raised')).to_be_visible()
        expect(self.page.locator('.layout-align-end-center > .md-raised')).not_to_have_attribute('disabled', 'true')
        self.page.click('.layout-align-end-center > .md-raised', force=True)

    # Arrasta para pessoa jurídica.
    def drag_person_legal(self):
        expect(self.page.locator('.flex-md-100 > .md-auto-horizontal-margin > .md-label')).to_be_visible()
        expect(self.page.locator('.flex-md-100 > .md-auto-horizontal-margin > .md-label')).to_contain_text('Pessoa Física/Pessoa Júridica')
        self.page.click('.flex-md-100 > .md-auto-horizontal-margin > .md-label', force=True)

    # Mensagem de "Registro salvo com sucesso!"
    def mess_first_regist_save_sucess(self):
        expect(self.page.locator('.toast')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_have_text('Aviso')
        expect(self.page.locator('.toast-message')).to_be_visible()
        expect(self.page.locator('.toast-message')).to_have_text('Registro salvo com sucesso!')

    # Logar novamente no sistema.
    def login_again(self):
        self.page.fill('#txtusername', 'sabium.automacao')
        self.page.fill('#txtpassword', '123.automacao')
        self.page.route('**/images/icons/discount.svg', lambda route: route.continue_())
        self.page.click('.test_btnSalvarCliente', force=True)
        self.page.wait_for_response('**/images/icons/discount.svg', timeout=40000)

    # Clica para sair do sistema.
    def click_out_system(self):
        self.page.click('.rodape > ._md-button-wrap > div.md-button > .md-no-style', force=True)

    # Valida e clica em SIM na mensagem "Deseja visualizar este cadastro?"
    def desire_see_register(self):
        expect(self.page.locator('.md-title')).to_be_visible()
        expect(self.page.locator('.md-title')).to_contain_text('Este CPF / CNPJ já está cadastrado para')
        expect(self.page.locator('.md-title')).to_contain_text(', deseja visualizar este cadastro?')
        expect(self.page.locator('.md-cancel-button')).to_be_visible()
        expect(self.page.locator('.md-cancel-button')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('.md-confirm-button')).to_be_visible()
        expect(self.page.locator('.md-confirm-button')).not_to_have_attribute('disabled', 'true')
        self.page.click('.md-confirm-button', force=True)

    # Autoriza trial ao alterar data de nascimento do cliente simples.
    def authorize_trial_date_birth(self):
        id_supervisor_trial = "393"
        nome_supervisor_trial = "T.A. USUÁRIO AUTOMAÇÃO"
        senha_supervisor = "123.automacao"

        expect(self.page.locator('.md-toolbar-tools > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-toolbar-tools > .ng-binding')).to_have_text('Autorização do Supervisor')
        expect(self.page.locator('thead > tr > :nth-child(1)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(1)')).to_have_text('Trial')
        expect(self.page.locator('tbody > .ng-scope > :nth-child(1)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(2)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(2)')).to_have_text('Descrição')
        expect(self.page.locator('tbody > .ng-scope > :nth-child(2)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(3)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(3)')).to_have_text('Status')
        expect(self.page.locator('td.ng-binding:has-text("Pendente")')).to_be_visible()
        expect(self.page.locator('td.ng-binding:has-text("Pendente")')).to_have_css('background-color', 'rgb(234, 7, 7)')
        expect(self.page.locator('thead > tr > :nth-child(4)')).to_be_visible()
        expect(self.page.locator('thead > tr > :nth-child(4)')).to_have_text('Permissão / Usuário')
        expect(self.page.locator('tbody > .ng-scope > :nth-child(4)')).to_be_visible()
        expect(self.page.locator('tbody > .ng-scope > :nth-child(4)')).to_have_text('Sim')
        expect(self.page.locator('tbody > :nth-child(2) > .ng-binding')).to_be_visible()
        expect(self.page.locator('tbody > :nth-child(2) > .ng-binding')).to_have_text('Supervisor')
        expect(self.page.locator('[ng-model="idUsuario"]')).to_be_visible()
        expect(self.page.locator('[ng-model="idUsuario"]')).to_have_value(id_supervisor_trial)
        expect(self.page.locator('[ng-model="nomeUsuario"]')).to_be_visible()
        expect(self.page.locator('[ng-model="nomeUsuario"]')).to_have_value(nome_supervisor_trial)
        expect(self.page.locator('tbody > :nth-child(3) > :nth-child(1)')).to_be_visible()
        expect(self.page.locator('tbody > :nth-child(3) > :nth-child(1)')).to_have_text('Senha')
        expect(self.page.locator(':nth-child(3) > [colspan="2"] > .ng-pristine')).to_be_visible()
        expect(self.page.locator(':nth-child(3) > [colspan="2"] > .ng-pristine')).to_have_value('')
        self.page.fill(':nth-child(3) > [colspan="2"] > .ng-pristine', senha_supervisor)
        self.page.click('button:has-text("Confirmar")')