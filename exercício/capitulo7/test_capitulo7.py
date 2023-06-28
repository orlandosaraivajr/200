from capitulo7  import capitulo7_exercicio1
from capitulo7  import capitulo7_exercicio2
from capitulo7  import capitulo7_exercicio3
from capitulo7  import capitulo7_exercicio4
from capitulo7  import capitulo7_exercicio5
from capitulo7  import capitulo7_exercicio6
from capitulo7  import capitulo7_exercicio7
from capitulo7  import capitulo7_exercicio8
from capitulo7  import capitulo7_exercicio9
from capitulo7  import capitulo7_exercicio10
from capitulo7  import capitulo7_exercicio11
from capitulo7  import capitulo7_exercicio12
from capitulo7  import capitulo7_exercicio13
from capitulo7  import capitulo7_exercicio14
from capitulo7  import capitulo7_exercicio15
from capitulo7  import capitulo7_exercicio16
from capitulo7  import capitulo7_exercicio17
from capitulo7  import capitulo7_exercicio18
from capitulo7  import capitulo7_exercicio19
from capitulo7  import capitulo7_exercicio20

import pickle
import pytest

class LoadData: 
    def load_list(self):
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


class Testcapitulo7Exercicio1(LoadData):
    def test_capitulo7_exercicio1_1(self):
        self.load_list()
        retorno = capitulo7_exercicio1(self.lista, 'Air India')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 8
        retorno = capitulo7_exercicio1(self.lista, 'VietJet Air')
        assert len(retorno) == 5

    def test_capitulo7_exercicio1_2(self):
        self.load_list()
        retorno = capitulo7_exercicio1(self.lista_1, 'Air India')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 3
        retorno = capitulo7_exercicio1(self.lista_1, 'VietJet Air')
        assert len(retorno) == 1

    def test_capitulo7_exercicio1_3(self):
        self.load_list()
        retorno = capitulo7_exercicio1(self.lista_2, 'Air India')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 2
        retorno = capitulo7_exercicio1(self.lista_2, 'VietJet Air')
        assert len(retorno) == 1

    def test_capitulo7_exercicio1_4(self):
        self.load_list()
        retorno = capitulo7_exercicio1(self.lista_3, 'Air India')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 3
        retorno = capitulo7_exercicio1(self.lista_3, 'VietJet Air')
        assert len(retorno) == 3


class Testcapitulo7Exercicio2(LoadData):
    def test_capitulo7_exercicio2_1(self):
        self.load_list()
        retorno = capitulo7_exercicio2(self.lista, 1)
        assert isinstance(retorno, list)
        assert len(retorno) == 57
        retorno = capitulo7_exercicio2(self.lista, 'non-stop')
        assert len(retorno) == 50
        retorno = capitulo7_exercicio2(self.lista, 5)
        assert len(retorno) == 0

    def test_capitulo7_exercicio2_2(self):
        self.load_list()
        retorno = capitulo7_exercicio2(self.lista_1, '1')
        assert isinstance(retorno, list)
        assert len(retorno) == 14
        retorno = capitulo7_exercicio2(self.lista_1, 'non-stop')
        assert len(retorno) == 15
        retorno = capitulo7_exercicio2(self.lista_1, 5)
        assert len(retorno) == 0

    def test_capitulo7_exercicio2_3(self):
        self.load_list()
        retorno = capitulo7_exercicio2(self.lista_2, 1)
        assert isinstance(retorno, list)
        assert len(retorno) == 15
        retorno = capitulo7_exercicio2(self.lista_2, 'non-stop')
        assert len(retorno) == 11
        retorno = capitulo7_exercicio2(self.lista_2, 5)
        assert len(retorno) == 0

    def test_capitulo7_exercicio2_4(self):
        self.load_list()
        retorno = capitulo7_exercicio2(self.lista_3, '1')
        assert isinstance(retorno, list)
        assert len(retorno) == 26
        retorno = capitulo7_exercicio2(self.lista_3, 'non-stop')
        assert len(retorno) == 23
        retorno = capitulo7_exercicio2(self.lista_3, 5)
        assert len(retorno) == 0


