from capitulo8  import capitulo8_exercicio1
from capitulo8  import capitulo8_exercicio2
from capitulo8  import capitulo8_exercicio3
from capitulo8  import capitulo8_exercicio4
from capitulo8  import capitulo8_exercicio5
from capitulo8  import capitulo8_exercicio6
from capitulo8  import capitulo8_exercicio7
from capitulo8  import capitulo8_exercicio8
from capitulo8  import capitulo8_exercicio9
from capitulo8  import capitulo8_exercicio10
from capitulo8  import capitulo8_exercicio11
from capitulo8  import capitulo8_exercicio12
from capitulo8  import capitulo8_exercicio13
from capitulo8  import capitulo8_exercicio14
from capitulo8  import capitulo8_exercicio15
from capitulo8  import capitulo8_exercicio16
from capitulo8  import capitulo8_exercicio17
from capitulo8  import capitulo8_exercicio18
from capitulo8  import capitulo8_exercicio19
from capitulo8  import capitulo8_exercicio20

import pickle
import pytest
from datetime import datetime

class LoadData: 
    def load_list(self):
        try:
            with open('../capitulo8.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:200]
                self.lista_2 = self.lista[201:400]
                self.lista_3 = self.lista[401:600]
        except FileNotFoundError:
            with open('capitulo8.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:200]
                self.lista_2 = self.lista[201:400]
                self.lista_3 = self.lista[401:600]


class Testcapitulo8Exercicio1(LoadData):
    def test_capitulo8_exercicio1_1(self):
        self.load_list()
        retorno = capitulo8_exercicio1(self.lista, 'Caio Araújo')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio1(self.lista, 'Caio')
        assert len(retorno) == 0

    def test_capitulo8_exercicio1_2(self):
        self.load_list()
        retorno = capitulo8_exercicio1(self.lista_1, 'Caio Araújo')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio1(self.lista_1, 'Caio')
        assert len(retorno) == 0

    def test_capitulo8_exercicio1_3(self):
        self.load_list()
        retorno = capitulo8_exercicio1(self.lista_2, 'Daniela Teixeira')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio1(self.lista_2, 'Daniela')
        assert len(retorno) == 0

    def test_capitulo8_exercicio1_4(self):
        self.load_list()
        retorno = capitulo8_exercicio1(self.lista_3, 'Alice Caldeira')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio1(self.lista_3, 'Alice')
        assert len(retorno) == 0


class Testcapitulo8Exercicio2(LoadData):
    def test_capitulo8_exercicio2_1(self):
        self.load_list()
        retorno = capitulo8_exercicio2(self.lista, 'Caio Araújo')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio2(self.lista, 'Caio')
        assert len(retorno) == 3

    def test_capitulo8_exercicio2_2(self):
        self.load_list()
        retorno = capitulo8_exercicio2(self.lista_1, 'Caio Araújo')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio2(self.lista_1, 'Caio')
        assert len(retorno) == 1

    def test_capitulo8_exercicio2_3(self):
        self.load_list()
        retorno = capitulo8_exercicio2(self.lista_2, 'Daniela Teixeira')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio2(self.lista_2, 'Daniela')
        assert len(retorno) == 4

    def test_capitulo8_exercicio2_4(self):
        self.load_list()
        retorno = capitulo8_exercicio2(self.lista_3, 'Alice Caldeira')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], tuple)
        assert isinstance(retorno[0][2], datetime)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio2(self.lista_3, 'Alice')
        assert len(retorno) == 3


