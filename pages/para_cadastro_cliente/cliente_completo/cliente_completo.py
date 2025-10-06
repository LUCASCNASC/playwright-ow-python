from playwright.sync_api import expect, Page

# Page Object para ações de navegação e validação no cadastro de cliente completo.
class ClickClientComplete:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar no menu de opções
    def icon_menu_options(self):
        expect(self.page.locator('[aria-label="Menu de opções"] > .ng-binding')).to_be_visible()
        expect(self.page.locator('[aria-label="Menu de opções"] > .ng-binding')).not_to_have_attribute('disabled', 'true')
        self.page.click('[aria-label="Menu de opções"] > .ng-binding', force=True)

    # Escolher opção cliente completo no menu de opções
    def option_client_complete(self):
        expect(self.page.locator('a[aria-label="Cliente completo"]')).to_be_visible()
        expect(self.page.locator('a[aria-label="Cliente completo"]')).not_to_have_attribute('disabled', 'true')
        expect(self.page.locator('a[aria-label="Cliente completo"]')).to_have_attribute('aria-label', 'Cliente completo')
        self.page.locator('a[aria-label="Cliente completo"]').scroll_into_view_if_needed()
        self.page.click('a[aria-label="Cliente completo"]', force=True)

    # Validar e clicar no botão para salvar cadastro de cliente
    def save_client(self):
        self.page.locator('.btn').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(self.page.locator('.btn')).to_be_visible()
        expect(self.page.locator('.btn')).not_to_have_attribute('disabled', 'true')
        self.page.click('.btn', force=True)

    # Clicar para salvar cadastro de cliente completo
    def save_client_complete(self):
        self.page.click('.btn > .ng-scope', force=True)

    # Dentro do cadastro de cliente completo, clicar no menu para aparecer as opções dentro do cadastro
    def menu_register_client_complete(self):
        expect(self.page.locator('#menu_click_pri')).to_be_visible()
        expect(self.page.locator('#menu_click_pri')).not_to_have_attribute('disabled', 'true')
        self.page.click('#menu_click_pri')

    # Validar e clicar na aba Referências
    def aba_references(self):
        expect(self.page.locator('#menu_items_pri > :nth-child(5)')).to_be_visible()
        expect(self.page.locator('#menu_items_pri > :nth-child(5)')).not_to_have_attribute('disabled', 'true')
        self.page.route('GET', '/views/cliente/refEtapaPessoalLista.html', lambda route: route.continue_())
        self.page.locator('#menu_items_pri > :nth-child(5)').click()
        self.page.wait_for_response(
            lambda response: '/views/cliente/refEtapaPessoalLista.html' in response.url and response.status == 200,
            timeout=40000
        )

# Page Object para validações e ações de cadastro de cliente completo.
class GeneralClientComplete:
    def __init__(self, page: Page):
        self.page = page

    # Validar botão salvar sem ter os campos obrigatórios (deve estar desabilitado)
    def button_save_disabled(self):
        expect(self.page.locator('#btnModalAddEndereco')).to_be_visible()
        expect(self.page.locator('#btnModalAddEndereco')).not_to_have_attribute('disabled', 'true')

    # Clicar para salvar cadastro de cliente completo
    def click_save_client_complete(self):
        self.page.click('.btn > .ng-scope', force=True)

    # Validar mensagem "Um endereço do tipo padrão é obrigatório" ao tentar salvar sem informar endereço
    def mess_alert_address_mandatory(self):
        expect(self.page.locator('.toast')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_have_text('Alerta')
        expect(self.page.locator('.toast-message')).to_be_visible()
        expect(self.page.locator('.toast-message')).to_have_text('Um endereço do tipo padrão é obrigatório.')

    # Validar modal de "Aguarde carregando..." após salvar cadastro
    def modal_waiting_loading(self):
        expect(self.page.locator('.layout-align-center-center > h3')).to_be_visible()
        expect(self.page.locator('.layout-align-center-center > h3')).to_have_text('Aguarde carregando...')

    # Validar mensagem "Registro salvo com sucesso!" após salvar cadastro
    def mess_register_save_success(self):
        expect(self.page.locator('.toast-success')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .toast-title')).to_have_text('Aviso')
        expect(self.page.locator('.toast-success > .toast-message')).to_be_visible()
        expect(self.page.locator('.toast-success > .toast-message')).to_have_text('Registro salvo com sucesso!')