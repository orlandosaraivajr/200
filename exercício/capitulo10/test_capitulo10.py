from capitulo10  import capitulo10_exercicio1
from capitulo10  import capitulo10_exercicio2
from capitulo10  import capitulo10_exercicio3
from capitulo10  import capitulo10_exercicio4
from capitulo10  import capitulo10_exercicio5
from capitulo10  import capitulo10_exercicio6
from capitulo10  import capitulo10_exercicio7
from capitulo10  import capitulo10_exercicio8
from capitulo10  import capitulo10_exercicio9
from capitulo10  import capitulo10_exercicio10
from capitulo10  import capitulo10_exercicio11
from capitulo10  import capitulo10_exercicio12
from capitulo10  import capitulo10_exercicio13
from capitulo10  import capitulo10_exercicio14
from capitulo10  import capitulo10_exercicio15
from capitulo10  import capitulo10_exercicio16
from capitulo10  import capitulo10_exercicio17
from capitulo10  import capitulo10_exercicio18
from capitulo10  import capitulo10_exercicio19
from capitulo10  import capitulo10_exercicio20

import pickle
import pytest
from datetime import datetime

class LoadData: 
    def load_list(self):
        try:
            with open('../capitulo10.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:2000]
                self.lista_2 = self.lista[2001:4000]
                self.lista_3 = self.lista[4001:5000]
        except FileNotFoundError:
            with open('capitulo10.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:2000]
                self.lista_2 = self.lista[2001:4000]
                self.lista_3 = self.lista[4001:5000]


class Testcapitulo10Exercicio1(LoadData):
    def test_capitulo10_exercicio1_1(self):
        self.load_list()
        retorno = capitulo10_exercicio1(self.lista, 'Dr. André Peixoto')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][1] == '310.784.926-03'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        retorno = capitulo10_exercicio1(self.lista, 'André')
        assert len(retorno) == 17

    def test_capitulo10_exercicio1_2(self):
        self.load_list()
        retorno = capitulo10_exercicio1(self.lista_1, 'Caroline da Rocha')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][1] == '189.670.453-01'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        retorno = capitulo10_exercicio1(self.lista_1, 'Rocha')
        assert len(retorno) == 59

    def test_capitulo10_exercicio1_3(self):
        self.load_list()
        retorno = capitulo10_exercicio1(self.lista_2, 'Mariana Correia')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        retorno = capitulo10_exercicio1(self.lista_2, 'Mariana')
        assert len(retorno) == 12

    def test_capitulo10_exercicio1_4(self):
        self.load_list()
        retorno = capitulo10_exercicio1(self.lista_3, 'Isadora Barros')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        retorno = capitulo10_exercicio1(self.lista_3, 'Barros')
        assert len(retorno) == 19


