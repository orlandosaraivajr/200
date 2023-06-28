import pickle
from datetime import datetime

def capitulo8_exercicio1(lista, nome_completo):
    sublista = []
    for item in lista:
        if item[1][0] == nome_completo:
            sublista.append(item)
    return sublista

def capitulo8_exercicio2(lista, trecho_nome):
    sublista = []
    for item in lista:
        if trecho_nome in item[1][0]:
            sublista.append(item)
    return sublista

def capitulo8_exercicio3(lista, mes):
    sublista = []
    for item in lista:
        if item[2].month == mes:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio4(lista, dia):
    sublista = []
    for item in lista:
        if item[2].day == dia:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio5(lista, dia, mes):
    '''
    x1 = capitulo8_exercicio3(lista, mes)
    x2 = capitulo8_exercicio4(lista, dia)
    return x1.intersection(x2)
    '''
    sublista = []
    for item in lista:
        if item[2].month == mes and item[2].day == dia:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio6(lista, dia, mes):
    sublista = []
    for item in lista:
        if item[3].month == mes and item[3].day == dia:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio7(lista, dia, mes):
    sublista = []
    for item in lista:
        if item[4].month == mes and item[4].day == dia:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio8(lista, dia, mes):
    sublista = []
    for item in lista:
        if item[5].month == mes and item[5].day == dia:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio9(lista, diferenca_dias):
    sublista = []
    for item in lista:
        diff_dias = item[3] - item[2]
        if diff_dias.days <= diferenca_dias:
            sublista.append(item[0])
    return set(sublista)

def capitulo8_exercicio10(lista):
    sublista = []
    for item in lista:
        if item[3].isoweekday() >= 6:
            sublista.append(item[0])
    return set(sublista)


def capitulo8_exercicio11(lista, indice):
    sublista = []
    try:
        for item in lista:
            if item[indice].hour > 18 or item[indice].hour < 6:
                sublista.append(item)
    except IndexError:
        raise IndexError('ID não encontrado.')
    except AttributeError:
        raise AttributeError('Campo datetime não encontrado.')
    return sublista

def capitulo8_exercicio12(lista):
    sublista = capitulo8_exercicio11(lista, 2)
    return sublista

def capitulo8_exercicio13(lista):
    sublista = capitulo8_exercicio11(lista, 2)
    sublista = capitulo8_exercicio11(sublista, 3)
    return sublista


def capitulo8_exercicio14(lista):
    sublista = capitulo8_exercicio11(lista, 2)
    sublista = capitulo8_exercicio11(sublista, 3)
    sublista = capitulo8_exercicio11(sublista, 4)
    sublista = capitulo8_exercicio11(sublista, 5)
    return sublista


def capitulo8_exercicio15(lista, estado='SP'):
    lista_retorno = []
    sublista = capitulo8_exercicio11(lista, 2)
    for item in sublista:
        if item[1][-1].endswith(estado):
            lista_retorno.append(item)
    return lista_retorno

def capitulo8_exercicio16(lista, estado='SP'):
    sublista = capitulo8_exercicio15(lista, estado)
    retorno = []
    for item in sublista:
        retorno.append((item[0], item[1][0], item[1][1]))
    return retorno

def capitulo8_exercicio17(lista, mes, estado='MG'):
    retorno = []
    for item in lista:
        if item[2].month == mes and item[1][-1].endswith(estado):
            retorno.append((item[1][0],item[1][2],item[1][-1],item[2]))
    return retorno

def capitulo8_exercicio18(lista, dia, mes):
    retorno = []
    for item in lista:
        if item[2].day == dia and item[2].month == mes:
            retorno.append(item)
    return retorno

def capitulo8_exercicio19(lista, id):
    try:
        return(lista[id][0],lista[id][2],lista[id][3],lista[id][4],lista[id][5])
    except IndexError:
        return ()

def capitulo8_exercicio20(lista, id ):
    try:
        return(lista[id][0],lista[id][2],lista[id][3],lista[id][4],lista[id][5])
    except IndexError:
        raise IndexError('ID não encontrado.')

if __name__ == "__main__":
    with open('../capitulo8.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
