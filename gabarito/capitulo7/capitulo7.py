import pickle


def capitulo7_exercicio1(lista, airline):
    sublista = []
    for item in lista:
        if item[1].get('airline').startswith(airline):
            sublista.append(item)
    return sublista

def capitulo7_exercicio2(lista, stops):
    stops = str(stops)
    sublista = []
    for item in lista:
        if str(item[1].get('stops')) == stops:
            sublista.append(item)
    return sublista

def capitulo7_exercicio3(lista, max_price=700):
    sublista = []
    for item in lista:
        if item[1].get('price') <= max_price:
            sublista.append(item)
    return sublista

def capitulo7_exercicio4(lista, min_price=100, max_price=700):
    sublista = []
    for item in lista:
        if item[1].get('price') >= min_price and item[1].get('price') <= max_price:
            sublista.append(item)
    return sublista

def capitulo7_exercicio5(lista, origin_city):
    sublista = []
    for item in lista:
        if item[1].get('origin').get('city') == origin_city:
            sublista.append(item)
    return sublista

def capitulo7_exercicio6(lista, destination_country):
    sublista = []
    for item in lista:
        if item[1].get('destination').get('country') == destination_country:
            sublista.append(item)
    return sublista

def capitulo7_exercicio7(lista, id):
    retorno = []
    try:
        retorno.append(lista[id][1].get('airline'))
        retorno.append(lista[id][1].get('origin').get('country'))
        retorno.append(lista[id][1].get('destination').get('country'))
    except IndexError:
        raise IndexError('ID não encontrado.')
    return tuple(retorno)

def capitulo7_exercicio8(lista, id):
    retorno = list(capitulo7_exercicio7(lista, id))
    retorno.append(len(lista[id][2]))
    return retorno

def capitulo7_exercicio9(lista, origin_iata):
    sublista = []
    for item in lista:
        if item[1].get('origin').get('iata') == origin_iata:
            sublista.append(item[0:2])
    return sublista

def capitulo7_exercicio10(lista, id):
    retorno = []
    try:
        retorno.append(lista[id][1].get('airline'))
        retorno.append(lista[id][1].get('destination'))
    except IndexError:
        raise IndexError('ID não encontrado.')
    return tuple(retorno)

def capitulo7_exercicio11(lista, id, cpf):
    try:
        lista_passageiros = lista[id][-1]
    except IndexError:
        raise IndexError('ID não encontrado.')
    for passageiro in lista_passageiros:
        if passageiro[-1] == cpf:
            return True
    return False

def capitulo7_exercicio12(lista, id, nome):
    try:
        lista_passageiros = lista[id][-1]
    except IndexError:
        raise IndexError('ID não encontrado.')
    for passageiro in lista_passageiros:
        if passageiro[0] == nome:
            return True
    return False

def capitulo7_exercicio13(lista, id, nome, cpf):
    try:
        lista_passageiros = lista[id][-1]
    except IndexError:
        raise IndexError('ID não encontrado.')
    for passageiro in lista_passageiros:
        if passageiro[0] == nome or passageiro[1] == cpf:
            return True
    return False

def capitulo7_exercicio14(lista, nome, cpf):
    lista_voo = []
    for voo in range(len(lista)):
        if capitulo7_exercicio13(lista, voo, nome, cpf):
            lista_voo.append(voo)
    return lista_voo

def capitulo7_exercicio15(lista, airline):
    lista_voo = []
    for voo in lista:
        if voo[1].get('airline') == airline:
            lista_voo.append(voo[0])
    return lista_voo

def capitulo7_exercicio16(lista, airline):
    lista_voo = []
    for voo in lista:
        if airline in voo[1].get('airline'):
            lista_voo.append(voo[0])
    return lista_voo

def capitulo7_exercicio17(lista, id):
    retorno = []
    try:
        retorno.append(id)
        retorno.append(lista[id][1].get('airline'))
        retorno.append(lista[id][1].get('origin').get('country'))
        retorno.append(lista[id][1].get('destination').get('country'))
    except IndexError:
        raise IndexError('ID não encontrado.')
    return set(retorno)

def capitulo7_exercicio18(lista, id):
    retorno = []
    try:
        retorno.append(id)
        retorno.append(lista[id][1].get('airline'))
        retorno.append(lista[id][1].get('origin').get('city'))
        retorno.append(lista[id][1].get('destination').get('city'))
    except IndexError:
        raise IndexError('ID não encontrado.')
    return set(retorno)

def capitulo7_exercicio19(lista, id):
    conjunto1 = capitulo7_exercicio17(lista, id)
    conjunto2 = capitulo7_exercicio18(lista, id)
    return conjunto1.union(conjunto2)

def capitulo7_exercicio20(lista, id_voo_1, id_voo_2 ):
    try:
        c1 = lista[id_voo_1][-1]
        c2 = lista[id_voo_2][-1]
    except IndexError:
        raise IndexError('ID não encontrado.')
    return list(c1.intersection(c2))

if __name__ == "__main__":
    with open('../capitulo7.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
#    capitulo7_exercicio1(lista)