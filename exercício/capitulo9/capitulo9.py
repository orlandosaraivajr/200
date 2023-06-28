import pickle


def capitulo9_exercicio1(lista, *airlines):
    pass

def capitulo9_exercicio2(lista, *precos):
    pass

def capitulo9_exercicio3(lista, *cidades_origem):
    pass

def capitulo9_exercicio4(lista, *cidades_destino):
    pass

def capitulo9_exercicio5(lista, *nomes_pessoas):
    pass

def capitulo9_exercicio6(lista, *cpf_pessoas):
    pass

def capitulo9_exercicio7(lista, *dados_pessoais):
    pass

def capitulo9_exercicio8(lista, **dados_voo):
    pass

def capitulo9_exercicio9(lista, **dados_origem_voo):
    pass

def capitulo9_exercicio10(lista, **dados_destino_voo):
    pass

def capitulo9_exercicio11(lista2, *cpfs):
    pass

def capitulo9_exercicio12(lista2, *cpfs):
    pass

def capitulo9_exercicio13(lista2, *profissoes):
    pass

def capitulo9_exercicio14(lista2, *dominios):
    pass

def capitulo9_exercicio15(lista2, *trechos_nome):
    pass

def capitulo9_exercicio16(lista3, *trechos_nome):
    pass

def capitulo9_exercicio17(lista3, *emails):
    pass

def capitulo9_exercicio18(lista3, *trechos_endereco):
    pass

def capitulo9_exercicio19(lista, *validacoes):
    pass

def capitulo9_exercicio20(lista, *validacoes_ano):
    pass

if __name__ == "__main__":
    with open('../capitulo7.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    with open('../capitulo8.bin', 'rb') as list_in_file:
        lista2 = pickle.load(list_in_file)
    with open('../capitulo6.bin', 'rb') as list_in_file:
        lista3 = pickle.load(list_in_file)
#    capitulo9_exercicio1(lista)