from playwright.sync_api import expect, Page
import re

# Page Object para produtos prestamista promocionais.
class ProductPromo:
    def __init__(self, page: Page):
        self.page = page

    def term_installment_prest(self):
        self._search_and_intercept('1918', True)

    def second_term_installment_prest(self):
        self._search_and_intercept('1919', True)

    def match_prest(self):
        self._search_and_intercept('1920', True)

    def third_term_installment_prest(self):
        self._search_and_intercept('1921', True)

    def term_fisrt_prest_abat_vf(self):
        self._search_and_intercept('1922', True)

    def term_second_prest_abat_vf(self):
        self._search_and_intercept('1923', True)

    def term_third_prest_abat_vf(self):
        self._search_and_intercept('1924', True)

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