from playwright.sync_api import expect, Page
import re

# Page Object para produtos normais.
class Product:
    def __init__(self, page: Page):
        self.page = page

    def fisrt(self):
        self._search_and_intercept('1860', True)

    def second(self):
        self._search_and_intercept('1870', True)

    def kit_first(self):
        self._search_and_intercept('1862')

    def without_balance(self):
        self._search_and_intercept('1869')

    def cd_first(self):
        self._search_and_intercept('1880')

    def cd_second(self):
        self._search_and_intercept('1881', True, False)

    def remote_with_cd(self):
        self._search_and_intercept('1883')

    def remote_without_cd(self):
        self._search_and_intercept('1882')

    def round_up_down(self):
        self._search_and_intercept('1908')

    def discount_number(self):
        self._search_and_intercept('1912')

    def discount_percentage(self):
        self._search_and_intercept('1913')

    def discount_value_fixed(self):
        self._search_and_intercept('1914')

    def kit_discount(self):
        self._search_and_intercept('1909', True)

    def kit_remote(self):
        self._search_and_intercept('1915', True)

    def promo_match(self):
        self._search_and_intercept('1868')

    def promo_deadline_entry(self):
        self._search_and_intercept('1866')

    def promo_deadline_installment(self):
        self._search_and_intercept('1867')

    def first_installment_deadline(self):
        self._search_and_intercept('1891')

    def second_installment_deadline(self):
        self._search_and_intercept('1895')

    def third_installment_deadline(self):
        self._search_and_intercept('1893')

    def fourth_installment_deadline(self):
        self._search_and_intercept('1894')

    # Abstração para busca de produto, limpando campo se necessário.
    def _search_and_intercept(self, codigo_produto, limpar_campo=False, esperar_vazio=True):
        pattern = re.compile(f"/consultaprodutos/.*{codigo_produto}.*")
        self.page.route(pattern, lambda route: route.fulfill())
        api_consulta_produtos = self.page.wait_for_response(pattern)
        search_field = self.page.locator('#searchText')
        if limpar_campo:
            search_field.clear()
            self.page.wait_for_timeout(100)
            if esperar_vazio:
                expect(search_field).to_have_value('')
        expect(search_field).to_be_visible()
        expect(search_field).not_to_be_disabled()
        search_label = self.page.locator('label[for="searchText"]')
        expect(search_label).to_have_text('Buscar produtos')
        search_field.type(codigo_produto)
        self.page.wait_for_timeout(100)
        expect(search_field).to_have_value(codigo_produto)
        api_consulta_produtos