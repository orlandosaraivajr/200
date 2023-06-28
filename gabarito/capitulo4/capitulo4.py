def capitulo4_exercicio1(numero1, numero2):
    try:
        numero3 = float(numero1) + float(numero2)
    except ValueError:
        raise ValueError('Necessário digitar um número')
    return int(numero3)

def capitulo4_exercicio2():
    try:
        numero1 = input("Digite o primeiro número ")
        numero1 = int(numero1)
        numero2 = input("Digite o segundo número ")
        numero2 = int(numero2)
    except ValueError:
        raise ValueError('Necessário digitar um número')
    return numero1 + numero2

def capitulo4_exercicio3(capital, i, juros):
    if juros <= 0 :
        raise ValueError('Juros precisa ser maior ou igual a zero')
    total_juros = capital * i * juros
    return total_juros

def capitulo4_exercicio4(capital, i, juros):
    if juros <= 0 :
        raise ValueError('Juros precisa ser maior ou igual a zero')
    if juros >= 1 :
        raise ValueError('Juros precisa ser menor que um')
    total_juros = capital * i * juros
    return total_juros

def capitulo4_exercicio5(numero1):
    try:
        numero1 = int(numero1)
    except:
        raise ValueError('Erro ao converter ' + str(numero1) + ' em inteiro')
    if numero1 <= 0 :
        return 0
    return numero1 * numero1 * numero1

def capitulo4_exercicio6(texto):
    if isinstance(texto, str):
        texto = texto.replace('a', '@').replace('e', '$')
        texto = texto.replace('i', 'Y')
        texto = texto.replace('o', '0')
        return texto
    raise TypeError('O argumento precisa ser string')

def capitulo4_exercicio7():
    try:
        idade = int(input("Qual a sua idade ? "))
    except:
        raise ValueError('Idade precisa ser número conversível para inteiro')
    if idade < 18:
        return True
    return False

def capitulo4_exercicio8(texto):
    try:
        return texto[::-1]
    except TypeError as e:
        return (e)

def capitulo4_exercicio9(numerador, denominador):
    try:
        numerador = float(numerador)
        denominador = float(denominador)
    except ValueError as e:
        return e
    try:
        return numerador / denominador
    except ZeroDivisionError as e:
        return e
        
def capitulo4_exercicio10(numerador, denominador):
    try:
        numerador = float(numerador)
        denominador = float(denominador)
        return numerador / denominador
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Não é divisível por zero.')
    except ValueError as e:
        raise ValueError('Erro ao converter argumentos.')

def capitulo4_exercicio11(valor):
    if valor < 0:
        raise ValueError("Valor menor que zero")
    if valor > 10:
        raise ValueError("Valor maior que dez")
    return valor

def capitulo4_exercicio12(nota1, nota2):
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
    except:
        raise TypeError("Argumento passado não é conversível para float")
    nota1 = capitulo4_exercicio11(nota1)
    nota2 = capitulo4_exercicio11(nota2)
    return (nota1 + nota2) / 2

def capitulo4_exercicio13(nota1, nota2 ):
    peso_nota1 = 1
    peso_nota2 = 2
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
    except:
        raise TypeError("Argumento passado não é conversível para float")
    nota1 = capitulo4_exercicio11(nota1)
    nota2 = capitulo4_exercicio11(nota2)
    MP = ((nota1 * peso_nota1) + (nota2 * peso_nota2)) / (peso_nota1 + peso_nota2 )
    return MP

def capitulo4_exercicio14(altura, peso):
    if peso < 50 or peso > 200:
        raise ValueError('Peso fora dos parâmetros (50 e 200)')
    if altura < 0.40 or altura > 2.10:
        raise ValueError('Altura fora dos parâmetros (0.40 e 2.10)')
    imc = peso / (altura * altura)
    return round(imc, 3)

def capitulo4_exercicio15(km_to_hour):
    if km_to_hour < 0.0 or km_to_hour > 100:
        raise ValueError('Kilometro fora dos parâmetros (0.0 e 100)')
    miles_to_hour = km_to_hour / 1.609344
    return miles_to_hour

def capitulo4_exercicio16(base, altura):
    if base < 0.0 or altura < 0.0:
        raise ValueError('Argumento não pode ser negativo')
    if base < altura:
        raise ValueError('Base não pode ser menor que a altura')
    area = base * altura / 2.0
    return area

def capitulo4_exercicio17(B, b, h):
    if B < 0.0 or b < 0.0 or h < 0.0:
        raise ValueError('Argumento não pode ser negativo')
    if B <= b:
        raise ValueError('Base maior não pode ser menor ou igual a base menor')
    area_trapezio = ((B + b) * h )/ 2
    return area_trapezio

def capitulo4_exercicio18(valor, porcentagem):
    if valor < 0.0:
        raise ValueError('Valor precisa ser positivo')
    if porcentagem <= 0.0 or porcentagem >= 1.0:
        raise ValueError('Porcentagem precisa estar entre 0 e 1')
    return valor * porcentagem

def capitulo4_exercicio19(valor):
    return valor - capitulo4_exercicio18(valor, 0.10)

def capitulo4_exercicio20(valor):
    return valor - capitulo4_exercicio18(valor, 0.15)