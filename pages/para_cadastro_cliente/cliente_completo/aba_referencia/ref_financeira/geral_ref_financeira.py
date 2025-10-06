from playwright.sync_api import expect, Page
from datetime import datetime, timedelta
import random

# ------referencia financeira - funções de geração de dados
def gerar_data_referencia_financeira():
    data_inicio = datetime(2000, 1, 1)
    data_atual = datetime.now()
    diferenca = data_atual - data_inicio
    data_aleatoria = data_inicio + timedelta(days=random.randint(0, diferenca.days))
    dia = f"{data_aleatoria.day:02d}"
    mes = f"{data_aleatoria.month:02d}"
    ano = data_aleatoria.year
    return f"{dia}/{mes}/{ano}"

def gerar_valor_duas_casas_apos_virgula():
    valor_inteiro = random.randint(100, 999)
    valor_decimal = int(float(f"{random.random():.2f}") * 100)
    valor_final = f"{valor_inteiro}.{valor_decimal:02d}"
    return valor_final

# Page Object para operações com referência financeira em cadastro de cliente.
class GeneralRefFinance:
    def __init__(self, page: Page):
        self.page = page

    # Validar e clicar na aba Financeira, dentro de Referencias
    def click_empty(self):
        botao_financeira = self.page.locator('#menu_items_sec > .on')
        expect(botao_financeira).to_be_visible()
        expect(botao_financeira).not_to_have_attribute('disabled')
        self.page.route('**/views/cliente/refEtapaFinanceiraLista.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/refEtapaFinanceiraLista.html', timeout=40000)
        self.page.locator('#menu_items_sec > :nth-child(4)').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações da tela antes de adicionar qualquer coisa - aba referencia Financeira
    def validate_aba_empty(self):
        titulo_financeira = self.page.locator('h3')
        expect(titulo_financeira).to_be_visible()
        expect(titulo_financeira).to_have_text('Referências / Financeira')
        botao_adicionar = self.page.locator('.layout-align-end-end > .md-fab')
        expect(botao_adicionar).to_be_visible()
        expect(botao_adicionar).not_to_have_attribute('disabled')
        mensagem_nenhum_registro = self.page.locator('.text-align-center')
        expect(mensagem_nenhum_registro).to_be_visible()
        expect(mensagem_nenhum_registro).to_have_text('Não foi encontrado nenhum registro')
        botao_salvar = self.page.locator('.btn')
        expect(botao_salvar).to_be_visible()
        expect(botao_salvar).not_to_have_attribute('disabled')

    # Clicar no botão + para adicionar uma nova referencia Financeira
    def click_add_new(self):
        self.page.route('**/views/cliente/modalClienteRefFinanc.html', lambda route: route.continue_())
        response = self.page.wait_for_response('**/views/cliente/modalClienteRefFinanc.html', timeout=40000)
        self.page.locator('.layout-align-end-end > .md-fab').click()
        expect(response.ok()).to_be_truthy()

    # Validar informações do modal Referencia Financeira antes de preencher as informações
    def modal_empty(self):
        titulo_modal = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .flex')
        expect(titulo_modal).to_be_visible()
        expect(titulo_modal).to_have_text('Referência financeira')
        botao_fechar = self.page.locator('.md-dialog-fullscreen > ._md > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(botao_fechar).to_be_visible()
        expect(botao_fechar).not_to_have_attribute('disabled')
        icone_calendario = self.page.locator('.md-datepicker-button')
        expect(icone_calendario).to_be_visible()
        expect(icone_calendario).not_to_have_attribute('disabled')
        campo_inicio_exp_credito = self.page.locator('text=Início exp. crédito')
        expect(campo_inicio_exp_credito).to_be_visible()
        informativo_inicio_exp_credito = self.page.locator('label[for="txtIniExpCred"]')
        expect(informativo_inicio_exp_credito).to_have_text('Início exp. crédito')
        campo_local_experiencia = self.page.locator('#txtLocExp')
        expect(campo_local_experiencia).to_be_visible()
        expect(campo_local_experiencia).to_have_value('')
        expect(campo_local_experiencia).not_to_have_attribute('disabled')
        informativo_local_experiencia = self.page.locator('label[for="txtLocExp"]')
        expect(informativo_local_experiencia).to_have_text('Local Experiência')
        campo_plano_experiencia = self.page.locator('#txtPlExp')
        expect(campo_plano_experiencia).to_be_visible()
        expect(campo_plano_experiencia).to_have_value('')
        expect(campo_plano_experiencia).not_to_have_attribute('disabled')
        informativo_plano_experiencia = self.page.locator('label[for="txtPlExp"]')
        expect(informativo_plano_experiencia).to_have_text('Plano experiência')
        informativo_possui_cartao = self.page.locator('label[for="txtPossuiCartao"]')
        expect(informativo_possui_cartao).to_have_text('Possui cartão')
        campo_valor_prestacao = self.page.locator('#txtVlrPrest')
        expect(campo_valor_prestacao).to_be_visible()
        expect(campo_valor_prestacao).to_have_value('')
        expect(campo_valor_prestacao).not_to_have_attribute('disabled')
        informativo_valor_prestacao = self.page.locator('label[for="txtVlrPrest"]')
        expect(informativo_valor_prestacao).to_have_text('Valor prestação')
        botao_salvar_desabilitado = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar_desabilitado).to_be_visible()
        expect(botao_salvar_desabilitado).to_have_attribute('disabled')

    # Clicar para salvar Referencia Financeira
    def click_save(self):
        botao_salvar = self.page.locator('button:has-text("Salvar")')
        expect(botao_salvar).to_be_visible()
        botao_salvar_habilitado = self.page.locator('#btnModalAddRefPessoal')
        expect(botao_salvar_habilitado).to_be_visible()
        expect(botao_salvar_habilitado).not_to_have_attribute('disabled')
        botao_salvar_habilitado.click()

    # Mensagem Referencia Financeira incluída com sucesso
    def mess_ref_finance_added_sucess(self):
        card_sucesso = self.page.locator('.toast-success')
        expect(card_sucesso).to_be_visible()
        titulo_aviso = self.page.locator('.toast-success > .toast-title')
        expect(titulo_aviso).to_be_visible()
        expect(titulo_aviso).to_have_text('Aviso')
        mensagem_sucesso = self.page.locator('.toast-success > .toast-message')
        expect(mensagem_sucesso).to_be_visible()
        expect(mensagem_sucesso).to_have_text('Referência Financeira incluída com sucesso.')

    # Validar informações que foram adicionadas no cadastro de referencia Financeira
    def info_ref_finance_added(self):
        campo_data = self.page.locator('.flex-gt-sm-70 > :nth-child(1) > .ng-binding')
        expect(campo_data).to_be_visible()
        plano_experiencia = self.page.locator('[ng-show="(item.planoexperiencia)"]')
        expect(plano_experiencia).to_be_visible()
        local_experiencia = self.page.locator('[ng-show="(item.localexperiencia)"]')
        expect(local_experiencia).to_be_visible()
        valor_prestacao = self.page.locator('.layout-align-gt-sm-center-end > .list-title > b')
        expect(valor_prestacao).to_be_visible()
        quantidade_valor_prestacao = self.page.locator('.layout-align-gt-sm-center-end > .list-title')
        expect(quantidade_valor_prestacao).to_be_visible()