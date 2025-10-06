from playwright.sync_api import expect, Page

# Classe utilitária para validação de URLs de rotas.
class ValidateURL:
    def __init__(self, page: Page):
        self.page = page

    def url_departamentos(self):
        expect(self.page).to_have_url(r'/\/#!\/departamentos\//')

    def url_servicos(self):
        expect(self.page).to_have_url(r'/\/#!\/servicos/')

    def url_pedidos_pendentes(self):
        expect(self.page).to_have_url(r'/\/#!\/vendedor\/pedidos/')

    def url_cliente(self):
        expect(self.page).to_have_url(r'/\/#!\/cliente\/cliente-cadastro/')

    def url_cliente_completo(self):
        expect(self.page).to_have_url(r'/\/#!\/clienteCompleto/')

    def url_pos_venda(self):
        expect(self.page).to_have_url(r'/\/#!\/posvenda/')

    def url_intencao_compra(self):
        expect(self.page).to_have_url(r'/\/#!\/intencoescompra/')

    def url_configuracoes(self):
        expect(self.page).to_have_url(r'/\/#!\/customizacao/')

    def url_minha_performance(self):
        expect(self.page).to_have_url(r'/\/#!\/vendedor/')