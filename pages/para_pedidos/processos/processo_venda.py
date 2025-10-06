from playwright.sync_api import expect, Page

# Page Object para seleção do processo de venda (NFe/NFCe).
class ProcessSale:
    def __init__(self, page: Page):
        self.page = page

    # ------------------- PROCESSOS NFe -------------------

    # Escolhe processo de venda 9860 NFe.
    def nfe(self):
        select_icon = self.page.locator('#select_value_label_4 > .md-select-icon')
        expect(select_icon).to_be_visible()
        expect(select_icon).not_to_be_disabled