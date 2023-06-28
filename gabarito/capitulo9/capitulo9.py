import pickle


def capitulo9_exercicio1(lista, *airlines):
    sublista = []
    for airline in airlines:
        for item in lista:
            if item[1].get('airline').startswith(airline):
                sublista.append(item)
    return sublista

def capitulo9_exercicio2(lista, *precos):
    sublista = []
    for preco in precos:
        for item in lista:
            if item[1].get('price') == preco:
                sublista.append(item)
    return sublista

def capitulo9_exercicio3(lista, *cidades_origem):
    sublista = []
    for cidade in cidades_origem:
        for item in lista:
            if item[1].get('origin').get('city') == cidade:
                sublista.append(item)
    return sublista

def capitulo9_exercicio4(lista, *cidades_destino):
    sublista = []
    for cidade in cidades_destino:
        for item in lista:
            if item[1].get('destination').get('city') == cidade:
                sublista.append(item)
    return sublista

def capitulo9_exercicio5(lista, *nomes_pessoas):
    sublista = []
    for item in lista:
        for passageiro in item[2]:
            for nome in nomes_pessoas:
                if passageiro[0] == nome:
                    sublista.append(item[0])
    return sublista

def capitulo9_exercicio6(lista, *cpf_pessoas):
    sublista = []
    for item in lista:
        for passageiro in item[2]:
            for cpf in cpf_pessoas:
                if passageiro[1] == cpf:
                    sublista.append(item[0])
    return sublista

def capitulo9_exercicio7(lista, *dados_pessoais):
    sublista = []
    for item in lista:
        for passageiro in item[2]:
            for dados in dados_pessoais:
                if  passageiro[0] == dados or passageiro[1] == dados:
                    sublista.append(item[0])
    return sublista

def capitulo9_exercicio8(lista, **dados_voo):
    sublista = []
    for dados in dados_voo:
        for item in lista:
            if item[1].get(dados) == dados_voo[dados]:
                sublista.append(item[0])
    return tuple(sublista)

def capitulo9_exercicio9(lista, **dados_origem_voo):
    sublista = []
    for dados in dados_origem_voo:
        for item in lista:
            if item[1].get('origin').get(dados) == dados_origem_voo[dados]:
                sublista.append(item[0])
    return tuple(sublista)

def capitulo9_exercicio10(lista, **dados_destino_voo):
    sublista = []
    for dados in dados_destino_voo:
        for item in lista:
            if item[1].get('destination').get(dados) == dados_destino_voo[dados]:
                sublista.append(item[0])
    return tuple(sublista)

def capitulo9_exercicio11(lista2, *cpfs):
    lista_retorno = []
    for cpf in cpfs:
        for item in lista2:
            if item[1][1] == cpf:
                lista_retorno.append(item[0])
    return lista_retorno

def capitulo9_exercicio12(lista2, *cpfs):
    lista_retorno = []
    for cpf in cpfs:
        for item in lista2:
            if item[1][1] == cpf:
                lista_retorno.append(item[1][0])
    return lista_retorno

def capitulo9_exercicio13(lista2, *profissoes):
    lista_retorno = []
    for profissao in profissoes:
        for item in lista2:
            if item[1][2] == profissao:
                lista_retorno.append(item[1][0] +'-'+item[1][2])
    return lista_retorno

def capitulo9_exercicio14(lista2, *dominios):
    lista_retorno = []
    for dominio in dominios:
        for item in lista2:
            if item[1][3].endswith(dominio):
                lista_retorno.append(item[1][0] +'-'+item[1][3])
    return lista_retorno

def capitulo9_exercicio15(lista2, *trechos_nome):
    lista_retorno = []
    for trecho_nome in trechos_nome:
        for item in lista2:
            if trecho_nome in item[1][0]:
                lista_retorno.append(item[1][0] +'-'+item[1][3])
    return lista_retorno

def capitulo9_exercicio16(lista3, *trechos_nome):
    lista_retorno = []
    for trecho_nome in trechos_nome:
        for item in lista3:
            if trecho_nome in item[0]:
                lista_retorno.append(item[0] + ' ' + item[1])
    return lista_retorno

def capitulo9_exercicio17(lista3, *emails):
    lista_retorno = []
    for email in emails:
        for item in lista3:
            if item[2] == email:
                lista_retorno.append(item[0] + ' ' + item[1])
    return lista_retorno

def capitulo9_exercicio18(lista3, *trechos_endereco):
    lista_retorno = []
    for trecho in trechos_endereco:
        for item in lista3:
            if trecho in item[3]:
                lista_retorno.append(item)
    return lista_retorno

def capitulo9_exercicio19(lista, *validacoes):
    lista_retorno = []
    for validacao in validacoes:
        for item in lista:
            if validacao == item[5]:
                lista_retorno.append(item)
    return lista_retorno

def capitulo9_exercicio20(lista, *validacoes_ano):
    lista_retorno = []
    for validacao in validacoes_ano:
        validacao = str(validacao)
        for item in lista:
            validacao_ano = item[5].split('/')[1]
            if validacao == validacao_ano:
                lista_retorno.append(item)
    return lista_retorno

if __name__ == "__main__":
    with open('../capitulo7.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    with open('../capitulo8.bin', 'rb') as list_in_file:
        lista2 = pickle.load(list_in_file)
    with open('../capitulo6.bin', 'rb') as list_in_file:
        lista3 = pickle.load(list_in_file)
#    capitulo9_exercicio1(lista)