class Testcapitulo8Exercicio3(LoadData):
    def test_capitulo8_exercicio3_1(self):
        self.load_list()
        retorno = capitulo8_exercicio3(self.lista, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 405
        retorno = capitulo8_exercicio3(self.lista, 2)
        assert len(retorno) == 195

    def test_capitulo8_exercicio3_2(self):
        self.load_list()
        retorno = capitulo8_exercicio3(self.lista_1, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 139
        retorno = capitulo8_exercicio3(self.lista_1, 2)
        assert len(retorno) == 61

    def test_capitulo8_exercicio3_3(self):
        self.load_list()
        retorno = capitulo8_exercicio3(self.lista_2, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 131
        retorno = capitulo8_exercicio3(self.lista_2, 2)
        assert len(retorno) == 68

    def test_capitulo8_exercicio3_4(self):
        self.load_list()
        retorno = capitulo8_exercicio3(self.lista_3, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 135
        retorno = capitulo8_exercicio3(self.lista_3, 2)
        assert len(retorno) == 64


class Testcapitulo8Exercicio4(LoadData):
    def test_capitulo8_exercicio4_1(self):
        self.load_list()
        retorno = capitulo8_exercicio4(self.lista, 28)
        assert isinstance(retorno, set)
        assert len(retorno) == 15
        retorno = capitulo8_exercicio4(self.lista, 25)
        assert len(retorno) == 8

    def test_capitulo8_exercicio4_2(self):
        self.load_list()
        retorno = capitulo8_exercicio4(self.lista_1, 28)
        assert isinstance(retorno, set)
        assert len(retorno) == 5
        retorno = capitulo8_exercicio4(self.lista_1, 25)
        assert len(retorno) == 2

    def test_capitulo8_exercicio4_3(self):
        self.load_list()
        retorno = capitulo8_exercicio4(self.lista_2, 28)
        assert isinstance(retorno, set)
        assert len(retorno) == 3
        retorno = capitulo8_exercicio4(self.lista_2, 25)
        assert len(retorno) == 3

    def test_capitulo8_exercicio4_4(self):
        self.load_list()
        retorno = capitulo8_exercicio4(self.lista_3, 28)
        assert isinstance(retorno, set)
        assert len(retorno) == 7
        retorno = capitulo8_exercicio4(self.lista_3, 25)
        assert len(retorno) == 3


class Testcapitulo8Exercicio5(LoadData):
    def test_capitulo8_exercicio5_1(self):
        self.load_list()
        retorno = capitulo8_exercicio5(self.lista, 28, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 15
        retorno = capitulo8_exercicio5(self.lista, 25, 1)
        assert len(retorno) == 8

    def test_capitulo8_exercicio5_2(self):
        self.load_list()
        retorno = capitulo8_exercicio5(self.lista_1, 28, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 5
        retorno = capitulo8_exercicio5(self.lista_1, 25, 1)
        assert len(retorno) == 2

    def test_capitulo8_exercicio5_3(self):
        self.load_list()
        retorno = capitulo8_exercicio5(self.lista_2, 28, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 3
        retorno = capitulo8_exercicio5(self.lista_2, 25, 1)
        assert len(retorno) == 3

    def test_capitulo8_exercicio5_4(self):
        self.load_list()
        retorno = capitulo8_exercicio5(self.lista_3, 28, 1)
        assert isinstance(retorno, set)
        assert len(retorno) == 7
        retorno = capitulo8_exercicio5(self.lista_3, 25, 1)
        assert len(retorno) == 3


class Testcapitulo8Exercicio6(LoadData):
    def test_capitulo8_exercicio6_1(self):
        self.load_list()
        retorno = capitulo8_exercicio6(self.lista, 28, 2)
        assert isinstance(retorno, set)
        assert len(retorno) == 10
        retorno = capitulo8_exercicio6(self.lista, 25, 2)
        assert len(retorno) == 16

    def test_capitulo8_exercicio6_2(self):
        self.load_list()
        retorno = capitulo8_exercicio6(self.lista_1, 28, 2)
        assert isinstance(retorno, set)
        assert len(retorno) == 3
        retorno = capitulo8_exercicio6(self.lista_1, 25, 2)
        assert len(retorno) == 4

    def test_capitulo8_exercicio6_3(self):
        self.load_list()
        retorno = capitulo8_exercicio6(self.lista_2, 28, 2)
        assert isinstance(retorno, set)
        assert len(retorno) == 3
        retorno = capitulo8_exercicio6(self.lista_2, 25, 2)
        assert len(retorno) == 9

    def test_capitulo8_exercicio6_4(self):
        self.load_list()
        retorno = capitulo8_exercicio6(self.lista_3, 28, 2)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        retorno = capitulo8_exercicio6(self.lista_3, 25, 2)
        assert len(retorno) == 3


class Testcapitulo8Exercicio7(LoadData):
    def test_capitulo8_exercicio7_1(self):
        self.load_list()
        retorno = capitulo8_exercicio7(self.lista, 28, 5)
        assert isinstance(retorno, set)
        assert len(retorno) == 3
        retorno = capitulo8_exercicio7(self.lista, 25, 5)
        assert len(retorno) == 5

    def test_capitulo8_exercicio7_2(self):
        self.load_list()
        retorno = capitulo8_exercicio7(self.lista_1, 28, 5)
        assert isinstance(retorno, set)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio7(self.lista_1, 25, 5)
        assert len(retorno) == 1

    def test_capitulo8_exercicio7_3(self):
        self.load_list()
        retorno = capitulo8_exercicio7(self.lista_2, 28, 5)
        assert isinstance(retorno, set)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio7(self.lista_2, 25, 5)
        assert len(retorno) == 3

    def test_capitulo8_exercicio7_4(self):
        self.load_list()
        retorno = capitulo8_exercicio7(self.lista_3, 28, 5)
        assert isinstance(retorno, set)
        assert len(retorno) == 1
        retorno = capitulo8_exercicio7(self.lista_3, 25, 5)
        assert len(retorno) == 1


class Testcapitulo8Exercicio8(LoadData):
    def test_capitulo8_exercicio8_1(self):
        self.load_list()
        retorno = capitulo8_exercicio8(self.lista, 18, 7)
        assert isinstance(retorno, set)
        assert len(retorno) == 16
        retorno = capitulo8_exercicio8(self.lista, 15, 7)
        assert len(retorno) == 8

    def test_capitulo8_exercicio8_2(self):
        self.load_list()
        retorno = capitulo8_exercicio8(self.lista_1, 18, 7)
        assert isinstance(retorno, set)
        assert len(retorno) == 5
        retorno = capitulo8_exercicio8(self.lista_1, 15, 7)
        assert len(retorno) == 1

    def test_capitulo8_exercicio8_3(self):
        self.load_list()
        retorno = capitulo8_exercicio8(self.lista_2, 18, 7)
        assert isinstance(retorno, set)
        assert len(retorno) == 7
        retorno = capitulo8_exercicio8(self.lista_2, 15, 7)
        assert len(retorno) == 2

    def test_capitulo8_exercicio8_4(self):
        self.load_list()
        retorno = capitulo8_exercicio8(self.lista_3, 18, 7)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        retorno = capitulo8_exercicio8(self.lista_3, 15, 7)
        assert len(retorno) == 5


class Testcapitulo8Exercicio9(LoadData):
    def test_capitulo8_exercicio9_1(self):
        self.load_list()
        retorno = capitulo8_exercicio9(self.lista, 9)
        assert isinstance(retorno, set)
        assert len(retorno) == 13
        assert 4 in retorno
        assert 56 not in retorno

    def test_capitulo8_exercicio9_2(self):
        self.load_list()
        retorno = capitulo8_exercicio9(self.lista, 11)
        assert isinstance(retorno, set)
        assert len(retorno) == 17
        assert 4 in retorno
        assert 56 in retorno

    def test_capitulo8_exercicio9_3(self):
        self.load_list()
        retorno = capitulo8_exercicio9(self.lista, 13)
        assert isinstance(retorno, set)
        assert len(retorno) == 31
        retorno = capitulo8_exercicio9(self.lista, 14)
        assert len(retorno) == 35


    def test_capitulo8_exercicio9_4(self):
        self.load_list()
        retorno = capitulo8_exercicio9(self.lista, 15)
        assert isinstance(retorno, set)
        assert len(retorno) == 37
        retorno = capitulo8_exercicio9(self.lista, 20)
        assert len(retorno) == 63


class Testcapitulo8Exercicio10(LoadData):
    def test_capitulo8_exercicio10_1(self):
        self.load_list()
        retorno = capitulo8_exercicio10(self.lista)
        assert 3 in retorno
        assert 15 not in retorno
        assert len(retorno) == 170

    def test_capitulo8_exercicio10_2(self):
        self.load_list()
        retorno = capitulo8_exercicio10(self.lista_1)
        assert len(retorno) == 53

    def test_capitulo8_exercicio10_3(self):
        self.load_list()
        retorno = capitulo8_exercicio10(self.lista_2)
        assert len(retorno) == 67

    def test_capitulo8_exercicio10_4(self):
        self.load_list()
        retorno = capitulo8_exercicio10(self.lista_3)
        assert len(retorno) == 50


class Testcapitulo8Exercicio11(LoadData):
    def test_capitulo8_exercicio11_1(self):
        self.load_list()
        retorno = capitulo8_exercicio11(self.lista, 2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 276
        retorno = capitulo8_exercicio11(self.lista, 3)
        assert len(retorno) == 282
        retorno = capitulo8_exercicio11(self.lista, 4)
        assert len(retorno) == 269
        retorno = capitulo8_exercicio11(self.lista, 5)
        assert len(retorno) == 272

    def test_capitulo8_exercicio11_2(self):
        self.load_list()
        retorno = capitulo8_exercicio11(self.lista_1, 2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 90
        retorno = capitulo8_exercicio11(self.lista_1, 3)
        assert len(retorno) == 99
        retorno = capitulo8_exercicio11(self.lista_1, 4)
        assert len(retorno) == 96
        retorno = capitulo8_exercicio11(self.lista_1, 5)
        assert len(retorno) == 83

    def test_capitulo8_exercicio11_3(self):
        self.load_list()
        retorno = capitulo8_exercicio11(self.lista_2, 2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 102
        retorno = capitulo8_exercicio11(self.lista_2, 3)
        assert len(retorno) == 93
        retorno = capitulo8_exercicio11(self.lista_2, 4)
        assert len(retorno) == 91
        retorno = capitulo8_exercicio11(self.lista_2, 5)
        assert len(retorno) == 96

    def test_capitulo8_exercicio11_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo8_exercicio11(self.lista, 1000)
        assert str(error.value) == msg_erro
        with pytest.raises(IndexError) as error:
            capitulo8_exercicio11(self.lista, 6)
        assert str(error.value) == msg_erro
        msg_erro = "Campo datetime não encontrado."
        with pytest.raises(AttributeError) as error:
            capitulo8_exercicio11(self.lista, 0)
        assert str(error.value) == msg_erro


class Testcapitulo8Exercicio12(LoadData):
    def test_capitulo8_exercicio12_1(self):
        self.load_list()
        retorno = capitulo8_exercicio12(self.lista)
        assert len(retorno[0]) == 6
        assert len(retorno) == 276


    def test_capitulo8_exercicio12_2(self):
        self.load_list()
        retorno = capitulo8_exercicio12(self.lista_1)
        assert len(retorno[0]) == 6
        assert len(retorno) == 90

    def test_capitulo8_exercicio12_3(self):
        self.load_list()
        retorno = capitulo8_exercicio12(self.lista_2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 102

    def test_capitulo8_exercicio12_4(self):
        self.load_list()
        retorno = capitulo8_exercicio12([])
        assert type(retorno) == list
        assert len(retorno) == 0


class Testcapitulo8Exercicio13(LoadData):
    def test_capitulo8_exercicio13_1(self):
        self.load_list()
        retorno = capitulo8_exercicio13(self.lista)
        assert len(retorno[0]) == 6
        assert len(retorno) == 132

    def test_capitulo8_exercicio13_2(self):
        self.load_list()
        retorno = capitulo8_exercicio13(self.lista_1)
        assert len(retorno[0]) == 6
        assert len(retorno) == 43

    def test_capitulo8_exercicio13_3(self):
        self.load_list()
        retorno = capitulo8_exercicio13(self.lista_2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 48
        
    def test_capitulo8_exercicio13_4(self):
        retorno = capitulo8_exercicio13([])
        assert type(retorno) == list
        assert len(retorno) == 0


class Testcapitulo8Exercicio14(LoadData):
    def test_capitulo8_exercicio14_1(self):
        self.load_list()
        retorno = capitulo8_exercicio14(self.lista)
        assert len(retorno[0]) == 6
        assert len(retorno) == 25

    def test_capitulo8_exercicio14_2(self):
        self.load_list()
        retorno = capitulo8_exercicio14(self.lista_1)
        assert len(retorno[0]) == 6
        assert len(retorno) == 5

    def test_capitulo8_exercicio14_3(self):
        self.load_list()
        retorno = capitulo8_exercicio14(self.lista_2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 12

    def test_capitulo8_exercicio14_4(self):
        retorno = capitulo8_exercicio14([])
        assert type(retorno) == list
        assert len(retorno) == 0


class Testcapitulo8Exercicio15(LoadData):
    def test_capitulo8_exercicio15_1(self):
        self.load_list()
        retorno = capitulo8_exercicio15(self.lista)
        assert len(retorno[0]) == 6
        assert len(retorno) == 8
        retorno = capitulo8_exercicio15(self.lista, 'MG')
        assert len(retorno[0]) == 6
        assert len(retorno) == 10


    def test_capitulo8_exercicio15_2(self):
        self.load_list()
        retorno = capitulo8_exercicio15(self.lista_1)
        assert len(retorno[0]) == 6
        assert len(retorno) == 2
        retorno = capitulo8_exercicio15(self.lista_1, 'MG')
        assert len(retorno[0]) == 6
        assert len(retorno) == 4

    def test_capitulo8_exercicio15_3(self):
        self.load_list()
        retorno = capitulo8_exercicio15(self.lista_2)
        assert len(retorno[0]) == 6
        assert len(retorno) == 4
        retorno = capitulo8_exercicio15(self.lista_2, 'MG')
        assert len(retorno[0]) == 6
        assert len(retorno) == 3

    def test_capitulo8_exercicio15_4(self):
        self.load_list()
        retorno = capitulo8_exercicio15(self.lista_3)
        assert len(retorno[0]) == 6
        assert len(retorno) == 2
        retorno = capitulo8_exercicio15(self.lista_3, 'MG')
        assert len(retorno[0]) == 6
        assert len(retorno) == 3


class Testcapitulo8Exercicio16(LoadData):
    def test_capitulo8_exercicio16_1(self):
        self.load_list()
        retorno = capitulo8_exercicio16(self.lista)
        assert len(retorno[0]) == 3
        assert retorno[0][0] == 79
        assert retorno[0][2] == '452.803.691-60'
        assert len(retorno) == 8
        retorno = capitulo8_exercicio16(self.lista, 'MG')
        assert len(retorno[0]) == 3
        assert len(retorno) == 10

    def test_capitulo8_exercicio16_2(self):
        self.load_list()
        retorno = capitulo8_exercicio16(self.lista_1)
        assert len(retorno[0]) == 3
        assert len(retorno) == 2
        retorno = capitulo8_exercicio16(self.lista_1, 'MG')
        assert len(retorno[0]) == 3
        assert len(retorno) == 4

    def test_capitulo8_exercicio16_3(self):
        self.load_list()
        retorno = capitulo8_exercicio16(self.lista_2)
        assert len(retorno[0]) == 3
        assert len(retorno) == 4
        retorno = capitulo8_exercicio16(self.lista_2, 'MG')
        assert len(retorno[0]) == 3
        assert len(retorno) == 3

    def test_capitulo8_exercicio16_4(self):
        self.load_list()
        retorno = capitulo8_exercicio16(self.lista_3)
        assert len(retorno[0]) == 3
        assert len(retorno) == 2
        retorno = capitulo8_exercicio16(self.lista_3, 'MG')
        assert len(retorno[0]) == 3
        assert len(retorno) == 3


class Testcapitulo8Exercicio17(LoadData):
    def test_capitulo8_exercicio17_1(self):
        self.load_list()
        retorno = capitulo8_exercicio17(self.lista, 1, 'SP')
        assert len(retorno[0]) == 4
        assert len(retorno) == 11
        retorno = capitulo8_exercicio17(self.lista, 1, 'MG')
        assert len(retorno) == 14

    def test_capitulo8_exercicio17_2(self):
        self.load_list()
        retorno = capitulo8_exercicio17(self.lista_1, 1, 'SP')
        assert len(retorno[0]) == 4
        assert len(retorno) == 3
        retorno = capitulo8_exercicio17(self.lista_1, 1, 'MG')
        assert len(retorno) == 4

    def test_capitulo8_exercicio17_3(self):
        self.load_list()
        retorno = capitulo8_exercicio17(self.lista_2, 1, 'SP')
        assert len(retorno[0]) == 4
        assert len(retorno) == 5
        retorno = capitulo8_exercicio17(self.lista_2, 1, 'MG')
        assert len(retorno) == 4

    def test_capitulo8_exercicio17_4(self):
        self.load_list()
        retorno = capitulo8_exercicio17(self.lista_3, 1, 'SP')
        assert len(retorno[0]) == 4
        assert len(retorno) == 3
        retorno = capitulo8_exercicio17(self.lista_3, 1, 'MG')
        assert len(retorno) == 6



class Testcapitulo8Exercicio18(LoadData):
    def test_capitulo8_exercicio18_1(self):
        self.load_list()
        retorno = capitulo8_exercicio18(self.lista, 15, 1)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 15
        retorno = capitulo8_exercicio18(self.lista, 22, 1)
        assert len(retorno) == 10

    def test_capitulo8_exercicio18_2(self):
        self.load_list()
        retorno = capitulo8_exercicio18(self.lista_1, 15, 1)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 5
        retorno = capitulo8_exercicio18(self.lista_1, 22, 1)
        assert len(retorno) == 3

    def test_capitulo8_exercicio18_3(self):
        self.load_list()
        retorno = capitulo8_exercicio18(self.lista_2, 15, 1)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 7
        retorno = capitulo8_exercicio18(self.lista_2, 22, 1)
        assert len(retorno) == 4

    def test_capitulo8_exercicio18_4(self):
        self.load_list()
        retorno = capitulo8_exercicio18(self.lista_3, 15, 1)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 3
        retorno = capitulo8_exercicio18(self.lista_3, 22, 1)
        assert len(retorno) == 3



class Testcapitulo8Exercicio19(LoadData):
    def test_capitulo8_exercicio19_1(self):
        self.load_list()
        retorno = capitulo8_exercicio19(self.lista, 10)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 11
        assert retorno[1].day == 23
        assert retorno[1].month == 1

    def test_capitulo8_exercicio19_2(self):
        self.load_list()
        retorno = capitulo8_exercicio19(self.lista, 39)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 40
        assert retorno[1].day == 11
        assert retorno[1].month == 2

    def test_capitulo8_exercicio19_3(self):
        self.load_list()
        retorno = capitulo8_exercicio19(self.lista, 140)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 141
        assert retorno[1].day == 26
        assert retorno[1].month == 1

    def test_capitulo8_exercicio19_4(self):
        self.load_list()
        retorno = capitulo8_exercicio19(self.lista, 1000)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 0


class Testcapitulo8Exercicio20(LoadData):
    def test_capitulo8_exercicio20_1(self):
        self.load_list()
        retorno = capitulo8_exercicio20(self.lista, 10)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 11
        assert retorno[1].day == 23
        assert retorno[1].month == 1

    def test_capitulo8_exercicio20_2(self):
        self.load_list()
        retorno = capitulo8_exercicio20(self.lista, 39)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 40
        assert retorno[1].day == 11
        assert retorno[1].month == 2

    def test_capitulo8_exercicio20_3(self):
        self.load_list()
        retorno = capitulo8_exercicio20(self.lista, 140)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 5
        assert retorno[0] == 141
        assert retorno[1].day == 26
        assert retorno[1].month == 1

    def test_capitulo8_exercicio8_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo8_exercicio20(self.lista, 1000)
        assert str(error.value) == msg_erro
