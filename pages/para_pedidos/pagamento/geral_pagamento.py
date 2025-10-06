from ...gerarDados import umDiaAposHoje, trintaUmDiasAposHoje
from playwright.sync_api import expect, Page

# Page Object para ações gerais de pagamento.
class GeneralPayment:
    def __init__(self, page: Page):
        self.page = page

    #------------------- OUTROS -------------------

    # Carregamento de forma de pagamento, quando clicamos no botão Gerar parcelas
    def loading_form_payment(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        close_button = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button > .ng-binding')
        expect(close_button).to_be_visible()
        expect(close_button).not_to_be_disabled()

    #------------------- BOTÕES GERAR PARCELAS -------------------

    # Botão "GERAR PARCELAS"
    def click_generate_installments(self):
        self.page.route('POST', '/services/v3/pedido_forma_pagamento_lista', lambda route: route.fulfill())
        self.page.route('GET', '/views/carrinho/modalFormasPgto.html', lambda route: route.fulfill())
        gerar_parcelas_button = self.page.locator('.gerar-parcelas > .layout-wrap > [style="padding: 0 5px"] > .md-primary')
        gerar_parcelas_button.scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(gerar_parcelas_button).to_be_visible()
        expect(gerar_parcelas_button).to_have_text('Gerar parcelas')
        gerar_parcelas_button.click(force=True)
        self.page.wait_for_response(
            lambda response: '/services/v3/pedido_forma_pagamento_lista' in response.url and response.status == 200,
            timeout=40000
        )
        self.page.wait_for_response(
            lambda response: '/views/carrinho/modalFormasPgto.html' in response.url and response.status == 200,
            timeout=40000
        )

    # Botão "GERAR PARCELAS" quando alteramos a data de vencimento da 1
    def click_generate_install_alter_due(self):
        self.page.wait_for_timeout(2000)
        self.page.locator('.gerar-parcelas > .layout-wrap > [style="padding: 0 5px"] > .md-primary').click(force=True)

    #------------------- GERAR ENTRADA NO PAGAMENTO -------------------

    # Preencher pagamento entrada
    def choose_entry_form_payment(self):
        expect(self.page.locator('[ng-show="carrinho.getValorParcelamento() > 0"] > .btn-rounded > .layout-wrap > :nth-child(1) > md-list.md-default-theme > .padding-0 > .md-list-item-text > p')).to_be_visible()
        expect(self.page.locator('[ng-show="carrinho.getValorParcelamento() > 0"] > .btn-rounded > .layout-wrap > :nth-child(1) > md-list.md-default-theme > .padding-0 > .md-secondary-container > div > .ng-binding > sup')).to_be_visible()
        expect(self.page.locator('[ng-show="carrinho.getValorParcelamento() > 0"] > .btn-rounded > .layout-wrap > :nth-child(1) > md-list.md-default-theme > .padding-0 > .md-secondary-container > div > .ng-binding > sup')).to_have_text('R$')
        expect(self.page.locator('[ng-show="carrinho.getValorParcelamento() > 0"] > .btn-rounded > .layout-wrap > :nth-child(1) > md-list.md-default-theme > .padding-0 > .md-secondary-container > div > .ng-binding')).to_be_visible()

        button_dollar = self.page.locator('.layout-row.flex-100 > :nth-child(1) > .md-fab')
        expect(button_dollar).to_be_visible()
        expect(button_dollar).not_to_be_disabled()

        button_x = self.page.locator(':nth-child(3) > .md-fab')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()

        campo_maximo_parcela = self.page.locator('input.campoMoeda_totalEntrada')
        expect(campo_maximo_parcela).to_be_visible()
        campo_maximo_parcela.type('30000')

        self.page.locator('[flex="100"][ng-show="(exibeBoxFormasPgtoEntrada)"] > .md-primary > .md-toolbar-tools > .flex').click(force=True)
        self.page.locator('div.md-text.ng-binding', has_text='3861 - T.A. A Receber A Vista').click(force=True)

    # Validando e clicando no botão GERAR PAGAMENTO
    def click_generate_payment(self):
        gerar_pagamento_button = self.page.locator('.white > .layout-align-center-center > .md-primary')
        expect(gerar_pagamento_button).to_be_visible()
        expect(gerar_pagamento_button).not_to_be_disabled()
        expect(gerar_pagamento_button).to_have_text('Gerar pagamento')
        gerar_pagamento_button.click(force=True)

    #------------------- MODIFICAR PRIMEIRO DIA DE VENCIMENTO -------------------

    # No campo 1 vencimento, colocar o dia de amanhã para mudar as formas de pagamento
    def insert_date_tomorrow_1_due(self):
        data_hoje = umDiaAposHoje()
        self.page.locator('.gerar-parcelas > .layout-wrap').scroll_into_view_if_needed()
        self.page.wait_for_timeout(300)
        input_vencimento = self.page.locator('input', has_text='1º Vencimento')
        input_vencimento.clear()
        self.page.wait_for_timeout(200)
        input_vencimento.type(data_hoje)

    # No campo 1 vencimento, colocar 31 dias após a data de hoje
    def insert_date_31_days_1_due(self):
        data_31_dias = trintaUmDiasAposHoje()
        self.page.locator('.gerar-parcelas > .layout-wrap').scroll_into_view_if_needed()
        self.page.wait_for_timeout(300)
        input_vencimento_31_dias = self.page.locator('input', has_text='1º Vencimento')
        input_vencimento_31_dias.clear()
        self.page.wait_for_timeout(200)
        input_vencimento_31_dias.type(data_31_dias)