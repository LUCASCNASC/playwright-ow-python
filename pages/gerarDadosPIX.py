import random
import string

def gerarChavePixTelefone(ddd=44):
    numero = '9' + ''.join(str(random.randint(0,9)) for _ in range(8))
    return f"{ddd}{numero[:1]}{numero[1:5]}{numero[5:]}"

def gerarChavePixEmail():
    caracteres = string.ascii_lowercase + string.digits
    nomeUsuario = ''.join(random.choice(caracteres) for _ in range(10))
    return nomeUsuario + '@gmail.com'

def gerarChavePixCPF():
    def calcularDigito(digits):
        soma = sum(val * (len(digits) + 1 - idx) for idx, val in enumerate(digits))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    randomDigits = [random.randint(0, 9) for _ in range(9)]
    d1 = calcularDigito(randomDigits)
    d2 = calcularDigito(randomDigits + [d1])
    return ''.join(map(str, randomDigits + [d1, d2]))

def gerarChavePixAleatoria():
    caracteres = string.ascii_letters + string.digits
    chavePix = ''
    for i in range(4):
        grupo = ''.join(random.choice(caracteres) for _ in range(8))
        chavePix += grupo
        if i < 3:
            chavePix += '-'
    return chavePix

# Incorretas

def gerarChavePixTelefoneErrada():
    numero = random.randint(1000000000, 9999999999)
    return str(numero)

def gerarChavePixEmailErrada():
    caracteres = string.ascii_letters + string.digits
    resultado = ''.join(random.choice(caracteres) for _ in range(16))
    return resultado + '@'

def gerarChavePixCpfCnpjErrada():
    caracteres = string.ascii_letters + string.digits
    resultado = ''.join(random.choice(caracteres) for _ in range(16))
    return resultado + '@'

__all__ = [
    'gerarChavePixTelefone', 'gerarChavePixTelefoneErrada', 'gerarChavePixEmailErrada', 'gerarChavePixCpfCnpjErrada',
    'gerarChavePixEmail', 'gerarChavePixCPF', 'gerarChavePixAleatoria'
]