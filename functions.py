import random
import string

def gerarSenha(comprimento=8, letras=True, numeros=True, especiais=True): #Função que irá gerar a senha aleatória
    caracteres = ''
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


#Funções de validação
def validarComprimento(comprimento):
    if not comprimento.isdigit():
        return False
    return True


def validarParametros(letras, numeros, especiais):
    if not isinstance(letras, bool) or not isinstance(numeros, bool) or not isinstance(especiais, bool):
        return False
    return True
