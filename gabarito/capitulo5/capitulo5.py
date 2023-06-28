def capitulo5_exercicio1(lista, valor):
    try:
        valor = float(valor)
    except ValueError:
        raise ValueError('Necessário digitar um número')
    lista.append(valor)
    return lista

def capitulo5_exercicio2(lista):
    try:
        valor = input("Digite número float")
        valor = float(valor)
    except ValueError:
        raise ValueError('Necessário digitar um número ponto-flutuante')
    lista.append(valor)
    return lista

def capitulo5_exercicio3(lista):
    lista_retorno = []
    for item in lista:
        if isinstance(item, int):
            lista_retorno.append(item)
    return lista_retorno

def capitulo5_exercicio4(lista, palavra):
    if isinstance(palavra, str):
        lista.append(palavra)
    return lista

def capitulo5_exercicio5(lista):
    return len(lista)

def capitulo5_exercicio6(lista):
    if isinstance(lista, list):
        return capitulo5_exercicio5(lista)
    raise TypeError('O argumento precisa ser lista')

def capitulo5_exercicio7(lista):
    if isinstance(lista, list):
        lista_retorno = []
        for item in lista:
            if isinstance(item, str):
                lista_retorno.append(item)
        return lista_retorno
    raise TypeError('O argumento precisa ser lista')

def capitulo5_exercicio8(lista):
    return capitulo5_exercicio6(capitulo5_exercicio7(lista))

def capitulo5_exercicio9(lista):
    if isinstance(lista, list):
        lista2 = capitulo5_exercicio3(lista)
        return sum(lista2)
    raise TypeError('O argumento precisa ser lista')

def capitulo5_exercicio10(lista):
    lista_retorno = []
    for item in lista:
        if isinstance(item, float):
            lista_retorno.append(item)
    return lista_retorno

def capitulo5_exercicio11(lista):
    lista1 = capitulo5_exercicio3(lista)
    lista2 = capitulo5_exercicio10(lista)
    lista_retorno =  lista1 + lista2
    return lista_retorno

def capitulo5_exercicio12(lista):
    lista1 = capitulo5_exercicio10(lista)
    lista2 = capitulo5_exercicio3(lista)
    lista_retorno =  lista1 + lista2
    return lista_retorno

def capitulo5_exercicio13(lista):
    if len(lista) > 2:
        lista_retorno = []
        lista_retorno.append(lista[0])
        lista_retorno.append(lista[-1])
        return lista_retorno
    return []

def capitulo5_exercicio14(lista):
    lista_retorno = []
    for item in lista:
        if isinstance(item, list):
            lista_retorno.append(item)
    return lista_retorno

def capitulo5_exercicio15(lista, palavra):
    return palavra in lista

def capitulo5_exercicio16(lista):
    if len(lista) > 5:
        item1 = lista[0]
        item4 = lista[3]
        item5 = lista[4]
        lista.remove(item1)
        lista.remove(item4)
        lista.remove(item5)
    return lista

def capitulo5_exercicio17(lista):
    return lista[-3::]

def capitulo5_exercicio18(lista):
    return lista[:-4:-1]

def capitulo5_exercicio19(lista):
    return lista[0:2]

def capitulo5_exercicio20(lista):
    # return lista[::-1]
    lista.reverse()
    return lista