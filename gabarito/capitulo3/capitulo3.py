def capitulo3_exercicio1():
     nome = input("Qual o seu nome ? ")
     return nome

def capitulo3_exercicio2():
    nome = input("Qual o seu nome ? ")
    return 'Seu nome é ' + nome

def capitulo3_exercicio3():
    nome = input("Qual o seu nome ? ")
    idade = input("Qual a sua idade ? ")
    return nome + ' - ' + idade

def capitulo3_exercicio4():
    retorno = capitulo3_exercicio3()
    return retorno + ' anos'

def capitulo3_exercicio5():
    idade = int(input("Qual a sua idade ? "))
    if idade < 18:
        return True
    return False

def capitulo3_exercicio6():
    idade = int(input("Qual a sua idade ? "))
    return str(idade + 5)

def capitulo3_exercicio7():
    idade = capitulo3_exercicio6()
    return idade + ' anos'

def capitulo3_exercicio8(senha):
    senha_informada = input("Qual é a senha ? ")
    return senha == senha_informada

def capitulo3_exercicio9(senha):
    senha = senha.upper()
    senha_informada = input("Qual é a senha ? ")
    return senha == senha_informada.upper()

def capitulo3_exercicio10(texto_procurado):
    nome = input("Informe o nome completo ? ")
    return texto_procurado in nome

def capitulo3_exercicio11():
    return capitulo3_exercicio10('a')


def capitulo3_exercicio12():
    nome = input("Informe o nome completo: ")
    return nome == nome.upper()

def capitulo3_exercicio13():
    nome = input("Informe o nome completo: ")
    return nome == nome.lower()


def capitulo3_exercicio14():
    nome = input("Informe o nome completo: ")
    if len(nome.split(' ')) > 1:
        return 'Nome Composto'
    return 'Nome Simples'

def capitulo3_exercicio15():
    nome = input("Informe o nome completo: ")
    return nome[::-1]

def capitulo3_exercicio16():
    senha1 = input("Informe a senha: ")
    senha2 = input("Confirme a senha: ")
    if senha1 == senha2:
        return True
    return False

def capitulo3_exercicio17():
    if capitulo3_exercicio16():
        return 'Senhas são idênticas'
    return 'Senhas diferentes'

def capitulo3_exercicio18():
    senha_secreta = '123mudar'
    senha = input("Informe a senha: ")
    while senha != senha_secreta:
        senha = input("Informe a senha correta: ")
    return True

def capitulo3_exercicio19():
    nome = input("Informe o nome completo: ")
    vogais = 'AEIOUaeiou'
    if nome[0] in vogais:
        return True
    return False

def capitulo3_exercicio20():
    nome = input("Informe o nome completo: ")
    vogais = 'AEIOUaeiou'
    return nome[-1] in vogais