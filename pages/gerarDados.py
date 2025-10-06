import random
import string
from datetime import datetime, timedelta

def gerarCNPJ():
    def randomDigits():
        return random.randint(0, 9)
    baseCNPJ = ''.join(str(randomDigits()) for _ in range(8))
    matriz = '0001'

    def calculateDigit(cnpj, position):
        if position == 1:
            weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(int(d) * w for d, w in zip(list(cnpj), weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    firstDigit = calculateDigit(baseCNPJ + matriz, 1)
    secondDigit = calculateDigit(baseCNPJ + matriz + str(firstDigit), 2)
    return f"{baseCNPJ[:2]}.{baseCNPJ[2:5]}.{baseCNPJ[5:8]}/{matriz}-{firstDigit}{secondDigit}"

def gerarCpf():
    def calcularDigito(digits):
        soma = sum(val * (len(digits) + 1 - idx) for idx, val in enumerate(digits))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    randomDigits = [random.randint(0, 9) for _ in range(9)]
    d1 = calcularDigito(randomDigits)
    d2 = calcularDigito(randomDigits + [d1])
    return ''.join(map(str, randomDigits + [d1, d2]))

def gerarEmailAleatorio():
    caracteres = string.ascii_lowercase + string.digits
    nomeUsuario = ''.join(random.choice(caracteres) for _ in range(10))
    return nomeUsuario + '@gmail.com'

def gerarNomeAleatorio():
    primeirosNomes = ['Ana', 'Carlos', 'João', 'Maria', 'Pedro', 'Beatriz', 'Lucas', 'Juliana', 'Rafael', 'Fernanda']
    sobrenomes = ['Silva', 'Oliveira', 'Santos', 'Pereira', 'Costa', 'Almeida', 'Rodrigues', 'Lima', 'Martins', 'Gomes']
    nome = random.choice(primeirosNomes)
    sobrenome = random.choice(sobrenomes)
    return f"{nome} {sobrenome}"

def gerarNomeEmpresa():
    prefixos = ['Tech', 'Global', 'Next', 'Mega', 'Prime', 'Super', 'Creative', 'Vision', 'Future', 'Eco']
    sufixos = ['Solutions', 'Systems', 'Group', 'Enterprises', 'Industries', 'Services', 'Corporation', 'Labs', 'Inc', 'Consulting']
    setores = ['Consulting', 'Development', 'Design', 'Marketing', 'Software', 'Digital', 'E-commerce', 'Security', 'Finance', 'Health']
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    setor = random.choice(setores)
    return f"{prefixo} {setor} {sufixo}"

def gerarTelefoneAleatorio():
    ddd = 44
    celular = '9' + ''.join(str(random.randint(0, 9)) for _ in range(8))
    return f"({ddd}) {celular[:5]}-{celular[5:]}"

def gerarRelacionamento(pessoa1=None, pessoa2=None):
    tiposRelacionamento = [
        "amigo", "namorada", "namorado", "esposa", "esposo", "mãe", "pai",
        "irmão", "irmã", "tia", "tio", "avó", "parente", "colega de trabalho",
        "ex-namorado(a)", "mentor(a)", "inimigos"
    ]
    return random.choice(tiposRelacionamento)

def gerarObservacao():
    palavras = [
        "amor", "vida", "felicidade", "sucesso", "trabalho", "amizade", "vontade",
        "carinho", "força", "esperança", "paz", "sabedoria", "confiança", "saúde",
        "alegria", "crescimento", "desafio", "sonhos", "coragem", "motivação", "Corinthians",
        "Futebol"
    ]
    frase = ""
    while len(frase) < 30:
        palavraAleatoria = random.choice(palavras)
        frase += palavraAleatoria + " "
    return frase.strip()[:30]

def umDiaAposHoje():
    today = datetime.today() + timedelta(days=1)
    return today.strftime('%d/%m/%Y')

def trintaUmDiasAposHoje():
    today = datetime.today() + timedelta(days=31)
    return today.strftime('%d/%m/%Y')

# Exports
__all__ = [
    'gerarCpf', 'gerarTelefoneAleatorio', 'gerarEmailAleatorio', 'gerarNomeAleatorio', 'gerarCNPJ', 'gerarNomeEmpresa',
    'gerarRelacionamento', 'gerarObservacao', 'umDiaAposHoje', 'trintaUmDiasAposHoje'
]