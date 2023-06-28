import pickle
import csv
from datetime import datetime

def capitulo10_exercicio1(lista, trecho_nome):
    pass

def capitulo10_exercicio2(lista, CPF):
    pass

def capitulo10_exercicio3(lista, RG):
    pass

def capitulo10_exercicio4(lista, email):
    pass

def capitulo10_exercicio5(lista, ip_1):
    pass

def capitulo10_exercicio6(lista, ip_2):
    pass

def capitulo10_exercicio7(lista, mac):
    pass

def capitulo10_exercicio8(lista, trecho_endereco):
    pass

def capitulo10_exercicio9(lista, estado='SP'):
    pass

def capitulo10_exercicio10(lista, dia, mes):
    pass

def capitulo10_exercicio11(lista, ano):
    pass

def capitulo10_exercicio12(lista, dia, mes, ano):
    pass

def capitulo10_exercicio13(lista, trecho_endereco, ano):
    pass

def capitulo10_exercicio14(lista, ip1, ip2):
    pass

def capitulo10_exercicio15(lista, mac, ip1, ip2):
    pass

def capitulo10_exercicio16(lista, mac, email):
    pass

def capitulo10_exercicio17(lista, trecho_nome, dominio_email):
    pass

def capitulo10_exercicio18(lista, *email):
    pass

def capitulo10_exercicio19(lista, *trecho_nomes):
    pass

def capitulo10_exercicio20(lista, *cpf):
    pass

def capitulo10_writer_csv(nome_arquivo = 'a.csv', lista=[]):
    colunas = ['Nome','CPF','RG','e-mail','IP privado','IP público', 'MAC', 'Endereço','Nascimento']
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(colunas)
        for item in lista:
            writer.writerow(item)

    
if __name__ == "__main__":
    with open('../capitulo10.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)


'''
    dados1 = capitulo10_exercicio19(lista, 'Pereira','Pires','Silva')
    capitulo10_writer_csv('dados1.csv', dados1)
    dados2 = capitulo10_exercicio20(lista, '359.860.214-60','869.305.472-47')
    capitulo10_writer_csv('dados2.csv', dados2)
'''