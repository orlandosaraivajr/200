import pickle 
         
def capitulo6_exercicio1(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR'):
            sublista.append(item)
    return sublista

def capitulo6_exercicio2(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR'):
            total = total + 1
    return total

def capitulo6_exercicio3(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DRA'):
            sublista.append(item[0])
    return sublista

def capitulo6_exercicio4(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR') and not item[0].upper().startswith('DRA'):
            sublista.append(item[0])
    return sublista

def capitulo6_exercicio5(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome in item[0]:
            sublista.append((item[0], item[1]))
    return sublista

def capitulo6_exercicio6(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome in item[0]:
            sublista.append((item[0], item[1]))
    return sublista[0:10]

def capitulo6_exercicio7(lista, email):
    for item in lista:
        if  item[2] == email:
            return item
    return ()

def capitulo6_exercicio8(lista, dominio='gmail.com'):
    sublista = []
    for item in lista:
        dominio_encontrado = item[2].split('@')
        if dominio == dominio_encontrado[1]:
            sublista.append(item)
    return sublista

def capitulo6_exercicio9(lista, username):
    sublista = []
    for item in lista:
        email_encontrado = item[2].split('@')
        if username == email_encontrado[0]:
            sublista.append(item)
    return sublista

def capitulo6_exercicio10(lista, trecho_endereco):
    sublista = []
    for item in lista:
        if trecho_endereco in item[3]:
            sublista.append(item)
    return sublista

def capitulo6_exercicio11(lista, estado):
    estado = estado.upper()
    sublista = []
    for item in lista:
        endereco = item[3]
        if endereco[-2:] == estado:
            sublista.append(item)
    return sublista

def capitulo6_exercicio12(lista, numero_cartao_procurado):
    sublista = []
    for item in lista:
        if numero_cartao_procurado in item[4]:
            sublista.append(item)
    return sublista

def capitulo6_exercicio13(lista, mes_ano_vencimento):
    sublista = []
    for item in lista:
        if mes_ano_vencimento == item[5]:
            sublista.append(item)
    return sublista

def capitulo6_exercicio14(lista, mes_vencimento):
    sublista = []
    for item in lista:
        if int(mes_vencimento) == int(item[5].split('/')[0]):
            sublista.append(item)
    return sublista

def capitulo6_exercicio15(lista, cpf):
    sublista = []
    for item in lista:
        if cpf == item[1]:
            sublista.append((item[0], item[1], item[2]))
    return sublista

def capitulo6_exercicio16(lista, estado, mes_vencimento):
    sublista = capitulo6_exercicio11(lista, estado)
    sublista = capitulo6_exercicio14(sublista, mes_vencimento)
    return sublista

def capitulo6_exercicio17(lista, trecho_endereco, sobrenome):
    sublista = capitulo6_exercicio10(lista, trecho_endereco)
    sublista = capitulo6_exercicio6(sublista, sobrenome)
    return sublista

def capitulo6_exercicio18(lista, dominio, estado ):
    sublista = capitulo6_exercicio8(lista, dominio)
    sublista = capitulo6_exercicio11(sublista, estado)
    return sublista

def capitulo6_exercicio19(lista, trecho_nome, trecho_cpf ):
    sublista = []
    for item in lista:
        cpf_no_item = item[1].replace('.','')
        cpf_no_item = cpf_no_item.replace('-','')
        if trecho_nome in item[0] and trecho_cpf in cpf_no_item:
            sublista.append(item)
    return sublista

def capitulo6_exercicio20(lista, estado, trecho_cpf ):
    sublista = []
    for item in capitulo6_exercicio11(lista, estado):
        cpf_no_item = item[1].replace('.','')
        cpf_no_item = cpf_no_item.replace('-','')
        if trecho_cpf in cpf_no_item:
            sublista.append(item)
    return sublista

if __name__ == "__main__":
    with open('../capitulo6.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    capitulo6_exercicio1(lista)


