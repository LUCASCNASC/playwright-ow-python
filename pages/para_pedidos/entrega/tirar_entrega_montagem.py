from playwright.sync_api import expect, Page

# Page Object para ações de retirada/entrega de produtos (drag switch).
class ThrowDelivery:
    def __init__(self, page: Page):
        self.page = page

    # Arrasta botão de Retirada / Entrega do primeiro produto.
    def freight_first(self):
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-container').scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-container')).to_be_visible()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-container')).not_to_be_disabled()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-container > .md-thumb-container > .md-thumb')).to_be_visible()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-container > .md-thumb-container > .md-thumb')).not_to_be_disabled()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_be_visible()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).not_to_be_disabled()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_have_text(' Retirada / Entrega ')
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label').click(force=True)

    # Arrasta botão de Retirada / Entrega do segundo produto.
    def freight_second(self):
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label').scroll_into_view_if_needed()
        self.page.wait_for_timeout(300)
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_be_visible()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).not_to_be_disabled()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_have_text(' Retirada / Entrega ')
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label').click(force=True)

    # Arrasta botão de Retirada / Entrega do terceiro produto.
    def freight_third(self):
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label').scroll_into_view_if_needed()
        self.page.wait_for_timeout(300)
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_be_visible()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).not_to_be_disabled()
        expect(self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label')).to_have_text(' Retirada / Entrega ')
        self.page.locator('.valor.flex-gt-sm-50 > .md-checked > .md-label').click(force=True)

# Page Object para ações de montagem de produtos (drag switch).
class ThrowAssembly:
    def __init__(self, page: Page):
        self.page = page

    # Arrasta botão de Montagem do primeiro produto.
    def first(self):
        self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar')).to_be_visible()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar')).not_to_be_disabled()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-thumb-container > .md-thumb')).to_be_visible()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-thumb-container > .md-thumb')).not_to_be_disabled()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).to_be_visible()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).not_to_be_disabled()
        expect(self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).to_have_text(' Montagem ')
        self.page.locator('.produto-nome > .valor > .md-auto-horizontal-margin > .md-label').click(force=True)

    # Arrasta botão de Montagem do segundo produto.
    def second(self):
        self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar')).to_be_visible()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-bar')).not_to_be_disabled()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-thumb-container > .md-thumb')).to_be_visible()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-container > .md-thumb-container > .md-thumb')).not_to_be_disabled()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).to_be_visible()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).not_to_be_disabled()
        expect(self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-label')).to_have_text(' Montagem ')
        self.page.locator(':nth-child(3) > .md-whiteframe-2dp > :nth-child(3) > .produto-nome > .valor > .md-auto-horizontal-margin > .md-label').click(force=True)