def capitulo1_exercicio1(numero1, numero2):
    numero_calculado = numero1 + numero2
    return numero_calculado

def capitulo1_exercicio2(numero1, numero2):
        numero_calculado = 3 * numero1 + numero2
        return numero_calculado

def capitulo1_exercicio3(numero1, numero2):
    numero_calculado = 3 * numero1 + numero2
    if numero_calculado <= 0:
        return 0
    return numero_calculado

def capitulo1_exercicio4(numero1):
    if numero1 <= 0 :
        return 0
    return numero1 * numero1 * numero1

def capitulo1_exercicio5(base, altura):
    area = base * altura / 2.0
    return area

def capitulo1_exercicio6(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

def capitulo1_exercicio7(capital, i, juros):
    total_juros = capital * i * juros
    return total_juros

def capitulo1_exercicio8(capital, i, juros):
    total = capital + capitulo1_exercicio7(capital, i, juros)
    return total

def capitulo1_exercicio9(capital, i, juros):
    total_juros = capital * (1+ juros) ** i
    return total_juros

def capitulo1_exercicio10(capital, i, juros):
    return capitulo1_exercicio9(capital, i, juros) - capital

def capitulo1_exercicio11(km_to_hour):
    miles_to_hour = km_to_hour * 0.621371
    miles_to_hour = km_to_hour / 1.609344
    return miles_to_hour

def capitulo1_exercicio12(km_to_hour):
    meter_per_second = km_to_hour / 3.6
    return meter_per_second

def capitulo1_exercicio13(altura, peso):
    imc = peso / (altura * altura)
    return imc

def capitulo1_exercicio14(N1, N2):
    P1 = 1
    P2 = 2
    MP = ((N1 * P1) + (N2 * P2)) / (P1 + P2 )
    return MP

def capitulo1_exercicio15(N1, N2, N3):
    P1 = 1
    P2 = 1
    P3 = 2
    MP = ((N1 * P1) + (N2 * P2) + (N3 * P3)) / (P1 + P2 + P3)
    return MP

def capitulo1_exercicio16(N1, N2, N3, N4):
    P1 = 1
    P2 = 1
    P3 = 2
    P4 = 3
    MP = ((N1 * P1) + (N2 * P2) + (N3 * P3) + (N4 * P4)) / (P1 + P2 + P3 + P4)
    return MP

def capitulo1_exercicio17(N1, N2, N3, N4):
    if capitulo1_exercicio16(N1, N2, N3, N4) > 5.0:
        return True
    return False

def capitulo1_exercicio18(N1):
    if (N1 % 2) == 0:
        return True
    else:
        return False

def capitulo1_exercicio19(N1):
    if (N1 % 10) == 0:
        return True
    return False

def capitulo1_exercicio20(N1):
    if (N1 % 3) == 0 and (N1 % 5) == 0:
        return True
    return False