class Testcapitulo10Exercicio2(LoadData):
    def test_capitulo10_exercicio2_1(self):
        self.load_list()
        retorno = capitulo10_exercicio2(self.lista, '687.429.130-04')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Gustavo Henrique Ferreira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio2_2(self):
        self.load_list()
        retorno = capitulo10_exercicio2(self.lista_1, '687.429.130-04')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Gustavo Henrique Ferreira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio2_3(self):
        self.load_list()
        retorno = capitulo10_exercicio2(self.lista_2, '037.145.628-26')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Catarina Oliveira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio2_4(self):
        self.load_list()
        retorno = capitulo10_exercicio2(self.lista_3, '274.806.359-74')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Sra. Giovanna Silveira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio3(LoadData):
    def test_capitulo10_exercicio3_1(self):
        self.load_list()
        retorno = capitulo10_exercicio3(self.lista, '315268700')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Elisa da Rosa'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio3_2(self):
        self.load_list()
        retorno = capitulo10_exercicio3(self.lista_1, '461835277')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Nicolas Monteiro'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio3_3(self):
        self.load_list()
        retorno = capitulo10_exercicio3(self.lista_2, '081352475')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Dr. Kaique Monteiro'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio3_4(self):
        self.load_list()
        retorno = capitulo10_exercicio3(self.lista_3, '048753622')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Gustavo Barbosa'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio4(LoadData):
    def test_capitulo10_exercicio4_1(self):
        self.load_list()
        retorno = capitulo10_exercicio4(self.lista, 'vnunes@bol.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Gustavo Barbosa'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio4_2(self):
        self.load_list()
        retorno = capitulo10_exercicio4(self.lista_1, 'bryanda-costa@gmail.com')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Dr. Noah Lopes'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio4_3(self):
        self.load_list()
        retorno = capitulo10_exercicio4(self.lista_2,'ramosgabriel@bol.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Marina Lima'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio4_4(self):
        self.load_list()
        retorno = capitulo10_exercicio4(self.lista_3,'helenacarvalho@hotmail.com')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Pedro Moreira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio5(LoadData):
    def test_capitulo10_exercicio5_1(self):
        self.load_list()
        retorno = capitulo10_exercicio5(self.lista, '172.28.212.183')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Pietro Rocha'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio5_2(self):
        self.load_list()
        retorno = capitulo10_exercicio5(self.lista_1,'172.28.212.183')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Pietro Rocha'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio5_3(self):
        self.load_list()
        retorno = capitulo10_exercicio5(self.lista_2,'10.159.24.166')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Eloah Nascimento'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio5_4(self):
        self.load_list()
        retorno = capitulo10_exercicio5(self.lista_3,'10.67.114.139')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Pedro Moreira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio6(LoadData):
    def test_capitulo10_exercicio6_1(self):
        self.load_list()
        retorno = capitulo10_exercicio6(self.lista, '223.32.79.132')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Brenda Gomes'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio6_2(self):
        self.load_list()
        retorno = capitulo10_exercicio6(self.lista_1,'223.32.79.132')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Brenda Gomes'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio6_3(self):
        self.load_list()
        retorno = capitulo10_exercicio6(self.lista_2, '24.230.5.128')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Vinicius Santos'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio6_4(self):
        self.load_list()
        retorno = capitulo10_exercicio6(self.lista_3, '60.232.87.120')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Ana Vitória Cavalcanti'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio7(LoadData):
    def test_capitulo10_exercicio7_1(self):
        self.load_list()
        retorno = capitulo10_exercicio7(self.lista, 'be:45:b2:e1:11:fa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Sra. Luana Alves'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio7_2(self):
        self.load_list()
        retorno = capitulo10_exercicio7(self.lista_1, '71:af:12:7f:05:da')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Davi Lucas Aragão'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio7_3(self):
        self.load_list()
        retorno = capitulo10_exercicio7(self.lista_2,'98:86:e0:07:c4:3c')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Marina Oliveira'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1

    def test_capitulo10_exercicio7_4(self):
        self.load_list()
        retorno = capitulo10_exercicio7(self.lista_3,'b5:a5:e1:d9:60:0b')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Ana Vitória Cavalcanti'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1


class Testcapitulo10Exercicio8(LoadData):
    def test_capitulo10_exercicio8_1(self):
        self.load_list()
        retorno = capitulo10_exercicio8(self.lista, 'Travessa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Brenda Martins'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 126

    def test_capitulo10_exercicio8_2(self):
        self.load_list()
        retorno = capitulo10_exercicio8(self.lista_1, 'Travessa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Brenda Martins'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 50

    def test_capitulo10_exercicio8_3(self):
        self.load_list()
        retorno = capitulo10_exercicio8(self.lista_2, 'Travessa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Pedro Henrique Martins'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 49


    def test_capitulo10_exercicio8_4(self):
        self.load_list()
        retorno = capitulo10_exercicio8(self.lista_3, 'Travessa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert retorno[0][0] == 'Lucca Cardoso'
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 27


class Testcapitulo10Exercicio9(LoadData):
    def test_capitulo10_exercicio9_1(self):
        self.load_list()
        retorno = capitulo10_exercicio9(self.lista, 'RJ')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 192
        retorno = capitulo10_exercicio9(self.lista, 'MG')
        assert len(retorno) == 167
        retorno = capitulo10_exercicio9(self.lista)
        assert len(retorno) == 190

    def test_capitulo10_exercicio9_2(self):
        self.load_list()
        retorno = capitulo10_exercicio9(self.lista_1, 'RJ')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 70
        retorno = capitulo10_exercicio9(self.lista_1, 'MG')
        assert len(retorno) == 81
        retorno = capitulo10_exercicio9(self.lista_1)
        assert len(retorno) == 69

    def test_capitulo10_exercicio9_3(self):
        self.load_list()
        retorno = capitulo10_exercicio9(self.lista_2, 'RJ')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 83
        retorno = capitulo10_exercicio9(self.lista_2, 'MG')
        assert len(retorno) == 57
        retorno = capitulo10_exercicio9(self.lista_2)
        assert len(retorno) == 88


    def test_capitulo10_exercicio9_4(self):
        self.load_list()
        retorno = capitulo10_exercicio9(self.lista_3, 'RJ')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 39
        retorno = capitulo10_exercicio9(self.lista_3, 'MG')
        assert len(retorno) == 29
        retorno = capitulo10_exercicio9(self.lista_3)
        assert len(retorno) == 33


class Testcapitulo10Exercicio10(LoadData):
    def test_capitulo10_exercicio10_1(self):
        self.load_list()
        retorno = capitulo10_exercicio10(self.lista, 12, 5)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 21
        retorno = capitulo10_exercicio10(self.lista, 22, 7)
        assert len(retorno) == 13

    def test_capitulo10_exercicio10_2(self):
        self.load_list()
        retorno = capitulo10_exercicio10(self.lista_1, 12, 5)
        assert len(retorno) == 7
        retorno = capitulo10_exercicio10(self.lista_1, 22, 7)
        assert len(retorno) == 2

    def test_capitulo10_exercicio10_3(self):
        self.load_list()
        retorno = capitulo10_exercicio10(self.lista_2, 12, 5)
        assert len(retorno) == 13
        retorno = capitulo10_exercicio10(self.lista_2, 22, 7)
        assert len(retorno) == 7

    def test_capitulo10_exercicio10_4(self):
        self.load_list()
        retorno = capitulo10_exercicio10(self.lista_3, 12, 5)
        assert len(retorno) == 1
        retorno = capitulo10_exercicio10(self.lista_3, 22, 7)
        assert len(retorno) == 4


class Testcapitulo10Exercicio11(LoadData):
    def test_capitulo10_exercicio11_1(self):
        self.load_list()
        retorno = capitulo10_exercicio11(self.lista, 1998)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 351
        retorno = capitulo10_exercicio11(self.lista, 2023)
        assert isinstance(retorno, list)
        assert len(retorno) == 0

    def test_capitulo10_exercicio11_2(self):
        self.load_list()
        retorno = capitulo10_exercicio11(self.lista_1, 1998)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 139
        retorno = capitulo10_exercicio11(self.lista_1, 2023)
        assert isinstance(retorno, list)
        assert len(retorno) == 0

    def test_capitulo10_exercicio11_3(self):
        self.load_list()
        retorno = capitulo10_exercicio11(self.lista_2, 1998)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 144
        retorno = capitulo10_exercicio11(self.lista_2, 2023)
        assert isinstance(retorno, list)
        assert len(retorno) == 0

    def test_capitulo10_exercicio11_4(self):
        self.load_list()
        retorno = capitulo10_exercicio11(self.lista_3, 1998)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 68
        retorno = capitulo10_exercicio11(self.lista_3, 2023)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo10Exercicio12(LoadData):
    def test_capitulo10_exercicio12_1(self):
        self.load_list()
        retorno = capitulo10_exercicio12(self.lista, 30, 12, 1997)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Maria Julia Caldeira'


    def test_capitulo10_exercicio12_2(self):
        self.load_list()
        retorno = capitulo10_exercicio12(self.lista, 29, 12, 1997)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Calebe Castro'

    def test_capitulo10_exercicio12_3(self):
        self.load_list()
        retorno = capitulo10_exercicio12(self.lista, 30, 3, 1999)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        assert retorno[0][0] == 'Maria Fernanda Carvalho'
        assert retorno[1][0] == 'Noah da Rocha'

    def test_capitulo10_exercicio12_4(self):
        self.load_list()
        retorno = capitulo10_exercicio12(self.lista, 1, 1, 2023)
        assert len(retorno) == 0


class Testcapitulo10Exercicio13(LoadData):
    def test_capitulo10_exercicio13_1(self):
        self.load_list()
        retorno = capitulo10_exercicio13(self.lista, 'Travessa', 1997)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        retorno = capitulo10_exercicio13(self.lista, 'Travessa', 1998)
        assert len(retorno) == 8

    def test_capitulo10_exercicio13_2(self):
        self.load_list()
        retorno = capitulo10_exercicio13(self.lista, 'Avenida', 1997)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 5
        retorno = capitulo10_exercicio13(self.lista, 'Avenida', 1998)
        assert len(retorno) == 10

    def test_capitulo10_exercicio13_3(self):
        self.load_list()
        retorno = capitulo10_exercicio13(self.lista, 'Praia', 1997)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 16
        retorno = capitulo10_exercicio13(self.lista, 'Praia', 1998)
        assert len(retorno) == 23

    def test_capitulo10_exercicio13_4(self):
        retorno = capitulo10_exercicio13([], 'Praia', 1997)
        assert len(retorno) == 0


class Testcapitulo10Exercicio14(LoadData):
    def test_capitulo10_exercicio14_1(self):
        self.load_list()
        retorno = capitulo10_exercicio14(self.lista, '192.168.246.242', '22.33.110.9')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Sr. Vinicius Alves'
   

    def test_capitulo10_exercicio14_2(self):
        self.load_list()
        retorno = capitulo10_exercicio14(self.lista, '10.212.126.249', '156.219.226.76')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Yuri Rocha'

    def test_capitulo10_exercicio14_3(self):
        self.load_list()
        retorno = capitulo10_exercicio14(self.lista, '10.200.64.125', '86.126.230.173')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Sabrina Porto'

    def test_capitulo10_exercicio14_4(self):
        self.load_list()
        retorno = capitulo10_exercicio14(self.lista, '10.200.64.125', '22.33.110.9')
        assert len(retorno) == 0


class Testcapitulo10Exercicio15(LoadData):
    def test_capitulo10_exercicio15_1(self):
        self.load_list()
        retorno = capitulo10_exercicio15(self.lista, '61:64:88:7e:f2:f5','10.218.144.42','14.228.65.85')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Nina da Cruz'


    def test_capitulo10_exercicio15_2(self):
        self.load_list()
        retorno = capitulo10_exercicio15(self.lista, '5d:44:7c:39:4f:38','10.180.53.228','137.165.195.108')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Carlos Eduardo Porto'


    def test_capitulo10_exercicio15_3(self):
        self.load_list()
        retorno = capitulo10_exercicio15(self.lista, '37:de:5a:e2:d9:1d','10.100.255.187','112.17.213.120')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Emanuel Freitas'


    def test_capitulo10_exercicio15_4(self):
        self.load_list()
        retorno = capitulo10_exercicio15(self.lista, '5d:44:7c:39:4f:39','10.180.53.228','137.165.195.108')
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo10Exercicio16(LoadData):
    def test_capitulo10_exercicio16_1(self):
        self.load_list()
        retorno = capitulo10_exercicio16(self.lista, 'e5:66:e7:2d:85:59','luiz-gustavo35@yahoo.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Vitor Hugo Nascimento'

    def test_capitulo10_exercicio16_2(self):
        self.load_list()
        retorno = capitulo10_exercicio16(self.lista, 'c5:6e:bf:d3:6f:01','duartemaite@gmail.com')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Helena Barros'

    def test_capitulo10_exercicio16_3(self):
        self.load_list()
        retorno = capitulo10_exercicio16(self.lista, '6a:b3:6a:db:99:f5','pereiramarina@yahoo.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Benjamin Lima'

    def test_capitulo10_exercicio16_4(self):
        self.load_list()
        retorno = capitulo10_exercicio16(self.lista, '6a:b3:6a:db:99:f5','yahoo.com.br')
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo10Exercicio17(LoadData):
    def test_capitulo10_exercicio17_1(self):
        self.load_list()
        retorno = capitulo10_exercicio17(self.lista, 'Lima','pereiramarina@yahoo.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Benjamin Lima'

    def test_capitulo10_exercicio17_2(self):
        self.load_list()
        retorno = capitulo10_exercicio17(self.lista, 'Barros','gmail.com')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 13
        assert retorno[0][0] == 'Helena Barros'

    def test_capitulo10_exercicio17_3(self):
        self.load_list()
        retorno = capitulo10_exercicio17(self.lista, 'Vitor Hugo','yahoo.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 6
        assert retorno[0][0] == 'Vitor Hugo Rezende'

    def test_capitulo10_exercicio17_4(self):
        self.load_list()
        retorno = capitulo10_exercicio17(self.lista, 'Vitor Hugo','gmail.com.br')
        assert isinstance(retorno, list)
        assert len(retorno) == 0



class Testcapitulo10Exercicio18(LoadData):
    def test_capitulo10_exercicio18_1(self):
        self.load_list()
        retorno = capitulo10_exercicio18(self.lista, 'thomasfogaca@gmail.com','fsales@uol.com.br')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        assert retorno[0][0] == 'Gustavo Henrique Ferreira'
        assert retorno[1][0] == 'Ana Luiza Alves'
        
    def test_capitulo10_exercicio18_2(self):
        self.load_list()
        retorno = capitulo10_exercicio18(self.lista, 'idias@hotmail.com')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Esther Cardoso'

    def test_capitulo10_exercicio18_3(self):
        self.load_list()
        retorno = capitulo10_exercicio18(self.lista, 'no_email@gmail.com')
        assert isinstance(retorno, list)
        assert len(retorno) == 0


    def test_capitulo10_exercicio18_4(self):
        self.load_list()
        retorno = capitulo10_exercicio18(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo10Exercicio19(LoadData):
    def test_capitulo10_exercicio19_1(self):
        self.load_list()
        retorno = capitulo10_exercicio19(self.lista, 'Silva','Pereira')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 125
        assert retorno[0][0] == 'Gabrielly Silva'

    def test_capitulo10_exercicio19_2(self):
        self.load_list()
        retorno = capitulo10_exercicio19(self.lista, 'Pereira','Pires','Silva')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 188
        assert retorno[0][0] == 'Sr. Luiz Henrique Pereira'

    def test_capitulo10_exercicio19_3(self):
        self.load_list()
        retorno = capitulo10_exercicio19(self.lista, 'Silva')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 59
        assert retorno[0][0] == 'Gabrielly Silva'

    def test_capitulo10_exercicio19_4(self):
        self.load_list()
        retorno = capitulo10_exercicio19(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo10Exercicio20(LoadData):
    def test_capitulo10_exercicio20_1(self):
        self.load_list()
        retorno = capitulo10_exercicio20(self.lista, '430.625.971-43', '867.402.319-31','719.328.564-55')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 3
        assert retorno[0][0] == 'Noah Pires'
        assert retorno[1][0] == 'Dra. Alice Cavalcanti'
        assert retorno[2][0] == 'Antônio Alves'

    def test_capitulo10_exercicio20_2(self):
        self.load_list()
        retorno = capitulo10_exercicio20(self.lista, '430.625.971-43', '867.402.319-31')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 2
        assert retorno[0][0] == 'Noah Pires'
        assert retorno[1][0] == 'Dra. Alice Cavalcanti'

    def test_capitulo10_exercicio20_3(self):
        self.load_list()
        retorno = capitulo10_exercicio20(self.lista, '430.625.971-43')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][0], str)
        assert isinstance(retorno[0][-1], datetime)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Noah Pires'

    def test_capitulo10_exercicio8_4(self):
        self.load_list()
        retorno = capitulo10_exercicio20(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0
