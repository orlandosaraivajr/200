import pickle
import csv
from datetime import datetime

def capitulo10_exercicio1(lista, trecho_nome):
    sublista = []
    for item in lista:
        if trecho_nome in item[0]:
            sublista.append(item)
    return sublista

def capitulo10_exercicio2(lista, CPF):
    sublista = []
    for item in lista:
        if item[1] == CPF:
            sublista.append(item)
    return sublista

def capitulo10_exercicio3(lista, RG):
    sublista = []
    for item in lista:
        if item[2] == RG:
            sublista.append(item)
    return sublista

def capitulo10_exercicio4(lista, email):
    sublista = []
    for item in lista:
        if item[3] == email:
            sublista.append(item)
    return sublista

def capitulo10_exercicio5(lista, ip_1):
    sublista = []
    for item in lista:
        if ip_1 in item[4]:
            sublista.append(item)
    return sublista

def capitulo10_exercicio6(lista, ip_2):
    sublista = []
    for item in lista:
        if ip_2 in item[5]:
            sublista.append(item)
    return sublista

def capitulo10_exercicio7(lista, mac):
    sublista = []
    for item in lista:
        if mac in item[6]:
            sublista.append(item)
    return sublista

def capitulo10_exercicio8(lista, trecho_endereco):
    sublista = []
    for item in lista:
        if trecho_endereco in item[7]:
            sublista.append(item)
    return sublista

def capitulo10_exercicio9(lista, estado='SP'):
    sublista = []
    for item in lista:
        if item[7].endswith(estado):
            sublista.append(item)
    return sublista

def capitulo10_exercicio10(lista, dia, mes):
    sublista = []
    for item in lista:
        if item[8].month == mes and item[8].day == dia:
            sublista.append(item)
    return sublista

def capitulo10_exercicio11(lista, ano):
    sublista = []
    for item in lista:
        if item[8].year == ano:
            sublista.append(item)
    return sublista

def capitulo10_exercicio12(lista, dia, mes, ano):
    sublista = capitulo10_exercicio10(lista, dia, mes)
    sublista = capitulo10_exercicio11(sublista, ano)
    return sublista

def capitulo10_exercicio13(lista, trecho_endereco, ano):
    sublista = capitulo10_exercicio8(lista, trecho_endereco)
    sublista = capitulo10_exercicio11(sublista, ano)
    return sublista

def capitulo10_exercicio14(lista, ip1, ip2):
    sublista = capitulo10_exercicio5(lista, ip1)
    sublista = capitulo10_exercicio6(sublista, ip2)
    return sublista

def capitulo10_exercicio15(lista, mac, ip1, ip2):
    sublista = capitulo10_exercicio7(lista, mac)
    sublista = capitulo10_exercicio14(sublista, ip1, ip2)
    return sublista

def capitulo10_exercicio16(lista, mac, email):
    sublista = capitulo10_exercicio7(lista, mac)
    sublista = capitulo10_exercicio4(sublista, email)
    return sublista

def capitulo10_exercicio17(lista, trecho_nome, dominio_email):
    retorno = []
    sublista = capitulo10_exercicio1(lista, trecho_nome)
    for item in sublista:
        if item[3].endswith(dominio_email):
            retorno.append(item)
    return retorno

def capitulo10_exercicio18(lista, *email):
    retorno = []
    for item in email:
        retorno += capitulo10_exercicio4(lista, item)
    return retorno

def capitulo10_exercicio19(lista, *trecho_nomes):
    retorno = []
    for item in trecho_nomes:
        retorno += capitulo10_exercicio1(lista, item)
    return retorno

def capitulo10_exercicio20(lista, *cpf):
    retorno = []
    for item in cpf:
        retorno += capitulo10_exercicio2(lista, item)
    return retorno

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