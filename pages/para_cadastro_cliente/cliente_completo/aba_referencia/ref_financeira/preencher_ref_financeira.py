from ...gerarDados import gerarNomeEmpresa
from datetime import datetime, timedelta
import random

# Início exp. crédito
def gerar_data_referencia_financeira():
    data_inicio = datetime(2000, 1, 1)
    data_atual = datetime.now()
    diferenca = data_atual - data_inicio
    data_aleatoria = data_inicio + timedelta(days=random.randint(0, diferenca.days))
    dia = f"{data_aleatoria.day:02d}"
    mes = f"{data_aleatoria.month:02d}"
    ano = data_aleatoria.year
    return f"{dia}/{mes}/{ano}"

# Valor prestação
def gerar_valor_duas_casas_apos_virgula():
    valor_inteiro = random.randint(100, 999)
    valor_decimal = int(float(f"{random.random():.2f}") * 100)
    valor_final = f"{valor_inteiro}.{valor_decimal:02d}"
    return valor_final

# Page Object para preencher campos de referência financeira no cadastro de cliente.
class FillRefFinance:
    def __init__(self, page):
        self.page = page

    # referência financeira - escolher Início exp. crédito
    def date_start(self):
        data_inicio = gerar_data_referencia_financeira()
        self.page.locator('text=Início exp. crédito').locator('..').locator('input').type(data_inicio)

    # referência financeira - escolher Local Experiencia
    def local_exp(self):
        local_experiencia = gerarNomeEmpresa()
        self.page.locator('#txtLocExp').type(local_experiencia)

    # referência financeira - escolher Plano experiencia
    def flat_exp(self):
        plano_experiencia = '444'
        self.page.locator('#txtPlExp').type(plano_experiencia)

    # referência financeira - escolher Valor prestação
    def value_prest(self):
        valor_prestacao = gerar_valor_duas_casas_apos_virgula()
        self.page.locator('#txtVlrPrest').type(valor_prestacao)