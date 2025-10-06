from playwright.sync_api import expect, Page

# Page Object para seleção de formas de pagamento prestamista (abatimento %, valor fixo, origem serviço).
class ProcessReceiptPrest:
    def __init__(self, page: Page):
        self.page = page

    # ---------- Prestamista Abatimento % ----------

    # Seleciona forma de pagamento 3874 (T.A. A Receber Futuro - para Prestamista)
    def fut_with_fees_abat_percentage(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3874 - T.A. A Receber Futuro - para Prestamista').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3874 - T.A. A Receber Futuro - para Prestamista')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # Seleciona forma de pagamento 3875 (T.A.A Receber Presente CDCI - para Prestamista)
    def present_abat_percentage(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3875 - T.A.A Receber Presente CDCI - para Prestamista').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3875 - T.A.A Receber Presente CDCI - para Prestamista')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # Seleciona forma de pagamento 3876 (T.A. A Receber Futuro - para Prestamista sem juros)
    def fut_without_fees_abat_percentage(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3876 - T.A. A Receber Futuro - para Prestamista sem juros').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3876 - T.A. A Receber Futuro - para Prestamista sem juros')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # ---------- Prestamista Abatimento Valor Fixo ----------

    # Seleciona forma de pagamento 3880 (T.A. A Receb Fut com juros - Prest. Valor Fixo)
    def fut_with_fees_abat_vf(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3880 - T.A. A Receb Fut com juros - Prest. Valor Fixo').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3880 - T.A. A Receb Fut com juros - Prest. Valor Fixo')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # Seleciona forma de pagamento 3878 (T.A.A Receb Presente CDCI - Prest. Valor Fixo)
    def present_abat_vf(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3878 - T.A.A Receb Presente CDCI - Prest. Valor Fixo').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3878 - T.A.A Receb Presente CDCI - Prest. Valor Fixo')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # Seleciona forma de pagamento 3879 (T.A. A Receb Fut sem juros - Prest. Valor Fixo)
    def fut_without_fees_abat_vf(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3879 - T.A. A Receb Fut sem juros - Prest. Valor Fixo').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3879 - T.A. A Receb Fut sem juros - Prest. Valor Fixo')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)

    # ---------- Prestamista Abatimento Origem Serviço ----------

    # Seleciona forma de pagamento 3881 (T.A. A Receb Fut com juros - Prest. Origem Produto)
    def fut_with_fees_abat_os(self):
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .flex')).to_have_text('Forma de pagamento')
        button_x = self.page.locator('.md-dialog-fullscreen > .md-primary > .md-toolbar-tools > .md-icon-button')
        expect(button_x).to_be_visible()
        expect(button_x).not_to_be_disabled()
        self.page.locator('text=3881 - T.A. A Receb Fut com juros - Prest. Origem Produto').scroll_into_view_if_needed()
        pagamento_option = self.page.locator('text=3881 - T.A. A Receb Fut com juros - Prest. Origem Produto')
        expect(pagamento_option).to_be_visible()
        expect(pagamento_option).not_to_be_disabled()
        self.page.route('POST', '/services/v3/pedido_forma_pagamento', lambda route: route.fulfill())
        pagamento_option.click(force=True)
        self.page.wait_for_response(lambda response: '/services/v3/pedido_forma_pagamento' in response.url and response.status == 200, timeout=40000)