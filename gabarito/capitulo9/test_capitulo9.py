from capitulo9  import capitulo9_exercicio1
from capitulo9  import capitulo9_exercicio2
from capitulo9  import capitulo9_exercicio3
from capitulo9  import capitulo9_exercicio4
from capitulo9  import capitulo9_exercicio5
from capitulo9  import capitulo9_exercicio6
from capitulo9  import capitulo9_exercicio7
from capitulo9  import capitulo9_exercicio8
from capitulo9  import capitulo9_exercicio9
from capitulo9  import capitulo9_exercicio10
from capitulo9  import capitulo9_exercicio11
from capitulo9  import capitulo9_exercicio12
from capitulo9  import capitulo9_exercicio13
from capitulo9  import capitulo9_exercicio14
from capitulo9  import capitulo9_exercicio15
from capitulo9  import capitulo9_exercicio16
from capitulo9  import capitulo9_exercicio17
from capitulo9  import capitulo9_exercicio18
from capitulo9  import capitulo9_exercicio19
from capitulo9  import capitulo9_exercicio20

import pickle
import pytest

class LoadData: 
    def load_list(self):
        self.load_list1()
        self.load_list2()
        self.load_list3()

    def load_list1(self):
        try:
            with open('../capitulo7.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:50]
                self.lista_2 = self.lista[51:100]
                self.lista_3 = self.lista[101:199]
        except FileNotFoundError:
            with open('capitulo7.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:50]
                self.lista_2 = self.lista[51:100]
                self.lista_3 = self.lista[101:199]

    def load_list2(self):
        try:
            with open('../capitulo8.bin', 'rb') as list_in_file:
                self.lista2 = pickle.load(list_in_file)
        except FileNotFoundError:
            with open('capitulo8.bin', 'rb') as list_in_file:
                self.lista2 = pickle.load(list_in_file)

    def load_list3(self):
        try:
            with open('../capitulo6.bin', 'rb') as list_in_file:
                self.lista3 = pickle.load(list_in_file)
        except FileNotFoundError:
            with open('capitulo6.bin', 'rb') as list_in_file:
                self.lista3 = pickle.load(list_in_file)

class Testcapitulo9Exercicio1(LoadData):
    def test_capitulo9_exercicio1_1(self):
        self.load_list()
        retorno = capitulo9_exercicio1(self.lista, 'Air India')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 8
        retorno = capitulo9_exercicio1(self.lista, 'VietJet Air')
        assert len(retorno) == 5

    def test_capitulo9_exercicio1_2(self):
        self.load_list()
        retorno = capitulo9_exercicio1(self.lista, 'Air India', 'LATAM Airlines')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 10
        retorno = capitulo9_exercicio1(self.lista, 'VietJet Air', 'Air India')
        assert len(retorno) == 13

    def test_capitulo9_exercicio1_3(self):
        self.load_list()
        retorno = capitulo9_exercicio1(self.lista, 'VietJet Air', 'Air India', 'LATAM Airlines')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 15


    def test_capitulo9_exercicio1_4(self):
        self.load_list()
        retorno = capitulo9_exercicio1(self.lista)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio1(self.lista, 'Not Airline')
        assert len(retorno) == 0


class Testcapitulo9Exercicio2(LoadData):
    def test_capitulo9_exercicio2_1(self):
        self.load_list()
        retorno = capitulo9_exercicio2(self.lista,  299, 713, 492)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 4


    def test_capitulo9_exercicio2_2(self):
        self.load_list()
        retorno = capitulo9_exercicio2(self.lista,  299)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 1
        retorno = capitulo9_exercicio2(self.lista,  292)
        assert len(retorno) == 0


    def test_capitulo9_exercicio2_3(self):
        self.load_list()
        retorno = capitulo9_exercicio2(self.lista,  299, 1500 ,200, 492)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 3

    def test_capitulo9_exercicio2_4(self):
        self.load_list()
        retorno = capitulo9_exercicio2(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio3(LoadData):
    def test_capitulo9_exercicio3_1(self):
        self.load_list()
        retorno = capitulo9_exercicio3(self.lista, 'Rome', 'Horley','Kenner')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 4

    def test_capitulo9_exercicio3_2(self):
        self.load_list()
        retorno = capitulo9_exercicio3(self.lista, 'Rome', 'Kenner')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 2
        retorno = capitulo9_exercicio3(self.lista, 'Rome', 'Horley')
        assert len(retorno) == 3

    def test_capitulo9_exercicio3_3(self):
        self.load_list()
        retorno = capitulo9_exercicio3(self.lista, 'Rome')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 1

    def test_capitulo9_exercicio3_4(self):
        self.load_list()
        retorno = capitulo9_exercicio3(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio4(LoadData):
    def test_capitulo9_exercicio4_1(self):
        self.load_list()
        retorno = capitulo9_exercicio4(self.lista, 'Nanchang','Foz do Iguacu','St. Petersburg')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 3

    def test_capitulo9_exercicio4_2(self):
        self.load_list()
        retorno = capitulo9_exercicio4(self.lista, 'Nanchang','St. Petersburg')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 2

    def test_capitulo9_exercicio4_3(self):
        self.load_list()
        retorno = capitulo9_exercicio4(self.lista, 'St. Petersburg')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 1

    def test_capitulo9_exercicio4_4(self):
        self.load_list()
        retorno = capitulo9_exercicio4(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio5(LoadData):
    def test_capitulo9_exercicio5_1(self):
        self.load_list()
        retorno = capitulo9_exercicio5(self.lista, 'Ana Beatriz Sales', 'Yasmin Fernandes','Sabrina Costa')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 28

    def test_capitulo9_exercicio5_2(self):
        self.load_list()
        retorno = capitulo9_exercicio5(self.lista, 'Ana Beatriz Sales')
        assert len(retorno) == 5
        retorno = capitulo9_exercicio5(self.lista, 'Yasmin Fernandes')
        assert len(retorno) == 6
        retorno = capitulo9_exercicio5(self.lista, 'Ana Beatriz Sales', 'Yasmin Fernandes')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 11

    def test_capitulo9_exercicio5_3(self):
        self.load_list()
        retorno = capitulo9_exercicio5(self.lista, 'Ana Beatriz Sales')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 5

    def test_capitulo9_exercicio5_4(self):
        self.load_list()
        retorno = capitulo9_exercicio5(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio6(LoadData):
    def test_capitulo9_exercicio6_1(self):
        self.load_list()
        retorno = capitulo9_exercicio6(self.lista, '549.360.817-01', '903.162.845-05', '729.361.584-19')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 11

    def test_capitulo9_exercicio6_2(self):
        self.load_list()
        retorno = capitulo9_exercicio6(self.lista, '549.360.817-01', '903.162.845-05')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 7

    def test_capitulo9_exercicio6_3(self):
        self.load_list()
        retorno = capitulo9_exercicio6(self.lista, '549.360.817-01')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 5

    def test_capitulo9_exercicio6_4(self):
        self.load_list()
        retorno = capitulo9_exercicio6(self.lista)
        assert isinstance(retorno, list)
        assert len(retorno) == 0



class Testcapitulo9Exercicio7(LoadData):
    def test_capitulo9_exercicio7_1(self):
        self.load_list()
        retorno = capitulo9_exercicio7(self.lista,  'Ana Beatriz Sales', '549.360.817-01','Yasmin Fernandes', '903.162.845-05')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 18

    def test_capitulo9_exercicio7_2(self):
        self.load_list()
        retorno = capitulo9_exercicio7(self.lista,  'Ana Beatriz Sales', '549.360.817-01')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 10


    def test_capitulo9_exercicio7_3(self):
        self.load_list()
        retorno = capitulo9_exercicio7(self.lista,  '549.360.817-01')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], int)
        assert isinstance(retorno[1], int)
        assert len(retorno) == 5
        retorno = capitulo9_exercicio7(self.lista,  'Ana Beatriz Sales')
        assert len(retorno) == 5

    def test_capitulo9_exercicio7_4(self):
        self.load_list()
        retorno = capitulo9_exercicio7(self.lista)
        assert len(retorno) == 0


class Testcapitulo9Exercicio8(LoadData):
    def test_capitulo9_exercicio8_1(self):
        self.load_list()
        retorno = capitulo9_exercicio8(self.lista, airline='American Airlines')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 7
        
    def test_capitulo9_exercicio8_2(self):
        self.load_list()
        retorno = capitulo9_exercicio8(self.lista, price=299)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 1
        retorno = capitulo9_exercicio8(self.lista, price=987)
        assert len(retorno) == 1

    def test_capitulo9_exercicio8_3(self):
        self.load_list()
        retorno = capitulo9_exercicio8(self.lista, stops='non-stop')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 50
        retorno = capitulo9_exercicio8(self.lista, stop='non-stop')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 0

    def test_capitulo9_exercicio8_4(self):
        self.load_list()
        retorno = capitulo9_exercicio8(self.lista, airline='American Airlines', price=987)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 8        
        retorno = capitulo9_exercicio8(self.lista)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 0
        

class Testcapitulo9Exercicio9(LoadData):
    def test_capitulo9_exercicio9_1(self):
        self.load_list()
        retorno = capitulo9_exercicio9(self.lista, state='Texas')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 7
        retorno = capitulo9_exercicio9(self.lista, state='California')
        assert len(retorno) == 3

   
    def test_capitulo9_exercicio9_2(self):
        self.load_list()
        retorno = capitulo9_exercicio9(self.lista, country='Chile')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        retorno = capitulo9_exercicio9(self.lista, country='Brazil')
        assert len(retorno) == 20
        retorno = capitulo9_exercicio9(self.lista, country='Brasil')
        assert len(retorno) == 0

    def test_capitulo9_exercicio9_3(self):
        self.load_list()
        retorno = capitulo9_exercicio9(self.lista, country='Brazil', state='California')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 23

    def test_capitulo9_exercicio9_4(self):
        self.load_list()
        retorno = capitulo9_exercicio9(self.lista)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 0


class Testcapitulo9Exercicio10(LoadData):
    def test_capitulo9_exercicio10_1(self):
        self.load_list()
        retorno = capitulo9_exercicio10(self.lista, state='Texas')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 3
        retorno = capitulo9_exercicio10(self.lista, state='California')
        assert len(retorno) == 2

    def test_capitulo9_exercicio10_2(self):
        self.load_list()
        retorno = capitulo9_exercicio10(self.lista, country='Chile')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 9
        retorno = capitulo9_exercicio10(self.lista, country='Brazil')
        assert len(retorno) == 16
        retorno = capitulo9_exercicio10(self.lista, country='Brasil')
        assert len(retorno) == 0

    def test_capitulo9_exercicio10_3(self):
        self.load_list()
        retorno = capitulo9_exercicio10(self.lista, country='Brazil', state='California')
        assert isinstance(retorno, tuple)
        assert len(retorno) == 18

    def test_capitulo9_exercicio10_4(self):
        self.load_list()
        retorno = capitulo9_exercicio10(self.lista)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 0


class Testcapitulo9Exercicio11(LoadData):
    def test_capitulo9_exercicio11_1(self):
        self.load_list()
        retorno = capitulo9_exercicio11(self.lista2, '846.023.971-31','704.285.163-35','489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert len(retorno) == 4

    def test_capitulo9_exercicio11_2(self):
        self.load_list()
        retorno = capitulo9_exercicio11(self.lista2, '704.285.163-35','489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert retorno[0] == 577
        assert len(retorno) == 3

    def test_capitulo9_exercicio11_3(self):
        self.load_list()
        retorno = capitulo9_exercicio11(self.lista2, '489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert retorno[0] == 567
        assert len(retorno) == 2

    def test_capitulo9_exercicio11_4(self):
        self.load_list()
        retorno = capitulo9_exercicio11(self.lista2, '111.111.111-11')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio11(self.lista2)
        assert len(retorno) == 0


class Testcapitulo9Exercicio12(LoadData):
    def test_capitulo9_exercicio12_1(self):
        self.load_list()
        retorno = capitulo9_exercicio12(self.lista2, '846.023.971-31','704.285.163-35','489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Maria Fernanda Barbosa'
        assert len(retorno) == 4


    def test_capitulo9_exercicio12_2(self):
        self.load_list()
        retorno = capitulo9_exercicio12(self.lista2, '704.285.163-35','489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Eloah Rezende'
        assert len(retorno) == 3

    def test_capitulo9_exercicio12_3(self):
        self.load_list()
        retorno = capitulo9_exercicio12(self.lista2, '489.015.267-94','643.598.120-51')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Ana Aragão'
        assert len(retorno) == 2

    def test_capitulo9_exercicio12_4(self):
        self.load_list()
        retorno = capitulo9_exercicio12(self.lista2, '111.111.111-11')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio12(self.lista2)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio13(LoadData):
    def test_capitulo9_exercicio13_1(self):
        self.load_list()
        retorno = capitulo9_exercicio13(self.lista2,'Frentista','Contador','Educador')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Ryan Moreira-Frentista'
        assert len(retorno) == 8

    def test_capitulo9_exercicio13_2(self):
        self.load_list()
        retorno = capitulo9_exercicio13(self.lista2,'Frentista','Educador')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Ryan Moreira-Frentista'
        assert len(retorno) == 6

    def test_capitulo9_exercicio13_3(self):
        self.load_list()
        retorno = capitulo9_exercicio13(self.lista2, 'Educador')
        assert isinstance(retorno, list)
        assert retorno[0] == 'Eloah Pinto-Educador'
        assert len(retorno) == 1

    def test_capitulo9_exercicio13_4(self):
        self.load_list()
        retorno = capitulo9_exercicio13(self.lista2)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio14(LoadData):
    def test_capitulo9_exercicio14_1(self):
        self.load_list()
        retorno = capitulo9_exercicio14(self.lista2,'example.com', 'example.net', 'example.org')
        assert isinstance(retorno, list)
        assert len(retorno) == 600

    def test_capitulo9_exercicio14_2(self):
        self.load_list()
        retorno = capitulo9_exercicio14(self.lista2,'example.org', 'example.net')
        assert isinstance(retorno, list)
        assert len(retorno) == 395
        assert retorno[0] == 'Sr. Antônio da Conceição-nascimentoisaac@example.org'
        retorno = capitulo9_exercicio14(self.lista2,'example.net', 'example.org')
        assert retorno[0] == 'Lucas Oliveira-lorenzoda-costa@example.net'

    def test_capitulo9_exercicio14_3(self):
        self.load_list()
        retorno = capitulo9_exercicio14(self.lista2, 'example.org')
        assert isinstance(retorno, list)
        assert len(retorno) == 208

    def test_capitulo9_exercicio14_4(self):
        self.load_list()
        retorno = capitulo9_exercicio14(self.lista2)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio15(LoadData):
    def test_capitulo9_exercicio15_1(self):
        self.load_list()
        retorno = capitulo9_exercicio15(self.lista2,'Silva','Caldeira','Rocha')
        assert isinstance(retorno, list)
        assert len(retorno) == 35
        assert retorno[0] == 'Alana Silva-rezenderafael@example.org'

    def test_capitulo9_exercicio15_2(self):
        self.load_list()
        retorno = capitulo9_exercicio15(self.lista2,'Rocha','Caldeira')
        assert isinstance(retorno, list)
        assert len(retorno) == 28
        assert retorno[0] == 'Raquel da Rocha-ianmonteiro@example.net'
        retorno = capitulo9_exercicio15(self.lista2,'Caldeira','Rocha')
        assert retorno[0] == 'Julia Caldeira-nicolas40@example.org'

    def test_capitulo9_exercicio15_3(self):
        self.load_list()
        retorno = capitulo9_exercicio15(self.lista2,'Rocha')
        assert isinstance(retorno, list)
        assert len(retorno) == 18
        assert retorno[0] == 'Raquel da Rocha-ianmonteiro@example.net'

    def test_capitulo9_exercicio15_4(self):
        self.load_list()
        retorno = capitulo9_exercicio15(self.lista2)
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio15(self.lista2, 'AAAA')
        assert len(retorno) == 0


class Testcapitulo9Exercicio16(LoadData):
    def test_capitulo9_exercicio16_1(self):
        self.load_list()
        retorno = capitulo9_exercicio16(self.lista3, 'Silva', 'Rocha', 'Pereira')
        assert isinstance(retorno, list)
        assert len(retorno) == 871
        assert retorno[0] == 'Daniel Silva 936.712.085-03'

    def test_capitulo9_exercicio16_2(self):
        self.load_list()
        retorno = capitulo9_exercicio16(self.lista3, 'Silva', 'Rocha')
        assert isinstance(retorno, list)
        assert len(retorno) == 668
        assert retorno[0] == 'Daniel Silva 936.712.085-03'
        retorno = capitulo9_exercicio16(self.lista3, 'Rocha', 'Silva')
        assert retorno[0] == 'Anthony Rocha 410.762.983-03'

    def test_capitulo9_exercicio16_3(self):
        self.load_list()
        retorno = capitulo9_exercicio16(self.lista3, 'Silva')
        assert isinstance(retorno, list)
        assert len(retorno) == 226
        assert retorno[0] == 'Daniel Silva 936.712.085-03'

    def test_capitulo9_exercicio16_4(self):
        self.load_list()
        retorno = capitulo9_exercicio16(self.lista3, 'AAA')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio16(self.lista3)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio17(LoadData):
    def test_capitulo9_exercicio17_1(self):
        self.load_list()
        retorno = capitulo9_exercicio17(self.lista3,'mirella98@gmail.com','fernandesenrico@moreira.br','mda-conceicao@bol.com.br')
        assert isinstance(retorno, list)
        assert len(retorno) == 3

    def test_capitulo9_exercicio17_2(self):
        self.load_list()
        retorno = capitulo9_exercicio17(self.lista3,'mirella98@gmail.com','fernandesenrico@moreira.br')
        assert isinstance(retorno, list)
        assert len(retorno) == 2
 
    def test_capitulo9_exercicio17_3(self):
        self.load_list()
        retorno = capitulo9_exercicio17(self.lista3,'mirella98@gmail.com')
        assert isinstance(retorno, list)
        assert len(retorno) == 1

    def test_capitulo9_exercicio17_4(self):
        self.load_list()
        retorno = capitulo9_exercicio17(self.lista3, 'aaa@aaa.com')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        retorno = capitulo9_exercicio17(self.lista3)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio18(LoadData):
    def test_capitulo9_exercicio18_1(self):
        self.load_list()
        retorno = capitulo9_exercicio18(self.lista3,'Avenida de Jesus','Rua de Monteiro','Pátio Cavalcanti')
        assert isinstance(retorno, list)
        assert len(retorno) == 9
        
    def test_capitulo9_exercicio18_2(self):
        self.load_list()
        retorno = capitulo9_exercicio18(self.lista3,'Avenida de Jesus','Rua de Monteiro')
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        retorno = capitulo9_exercicio18(self.lista3,'Rua de Monteiro', 'Avenida de Jesus')
        assert isinstance(retorno, list)
        assert len(retorno) == 4

    def test_capitulo9_exercicio18_3(self):
        self.load_list()
        retorno = capitulo9_exercicio18(self.lista3,'Rua de Monteiro')
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert isinstance(retorno[0], tuple)

    def test_capitulo9_exercicio18_4(self):
        self.load_list()
        retorno = capitulo9_exercicio18(self.lista3)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio19(LoadData):
    def test_capitulo9_exercicio19_1(self):
        self.load_list()
        retorno = capitulo9_exercicio19(self.lista3,'04/27','03/30','04/29')
        assert isinstance(retorno, list)
        assert len(retorno) == 387
        assert len(retorno[0]) == 6

    def test_capitulo9_exercicio19_2(self):
        self.load_list()
        retorno = capitulo9_exercicio19(self.lista3,'04/27','03/30')
        assert isinstance(retorno, list)
        assert len(retorno) == 253
        assert len(retorno[0]) == 6
        retorno = capitulo9_exercicio19(self.lista3,'03/30','04/27')
        assert isinstance(retorno, list)
        assert len(retorno) == 253

    def test_capitulo9_exercicio19_3(self):
        self.load_list()
        retorno = capitulo9_exercicio19(self.lista3,'03/30')
        assert isinstance(retorno, list)
        assert len(retorno) == 140

    def test_capitulo9_exercicio19_4(self):
        self.load_list()
        retorno = capitulo9_exercicio19(self.lista3)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo9Exercicio20(LoadData):
    def test_capitulo9_exercicio20_1(self):
        self.load_list()
        retorno = capitulo9_exercicio20(self.lista3,'27','30','29')
        assert isinstance(retorno, list)
        assert len(retorno) == 4480
        assert len(retorno[0]) == 6
        retorno = capitulo9_exercicio20(self.lista3,27,30,29)
        assert len(retorno) == 4480

    def test_capitulo9_exercicio20_2(self):
        self.load_list()
        retorno = capitulo9_exercicio20(self.lista3,'27','30')
        assert isinstance(retorno, list)
        assert len(retorno) == 3003
        assert len(retorno[0]) == 6

    def test_capitulo9_exercicio20_3(self):
        self.load_list()
        retorno = capitulo9_exercicio20(self.lista3,'27')
        assert isinstance(retorno, list)
        assert len(retorno) == 1539
        assert len(retorno[0]) == 6

    def test_capitulo9_exercicio8_4(self):
        self.load_list()
        retorno = capitulo9_exercicio20(self.lista3)
        assert isinstance(retorno, list)
        assert len(retorno) == 0