class Testcapitulo7Exercicio3(LoadData):
    def test_capitulo7_exercicio3_1(self):
        self.load_list()
        retorno = capitulo7_exercicio3(self.lista, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 72
        retorno = capitulo7_exercicio3(self.lista, 700)
        assert len(retorno) == 124
        retorno = capitulo7_exercicio3(self.lista, 300)
        assert len(retorno) == 26
        assert len(capitulo7_exercicio3(self.lista)) == 124

    def test_capitulo7_exercicio3_2(self):
        self.load_list()
        retorno = capitulo7_exercicio3(self.lista_1, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 9
        retorno = capitulo7_exercicio3(self.lista_1, 700)
        assert len(retorno) == 24
        retorno = capitulo7_exercicio3(self.lista_1, 300)
        assert len(retorno) == 6
        assert len(capitulo7_exercicio3(self.lista_1)) == 24

    def test_capitulo7_exercicio3_3(self):
        self.load_list()
        retorno = capitulo7_exercicio3(self.lista_2, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 24
        retorno = capitulo7_exercicio3(self.lista_2, 700)
        assert len(retorno) == 39
        retorno = capitulo7_exercicio3(self.lista_2, 300)
        assert len(retorno) == 7
        assert len(capitulo7_exercicio3(self.lista_2)) == 39

    def test_capitulo7_exercicio3_4(self):
        self.load_list()
        retorno = capitulo7_exercicio3(self.lista_3, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 39
        retorno = capitulo7_exercicio3(self.lista_3, 700)
        assert len(retorno) == 61
        retorno = capitulo7_exercicio3(self.lista_3, 300)
        assert len(retorno) == 13
        assert len(capitulo7_exercicio3(self.lista_3)) == 61


class Testcapitulo7Exercicio4(LoadData):
    def test_capitulo7_exercicio4_1(self):
        self.load_list()
        retorno = capitulo7_exercicio4(self.lista, 200, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 72
        retorno = capitulo7_exercicio4(self.lista, 200, 700)
        assert len(retorno) == 124
        retorno = capitulo7_exercicio4(self.lista, 200, 300)
        assert len(retorno) == 26
        assert len(capitulo7_exercicio4(self.lista)) == 124

    def test_capitulo7_exercicio4_2(self):
        self.load_list()
        retorno = capitulo7_exercicio4(self.lista_1, 200, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 9
        retorno = capitulo7_exercicio4(self.lista_1, 200, 700)
        assert len(retorno) == 24
        retorno = capitulo7_exercicio4(self.lista_1, 200, 300)
        assert len(retorno) == 6
        assert len(capitulo7_exercicio4(self.lista_1)) == 24

    def test_capitulo7_exercicio4_3(self):
        self.load_list()
        retorno = capitulo7_exercicio4(self.lista_2, 200, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 24
        retorno = capitulo7_exercicio4(self.lista_2, 200, 700)
        assert len(retorno) == 39
        retorno = capitulo7_exercicio4(self.lista_2, 200, 300)
        assert len(retorno) == 7
        assert len(capitulo7_exercicio4(self.lista_2)) == 39

    def test_capitulo7_exercicio4_4(self):
        self.load_list()
        retorno = capitulo7_exercicio4(self.lista_3, 200, 500)
        assert isinstance(retorno, list)
        assert len(retorno) == 39
        retorno = capitulo7_exercicio4(self.lista_3, 200, 700)
        assert len(retorno) == 61
        retorno = capitulo7_exercicio4(self.lista_3, 200, 300)
        assert len(retorno) == 13
        assert len(capitulo7_exercicio4(self.lista_3)) == 61


class Testcapitulo7Exercicio5(LoadData):
    origem = 'Boston'
    origem2 = 'Salvador'
    def test_capitulo7_exercicio5_1(self):
        self.load_list()
        retorno = capitulo7_exercicio5(self.lista, self.origem)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 3
        retorno = capitulo7_exercicio5(self.lista, self.origem2)
        assert len(retorno) == 2

    def test_capitulo7_exercicio5_2(self):
        self.load_list()
        retorno = capitulo7_exercicio5(self.lista_1, self.origem)
        assert len(retorno) == 0
        retorno = capitulo7_exercicio5(self.lista_1, self.origem2)
        assert len(retorno) == 1

    def test_capitulo7_exercicio5_3(self):
        self.load_list()
        retorno = capitulo7_exercicio5(self.lista_2, self.origem)
        assert len(retorno) == 1
        retorno = capitulo7_exercicio5(self.lista_2, self.origem2)
        assert len(retorno) == 0

    def test_capitulo7_exercicio5_4(self):
        self.load_list()
        retorno = capitulo7_exercicio5(self.lista_3, self.origem)
        assert len(retorno) == 2
        retorno = capitulo7_exercicio5(self.lista_3, self.origem2)
        assert len(retorno) == 1


class Testcapitulo7Exercicio6(LoadData):
    origem = 'Russia'
    origem2 = 'China'
    def test_capitulo7_exercicio6_1(self):
        self.load_list()
        retorno = capitulo7_exercicio6(self.lista, self.origem)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert isinstance(retorno[0][1], dict)
        assert isinstance(retorno[0][2], set)
        assert len(retorno) == 9
        retorno = capitulo7_exercicio6(self.lista, self.origem2)
        assert len(retorno) == 21

    def test_capitulo7_exercicio6_2(self):
        self.load_list()
        retorno = capitulo7_exercicio6(self.lista_1, self.origem)
        assert isinstance(retorno, list)
        assert len(retorno) == 3
        retorno = capitulo7_exercicio6(self.lista_1, self.origem2)
        assert len(retorno) == 6

    def test_capitulo7_exercicio6_3(self):
        self.load_list()
        retorno = capitulo7_exercicio6(self.lista_2, self.origem)
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        retorno = capitulo7_exercicio6(self.lista_2, self.origem2)
        assert len(retorno) == 4

    def test_capitulo7_exercicio6_4(self):
        self.load_list()
        retorno = capitulo7_exercicio6(self.lista_3, self.origem)
        assert len(retorno) == 4
        retorno = capitulo7_exercicio6(self.lista_3, self.origem2)
        assert len(retorno) == 11


class Testcapitulo7Exercicio7(LoadData):
    def test_capitulo7_exercicio7_1(self):
        self.load_list()
        retorno = capitulo7_exercicio7(self.lista, 1)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 3
        assert retorno[0] == 'American Airlines'
        assert retorno[1] == 'United states'
        assert retorno[2] == 'Italy'

    def test_capitulo7_exercicio7_2(self):
        self.load_list()
        retorno = capitulo7_exercicio7(self.lista, 15)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 3
        assert retorno[0] == 'Delta Air Lines'
        assert retorno[1] == 'China'
        assert retorno[2] == 'United states'

    def test_capitulo7_exercicio7_3(self):
        self.load_list()
        retorno = capitulo7_exercicio7(self.lista, 100)
        assert isinstance(retorno, tuple)
        assert len(retorno) == 3
        assert retorno[0] == 'Lion Air'
        assert retorno[1] == 'Italy'
        assert retorno[2] == 'United states'

    def test_capitulo7_exercicio7_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio7(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio8(LoadData):
    def test_capitulo7_exercicio8_1(self):
        self.load_list()
        retorno = capitulo7_exercicio8(self.lista, 1)
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        assert retorno[0] == 'American Airlines'
        assert retorno[1] == 'United states'
        assert retorno[2] == 'Italy'
        assert retorno[3] == 99

    def test_capitulo7_exercicio8_2(self):
        self.load_list()
        retorno = capitulo7_exercicio8(self.lista, 15)
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        assert retorno[0] == 'Delta Air Lines'
        assert retorno[1] == 'China'
        assert retorno[2] == 'United states'
        assert retorno[3] == 97

    def test_capitulo7_exercicio8_3(self):
        self.load_list()
        retorno = capitulo7_exercicio8(self.lista, 100)
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        assert retorno[0] == 'Lion Air'
        assert retorno[1] == 'Italy'
        assert retorno[2] == 'United states'
        assert retorno[3] == 99

    def test_capitulo7_exercicio8_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio8(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio9(LoadData):
    def test_capitulo7_exercicio9_1(self):
        self.load_list()
        retorno = capitulo7_exercicio9(self.lista, 'CJC')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert len(retorno) == 2
        assert len(retorno[0]) == 2

    def test_capitulo7_exercicio9_2(self):
        self.load_list()
        retorno = capitulo7_exercicio9(self.lista, 'CLT')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert len(retorno) == 1
        assert len(retorno[0]) == 2

    def test_capitulo7_exercicio9_3(self):
        self.load_list()
        retorno = capitulo7_exercicio9(self.lista, 'ABC')
        assert isinstance(retorno, list)
        assert len(retorno) == 0

    def test_capitulo7_exercicio9_4(self):
        self.load_list()
        retorno = capitulo7_exercicio9(self.lista, 'ZUH')
        assert isinstance(retorno, list)
        assert isinstance(retorno[0][0], int)
        assert isinstance(retorno[0][1], dict)
        assert len(retorno) == 1
        assert len(retorno[0]) == 2


class Testcapitulo7Exercicio10(LoadData):
    def test_capitulo7_exercicio10_1(self):
        self.load_list()
        retorno = capitulo7_exercicio10(self.lista, 10)
        assert isinstance(retorno, tuple)
        assert isinstance(retorno[0], str)
        assert isinstance(retorno[1], dict)
        assert len(retorno) == 2
        assert retorno[0] == 'Malaysia Airlines'
        assert retorno[1].get('city') == 'Oberding'

    def test_capitulo7_exercicio10_2(self):
        self.load_list()
        retorno = capitulo7_exercicio10(self.lista, 15)
        assert isinstance(retorno, tuple)
        assert isinstance(retorno[0], str)
        assert isinstance(retorno[1], dict)
        assert len(retorno) == 2
        assert retorno[0] == 'Delta Air Lines'
        assert retorno[1].get('city') == 'Atlanta'

    def test_capitulo7_exercicio10_3(self):
        self.load_list()
        retorno = capitulo7_exercicio10(self.lista, 97)
        assert isinstance(retorno, tuple)
        assert isinstance(retorno[0], str)
        assert isinstance(retorno[1], dict)
        assert len(retorno) == 2
        assert retorno[0] == 'Batik Air'
        assert retorno[1].get('city') == 'Arequipa'

    def test_capitulo7_exercicio10_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio10(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio11(LoadData):
    def test_capitulo7_exercicio11_1(self):
        self.load_list()
        assert not capitulo7_exercicio11(self.lista, 80, '079.324.158-88')
        assert capitulo7_exercicio11(self.lista, 81, '079.324.158-88')
        assert not capitulo7_exercicio11(self.lista, 82, '079.324.158-88')

    def test_capitulo7_exercicio11_2(self):
        self.load_list()
        assert capitulo7_exercicio11(self.lista, 20, '129.503.846-33')
        assert not capitulo7_exercicio11(self.lista, 21, '129.503.846-33')
        assert not capitulo7_exercicio11(self.lista, 22, '129.503.846-33')

    def test_capitulo7_exercicio11_3(self):
        self.load_list()
        assert capitulo7_exercicio11(self.lista, 100, '094.528.673-29')
        assert not capitulo7_exercicio11(self.lista, 101, '094.528.673-29')
        assert not capitulo7_exercicio11(self.lista, 102, '094.528.673-29')


    def test_capitulo7_exercicio11_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio11(self.lista, 1000, '094.528.673-29')
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio12(LoadData):
    def test_capitulo7_exercicio12_1(self):
        self.load_list()
        assert not capitulo7_exercicio12(self.lista, 80, 'Sr. Davi Luiz Carvalho')
        assert capitulo7_exercicio12(self.lista, 81, 'Sr. Davi Luiz Carvalho')
        assert not capitulo7_exercicio12(self.lista, 82, 'Sr. Davi Luiz Carvalho')


    def test_capitulo7_exercicio12_2(self):
        self.load_list()
        assert capitulo7_exercicio12(self.lista, 20, 'Erick Silva')
        assert not capitulo7_exercicio12(self.lista, 21, 'Erick Silva')
        assert not capitulo7_exercicio12(self.lista, 22, 'Erick Silva')


    def test_capitulo7_exercicio12_3(self):
        self.load_list()
        assert capitulo7_exercicio12(self.lista, 100, 'Alexia Moura')
        assert not capitulo7_exercicio12(self.lista, 101, 'Alexia Moura')
        assert not capitulo7_exercicio12(self.lista, 102, 'Alexia Moura')

    def test_capitulo7_exercicio12_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio12(self.lista, 1000, 'Alexia Moura')
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio13(LoadData):
    def test_capitulo7_exercicio13_1(self):
        self.load_list()
        assert capitulo7_exercicio13(self.lista, 81, 'Sr. Davi Luiz Carvalho','079.324.158-88')
        assert capitulo7_exercicio13(self.lista, 81, 'XXXX','079.324.158-88')
        assert capitulo7_exercicio13(self.lista, 81, 'Sr. Davi Luiz Carvalho','111.111.111-11')

    def test_capitulo7_exercicio13_2(self):
        self.load_list()
        assert capitulo7_exercicio13(self.lista, 20, 'Erick Silva','129.503.846-33')
        assert capitulo7_exercicio13(self.lista, 20, 'Erick Silva','111.111.111-11')
        assert capitulo7_exercicio13(self.lista, 20, 'XXXX','129.503.846-33')

    def test_capitulo7_exercicio13_3(self):
        self.load_list()
        assert capitulo7_exercicio13(self.lista, 100, 'Alexia Moura','094.528.673-29')
        assert capitulo7_exercicio13(self.lista, 100, 'Alexia Moura','111.111.111-11')
        assert capitulo7_exercicio13(self.lista, 100, 'XXXX','094.528.673-29')

    def test_capitulo7_exercicio13_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio13(self.lista, 1000, 'Alexia Moura', '094.528.673-29')
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio14(LoadData):
    def test_capitulo7_exercicio14_1(self):
        self.load_list()
        retorno = capitulo7_exercicio14(self.lista, 'Raquel Araújo', '370.861.924-22')
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        assert retorno == [13, 43, 89, 145]
        retorno = capitulo7_exercicio14(self.lista, 'Raquel Araújo', '111.111.111-11')
        assert retorno == [13, 43, 89, 145]

    def test_capitulo7_exercicio14_2(self):
        self.load_list()
        retorno = capitulo7_exercicio14(self.lista, 'Olivia das Neves', '849.670.135-20')
        assert isinstance(retorno, list)
        assert len(retorno) == 4
        assert retorno == [118, 123, 149, 178]
        retorno = capitulo7_exercicio14(self.lista, 'Olivia das Neves', '111.111.111-11')
        assert retorno == [118, 123, 149, 178]

    def test_capitulo7_exercicio14_3(self):
        self.load_list()
        retorno = capitulo7_exercicio14(self.lista, 'Vitor Rodrigues', '971.458.320-97')
        assert isinstance(retorno, list)
        assert len(retorno) == 2
        assert retorno == [90, 195]
        retorno = capitulo7_exercicio14(self.lista, 'XXXX', '971.458.320-97')
        assert retorno == [90, 195]

    def test_capitulo7_exercicio14_4(self):
        self.load_list()
        retorno = capitulo7_exercicio14(self.lista, 'xxx', 'xxx')
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo7Exercicio15(LoadData):
    def test_capitulo7_exercicio15_1(self):
        self.load_list()
        retorno = capitulo7_exercicio15(self.lista, 'American Airlines')
        assert isinstance(retorno, list)
        assert len(retorno) == 7
        assert retorno == [1, 2, 121, 131, 135, 163, 173]

    def test_capitulo7_exercicio15_2(self):
        self.load_list()
        retorno = capitulo7_exercicio15(self.lista, 'American')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        assert retorno == []

    def test_capitulo7_exercicio15_3(self):
        self.load_list()
        retorno = capitulo7_exercicio15(self.lista, 'Qatar Airways')
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert retorno == [176]

    def test_capitulo7_exercicio15_4(self):
        self.load_list()
        retorno = capitulo7_exercicio15(self.lista, 'Qatar')
        assert isinstance(retorno, list)
        assert len(retorno) == 0
        assert retorno == []


class Testcapitulo7Exercicio16(LoadData):
    def test_capitulo7_exercicio16_1(self):
        self.load_list()
        retorno = capitulo7_exercicio16(self.lista, 'American Airlines')
        assert isinstance(retorno, list)
        assert len(retorno) == 7
        assert retorno == [1, 2, 121, 131, 135, 163, 173]

    def test_capitulo7_exercicio16_2(self):
        self.load_list()
        retorno = capitulo7_exercicio16(self.lista, 'American')
        assert isinstance(retorno, list)
        assert len(retorno) == 7
        assert retorno == [1, 2, 121, 131, 135, 163, 173]

    def test_capitulo7_exercicio16_3(self):
        self.load_list()
        retorno = capitulo7_exercicio16(self.lista, 'Qatar Airways')
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert retorno == [176]

    def test_capitulo7_exercicio16_4(self):
        self.load_list()
        retorno = capitulo7_exercicio16(self.lista, 'Qatar')
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert retorno == [176]


class Testcapitulo7Exercicio17(LoadData):
    def test_capitulo7_exercicio17_1(self):
        self.load_list()
        retorno = capitulo7_exercicio17(self.lista, 10)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {10, 'Bolivia', 'Germany', 'Malaysia Airlines'}

    def test_capitulo7_exercicio17_2(self):
        self.load_list()
        retorno = capitulo7_exercicio17(self.lista, 39)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {39, 'GoAir', 'Thailand', 'United states'}
        assert retorno == {'GoAir', 'Thailand', 39, 'United states'}

    def test_capitulo7_exercicio17_3(self):
        self.load_list()
        retorno = capitulo7_exercicio17(self.lista, 140)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {140, 'Brazil', 'China United Airlines', 'Mexico'}
        assert retorno == {'Brazil',140, 'China United Airlines', 'Mexico'}

    def test_capitulo7_exercicio17_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio17(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio18(LoadData):
    def test_capitulo7_exercicio18_1(self):
        self.load_list()
        self.load_list()
        retorno = capitulo7_exercicio18(self.lista, 10)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {10, 'Malaysia Airlines', 'Oberding', 'Tarija'}
        assert retorno == {'Malaysia Airlines', 'Oberding', 'Tarija', 10}

    def test_capitulo7_exercicio18_2(self):
        self.load_list()
        retorno = capitulo7_exercicio18(self.lista, 39)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {39, 'Boise', 'Chiang Mai', 'GoAir'}
        assert retorno == {'Boise', 'Chiang Mai', 'GoAir', 39}


    def test_capitulo7_exercicio18_3(self):
        self.load_list()
        retorno = capitulo7_exercicio18(self.lista, 140)
        assert isinstance(retorno, set)
        assert len(retorno) == 4
        assert retorno == {140, 'China United Airlines', 'Pesquería', 'Sao Jose dos Pinhais'}
        assert retorno == {'China United Airlines', 'Pesquería',140, 'Sao Jose dos Pinhais'}

    def test_capitulo7_exercicio18_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio18(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio19(LoadData):
    def test_capitulo7_exercicio19_1(self):
        self.load_list()
        retorno = capitulo7_exercicio19(self.lista, 10)
        assert isinstance(retorno, set)
        assert len(retorno) == 6
        assert retorno == {10, 'Bolivia', 'Germany', 'Malaysia Airlines', 'Oberding', 'Tarija'}

    def test_capitulo7_exercicio19_2(self):
        self.load_list()
        retorno = capitulo7_exercicio19(self.lista, 39)
        assert isinstance(retorno, set)
        assert len(retorno) == 6
        assert retorno == {39, 'Boise', 'Chiang Mai', 'GoAir', 'Thailand', 'United states'}

    def test_capitulo7_exercicio19_3(self):
        self.load_list()
        retorno = capitulo7_exercicio19(self.lista, 140)
        assert isinstance(retorno, set)
        assert len(retorno) == 6
        assert retorno == {140,'Brazil','China United Airlines','Mexico', 'Pesquería', 'Sao Jose dos Pinhais'}

    def test_capitulo7_exercicio19_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio19(self.lista, 1000)
        assert str(error.value) == msg_erro


class Testcapitulo7Exercicio20(LoadData):
    def test_capitulo7_exercicio20_1(self):
        self.load_list()
        estado = 'sp'
        trecho_cpf = '451'
        retorno = capitulo7_exercicio20(self.lista, 1, 150)
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert retorno == [('Isaac Barros', '451.287.396-19')]

    def test_capitulo7_exercicio20_2(self):
        self.load_list()
        retorno = capitulo7_exercicio20(self.lista, 1, 145)
        assert isinstance(retorno, list)
        assert len(retorno) == 1
        assert retorno == [('Luiz Henrique Cunha', '347.192.065-06')]

    def test_capitulo7_exercicio20_3(self):
        self.load_list()
        retorno = capitulo7_exercicio20(self.lista, 1, 140)
        assert isinstance(retorno, list)
        assert len(retorno) == 3

    def test_capitulo7_exercicio8_4(self):
        self.load_list()
        msg_erro = "ID não encontrado."
        with pytest.raises(IndexError) as error:
            capitulo7_exercicio20(self.lista, 1, 1000)
        assert str(error.value) == msg_erro
