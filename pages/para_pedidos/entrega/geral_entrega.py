from playwright.sync_api import expect, Page

# Page Object para operações gerais de entrega, rotas e inconsistências.
class GeneralDelivery:
    def __init__(self, page: Page):
        self.page = page

    # Clica no campo transportadora e escolhe a transportadora.
    def choose_transporter(self):
        self.page.locator('.progressbar').scroll_into_view_if_needed()
        self.page.wait_for_timeout(200)
        self.page.locator('[name="transportadora"]').click(force=True)
        self.page.wait_for_timeout(300)
        self.page.locator('span[md-highlight-text="transpAutoCompleteSearchText"]', has_text='1').click()

    # Escolhe rota completa, rota Maringá.
    def choose_route(self):
        self.page.locator('.rota-frete > .md-icon-right > .ng-binding').scroll_into_view_if_needed()
        self.page.locator('.rota-frete > .md-icon-right > .ng-binding').click(force=True)
        self.page.wait_for_timeout(400)
        self.page.locator('#txtBuscaRotaModal').type('1')
        self.page.locator('md-icon[ng-click="pesquisar()"]').click()
        self.page.wait_for_timeout(400)
        self.page.locator('v-pane-header.ng-scope > div').click()
        self.page.locator(':nth-child(4) > .padding-10-0').click()
        self.page.wait_for_timeout(200)

    # Valida card de inconsistências - rota e transportadora.
    def modal_incons_route_transporter(self):
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_have_text('Inconsistências')
        expect(self.page.locator(':nth-child(1) > h3')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > h3')).to_have_text('Restriçoes geradas (triais), por favor comunique à seu gerente:')
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_be_visible()
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_have_text('Processo de venda')
        expect(self.page.locator(':nth-child(1) > .md-avatar-icon')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-list-item-text > .no-truncate')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > .md-list-item-text > .no-truncate')).to_have_text('A Rota é obrigatória.')
        expect(self.page.locator(':nth-child(1) > .md-avatar-icon')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-list-item-text > .no-truncate')).to_be_visible()
        expect(self.page.locator(':nth-child(2) > .md-list-item-text > .no-truncate')).to_have_text('Pedidos referêntes a NFC-e com definição de entrega deverão possuir entidade transportadora preenchida, favor verificar.')
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_be_disabled()
        self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding').click(force=True)

    # Valida card de inconsistências - apenas transportadora.
    def modal_incons_only_transporter(self):
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_have_text('Inconsistências')
        expect(self.page.locator(':nth-child(1) > h3')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > h3')).to_have_text('Restriçoes geradas (triais), por favor comunique à seu gerente:')
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_be_visible()
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_have_text('Processo de venda')
        expect(self.page.locator('.md-avatar-icon')).to_be_visible()
        expect(self.page.locator('.no-truncate')).to_be_visible()
        expect(self.page.locator('.no-truncate')).to_have_text('Pedidos referêntes a NFC-e com definição de entrega deverão possuir entidade transportadora preenchida, favor verificar.')
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_be_disabled()
        self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding').click(force=True)

    # Valida card de inconsistências - apenas rota.
    def modal_incons_only_route(self):
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .flex')).to_have_text('Inconsistências')
        expect(self.page.locator(':nth-child(1) > h3')).to_be_visible()
        expect(self.page.locator(':nth-child(1) > h3')).to_have_text('Restriçoes geradas (triais), por favor comunique à seu gerente:')
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_be_visible()
        expect(self.page.locator('.ng-scope.flex-100 > .md-primary > .md-toolbar-tools > h2')).to_have_text('Processo de venda')
        expect(self.page.locator('.md-avatar-icon')).to_be_visible()
        expect(self.page.locator('.no-truncate')).to_be_visible()
        expect(self.page.locator('.no-truncate')).to_have_text('A Rota é obrigatória.')
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).to_be_visible()
        expect(self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding')).not_to_be_disabled()
        self.page.locator('.md-dialog-fullscreen > :nth-child(1) > .md-toolbar-tools > .md-icon-button > .ng-binding').click(force=True)