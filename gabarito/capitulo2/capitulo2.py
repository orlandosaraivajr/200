def capitulo2_exercicio1(texto):
    return texto.upper()


def capitulo2_exercicio2(texto):
    return texto.lower()


def capitulo2_exercicio3(texto):
    return texto.capitalize()


def capitulo2_exercicio4(texto):
    if texto.endswith('ando') or texto.endswith('endo') or texto.endswith('indo'):
        return True
    return False


def capitulo2_exercicio5(texto):
    return len(texto)


def capitulo2_exercicio6(texto):
    return texto.isdigit()


def capitulo2_exercicio7(texto_interno, texto):
    return texto_interno in texto


def capitulo2_exercicio8(texto_interno, texto):
    return texto_interno.upper() in texto.upper()


def capitulo2_exercicio9(texto):
    texto = str(texto)
    if texto.isdecimal():
        return bin(int(texto))
    return "Número inválido"


def capitulo2_exercicio10(texto):
    return texto.title()


def capitulo2_exercicio11(texto):
    texto = texto.replace('a', '@').replace('e', '$')
    texto = texto.replace('i', 'Y')
    texto = texto.replace('o', '0')
    return texto


def capitulo2_exercicio12(texto):
    texto = texto.lower()
    texto = capitulo2_exercicio11(texto)
    return texto


def capitulo2_exercicio13(texto):
    if len(texto) % 2 == 0:
        return texto.upper()
    return texto.lower()


def capitulo2_exercicio14(texto):
    return texto[::-1]


def capitulo2_exercicio15(texto):
    if texto == texto[::-1]:
        return True
    return False


def capitulo2_exercicio16(texto, remover_texto):
    return texto.replace(remover_texto, '')


def capitulo2_exercicio17(texto):
    return texto * 2


def capitulo2_exercicio18(texto):
    return texto.split(' ')[0]


def capitulo2_exercicio19(texto):
    return texto.split(' ')[-1]


def capitulo2_exercicio20(texto):
    caracteres_especial = '@#$&*'
    if len(texto) > 7:
        for caracter in caracteres_especial:
            if caracter in texto:
                return True
    return False
