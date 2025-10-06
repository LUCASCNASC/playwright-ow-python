from playwright.sync_api import expect, Page

# Page Object para validações e interações na tela de login.
class Login:
    def __init__(self, page: Page):
        self.page = page

    # Validando Logo da empresa
    def logo_enterprise_login(self):
        assert self.page.locator('.logo').is_visible()

    # Validando Ícone do computador
    def icon_computer_login(self):
        expect(self.page.locator('[ng-click="clienteStatsOpen()"] > .ng-binding')).to_be_visible()
        expect(self.page.locator('[ng-click="clienteStatsOpen()"] > .ng-binding')).not_to_have_attribute('disabled', '')

    # Validando texto usuário, acima do campo usuário e ícone
    def user_text_icon(self):
        expect(self.page.locator('label[for="txtusername"]')).to_be_visible()
        expect(self.page.locator('label[for="txtusername"]')).to_have_text('Usuário')
        expect(self.page.locator(':nth-child(3) > .name')).to_be_visible()

    # Validando texto Senha, acima do campo senha e ícone
    def password_text_icon(self):
        expect(self.page.locator('label[for="txtpassword"]')).to_be_visible()
        expect(self.page.locator('label[for="txtpassword"]')).to_have_text('Senha')
        expect(self.page.locator('.md-icon-right > .name')).to_be_visible()

    # Ícone de visualizar senha
    def icon_eyes_password(self):
        expect(self.page.locator('.md-icon-right > .md-primary')).to_be_visible()
        expect(self.page.locator('.md-icon-right > .md-primary')).not_to_have_attribute('disabled', '')

    # Botão Esqueceu Senha
    def button_forgot_password(self):
        expect(self.page.locator('div[ng-click="modalSenhaNovaOpen()"]').filter(has_text='Esqueceu a senha?')).to_be_visible()
        expect(self.page.locator('div[ng-click="modalSenhaNovaOpen()"]').filter(has_text='Esqueceu a senha?')).not_to_have_attribute('disabled', '')

    # Botão entrar habilitado
    def button_enter_enabled(self):
        expect(self.page.locator('.test_btnSalvarCliente')).to_be_visible()
        expect(self.page.locator('.test_btnSalvarCliente')).to_have_text('Entrar')
        expect(self.page.locator('.test_btnSalvarCliente')).not_to_have_attribute('disabled', '')

    # Botão entrar desabilitado
    def button_enter_disabled(self):
        expect(self.page.locator('.test_btnSalvarCliente')).to_be_visible()
        expect(self.page.locator('.test_btnSalvarCliente')).to_have_text('Entrar')
        expect(self.page.locator('.test_btnSalvarCliente')).not_to_have_attribute('not.disabled', '')

    # Clicar no botão entrar
    def click_button_enter(self):
        self.page.locator('.test_btnSalvarCliente').click(force=True)

    # Mensagem Entrando no sistema
    def message_opening_system(self):
        expect(self.page.locator('.ng-scope > .ng-binding')).to_be_visible()
        expect(self.page.locator('.ng-scope > .ng-binding')).to_have_text('Entrando no sistema')

    # Botão INICIAR ATENDIMENTO - validando que entrou no sistema
    def button_init_service(self):
        expect(self.page.locator('.md-raised > .truncate')).to_be_visible()

    # Mensagem Login ou senha incorretos
    def mess_login_password_incorrect(self):
        expect(self.page.locator('.toast')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_be_visible()
        expect(self.page.locator('.toast-title')).to_have_text('Atenção')
        expect(self.page.locator('.toast-title')).not_to_have_attribute('disabled', '')
        expect(self.page.locator('.toast-message')).to_be_visible()
        expect(self.page.locator('.toast-message')).to_have_text('Login ou Senha do usuário está incorreto.')
        expect(self.page.locator('.toast-message')).not_to_have_attribute('disabled', '')
        expect(self.page.locator('.toast-close-button')).to_be_visible()

    # Card de expira acesso - "Falta(m) " 2 " dia(s) para seu acesso ao sistema expirar. Favor atualizá-lo."
    def expires_acess_card_validate(self):
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-content-body > .ng-binding')).to_have_text('Falta(m) "2" dia(s) para seu acesso ao sistema expirar. Favor atualizá-lo.')
        expect(self.page.locator('.md-cancel-button')).to_be_visible()
        expect(self.page.locator('.md-cancel-button')).to_have_text('NÃO')
        expect(self.page.locator('.md-cancel-button')).not_to_have_attribute('disabled', '')
        expect(self.page.locator('.md-confirm-button')).to_be_visible()
        expect(self.page.locator('.md-confirm-button')).to_have_text('SIM')
        expect(self.page.locator('.md-confirm-button')).not_to_have_attribute('disabled', '')

    # Card de expira acesso - clicar em SIM
    def click_sim_expires(self):
        self.page.locator('.md-confirm-button').click()
        expect(self.page.locator('center')).to_be_visible()
        expect(self.page.locator('center')).to_have_text('Aguarde carregando...')

    # Validar Regras para a Nova Senha (antes de preencher campo Nova Senha)
    def rules_new_password_before(self):
        expect(self.page.locator('span', has_text='Ao menos 8 caracteres.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 8 caracteres.')).to_have_css('color', 'rgb(204, 0, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 letra maiúscula ou minúscula.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 letra maiúscula ou minúscula.')).to_have_css('color', 'rgb(204, 0, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 algarismo.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 algarismo.')).to_have_css('color', 'rgb(204, 0, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 caractere especial.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 caractere especial.')).to_have_css('color', 'rgb(204, 0, 0)')
        expect(self.page.locator('span', has_text='A nova senha não pode ser a atual.')).to_be_visible()
        expect(self.page.locator('span', has_text='A nova senha não pode ser a atual.')).to_have_css('color', 'rgb(204, 0, 0)')
        expect(self.page.locator('span', has_text='As novas senhas informadas são iguais.')).to_be_visible()
        expect(self.page.locator('span', has_text='As novas senhas informadas são iguais.')).to_have_css('color', 'rgb(204, 0, 0)')

    # Validar Regras para a Nova Senha (depois de preencher campo Nova Senha)
    def rules_new_password_after(self):
        expect(self.page.locator('span', has_text='Ao menos 8 caracteres.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 8 caracteres.')).to_have_css('color', 'rgb(0, 100, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 letra maiúscula ou minúscula.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 letra maiúscula ou minúscula.')).to_have_css('color', 'rgb(0, 100, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 algarismo.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 algarismo.')).to_have_css('color', 'rgb(0, 100, 0)')
        expect(self.page.locator('span', has_text='Ao menos 1 caractere especial.')).to_be_visible()
        expect(self.page.locator('span', has_text='Ao menos 1 caractere especial.')).to_have_css('color', 'rgb(0, 100, 0)')
        expect(self.page.locator('span', has_text='A nova senha não pode ser a atual.')).to_be_visible()
        expect(self.page.locator('span', has_text='A nova senha não pode ser a atual.')).to_have_css('color', 'rgb(0, 100, 0)')
        expect(self.page.locator('span', has_text='As novas senhas informadas são iguais.')).to_be_visible()
        expect(self.page.locator('span', has_text='As novas senhas informadas são iguais.')).to_have_css('color', 'rgb(204, 0, 0)')

    # Validar card "Sua Senha expirou" quando a senha do usuário está expirada
    def mess_password_user_expired(self):
        expect(self.page.locator('.md-dialog-content-body')).to_be_visible()
        expect(self.page.locator('.md-dialog-content-body')).to_have_text('Sua Senha expirou...')
        expect(self.page.locator('md-dialog-actions > .md-primary')).to_be_visible()
        expect(self.page.locator('md-dialog-actions > .md-primary')).to_have_text('Ok')
        expect(self.page.locator('md-dialog-actions > .md-primary')).not_to_have_attribute('disabled', '')
        self.page.locator('md-dialog-actions > .md-primary').click()