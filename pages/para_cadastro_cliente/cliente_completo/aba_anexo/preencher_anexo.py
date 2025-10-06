from playwright.sync_api import Page

# Page Object para anexar arquivo PDF ao cadastro de cliente completo.
class FillFieldAnexo:
    def __init__(self, page: Page):
        self.page = page

    # Função para anexar arquivo dentro do cadastro de cliente completo.
    def file_pdf(self):
        caminho_do_arquivo = 'cypress/fixtures/anexo_cadastro_cliente_completo.pdf'
        self.page.set_input_files("[type='file']", caminho_do_arquivo)