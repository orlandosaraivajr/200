import pickle 
         
def capitulo6_exercicio1(lista):
    pass

def capitulo6_exercicio2(lista):
    pass

def capitulo6_exercicio3(lista):
    pass

def capitulo6_exercicio4(lista):
    pass

def capitulo6_exercicio5(lista, sobrenome):
    pass

def capitulo6_exercicio6(lista, sobrenome):
    pass

def capitulo6_exercicio7(lista, email):
    pass

def capitulo6_exercicio8(lista, dominio='gmail.com'):
    pass

def capitulo6_exercicio9(lista, username):
    pass

def capitulo6_exercicio10(lista, trecho_endereco):
    pass

def capitulo6_exercicio11(lista, estado):
    pass

def capitulo6_exercicio12(lista, numero_cartao_procurado):
    pass

def capitulo6_exercicio13(lista, mes_ano_vencimento):
    pass

def capitulo6_exercicio14(lista, mes_vencimento):
    pass

def capitulo6_exercicio15(lista, cpf):
    pass

def capitulo6_exercicio16(lista, estado, mes_vencimento):
    pass

def capitulo6_exercicio17(lista, trecho_endereco, sobrenome):
    pass

def capitulo6_exercicio18(lista, dominio, estado ):
    pass

def capitulo6_exercicio19(lista, trecho_nome, trecho_cpf ):
    pass

def capitulo6_exercicio20(lista, estado, trecho_cpf ):
    pass

if __name__ == "__main__":
    with open('../capitulo6.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    capitulo6_exercicio1(lista)


