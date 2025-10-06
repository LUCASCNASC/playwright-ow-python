from playwright.sync_api import expect, Page
import re

# Page Object para produtos exclusivos.
class ProductExclusiva:
    def __init__(self, page: Page):
        self.page = page

    def first_normal(self):
        self._search_and_intercept('1896')

    def kit_without_balance_scheduling(self):
        self._search_and_intercept('1900', True)

    def kit_volumes(self):
        self._search_and_intercept('1903', True)

    def balance_receive(self):
        self._search_and_intercept('1905')

    def balance_receive_two_lines(self):
        self._search_and_intercept('1906')

    # Abstração para busca de produto, limpando campo se necessário.
    def _search_and_intercept(self, codigo_produto, limpar_campo=False):
        pattern = re.compile(f"/consultaprodutos/.*{codigo_produto}.*")
        self.page.route(pattern, lambda route: route.fulfill())
        api_consulta_produtos = self.page.wait_for_response(pattern)
        search_field = self.page.locator('#searchText')
        if limpar_campo:
            search_field.clear()
            self.page.wait_for_timeout(100)
            expect(search_field).to_have_value('')
        expect(search_field).to_be_visible()
        expect(search_field).not_to_be_disabled()
        search_label = self.page.locator('label[for="searchText"]')
        expect(search_label).to_have_text('Buscar produtos')
        search_field.type(codigo_produto)
        self.page.wait_for_timeout(100)
        expect(search_field).to_have_value(codigo_produto)
        api_consulta_produtos