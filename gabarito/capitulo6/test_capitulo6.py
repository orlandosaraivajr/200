from capitulo6  import capitulo6_exercicio1
from capitulo6  import capitulo6_exercicio2
from capitulo6  import capitulo6_exercicio3
from capitulo6  import capitulo6_exercicio4
from capitulo6  import capitulo6_exercicio5
from capitulo6  import capitulo6_exercicio6
from capitulo6  import capitulo6_exercicio7
from capitulo6  import capitulo6_exercicio8
from capitulo6  import capitulo6_exercicio9
from capitulo6  import capitulo6_exercicio10
from capitulo6  import capitulo6_exercicio11
from capitulo6  import capitulo6_exercicio12
from capitulo6  import capitulo6_exercicio13
from capitulo6  import capitulo6_exercicio14
from capitulo6  import capitulo6_exercicio15
from capitulo6  import capitulo6_exercicio16
from capitulo6  import capitulo6_exercicio17
from capitulo6  import capitulo6_exercicio18
from capitulo6  import capitulo6_exercicio19
from capitulo6  import capitulo6_exercicio20

import pickle
import pytest

class LoadData:
    def load_list(self):
        try:
            with open('../capitulo6.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:5000]
                self.lista_2 = self.lista[5001:10000]
                self.lista_3 = self.lista[10002:15000]
        except FileNotFoundError:
            with open('capitulo6.bin', 'rb') as list_in_file:
                self.lista = pickle.load(list_in_file)
                self.lista_1 = self.lista[0:5000]
                self.lista_2 = self.lista[5001:10000]
                self.lista_3 = self.lista[10002:15000]
 
class Testcapitulo6Exercicio1(LoadData):
    def test_capitulo6_exercicio1_1(self):
        self.load_list()
        retorno = capitulo6_exercicio1(self.lista)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 1067

    def test_capitulo6_exercicio1_2(self):
        self.load_list()
        retorno = capitulo6_exercicio1(self.lista_1)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 358

    def test_capitulo6_exercicio1_3(self):
        self.load_list()
        retorno = capitulo6_exercicio1(self.lista_2)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 340

    def test_capitulo6_exercicio1_4(self):
        self.load_list()
        retorno = capitulo6_exercicio1(self.lista_3)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 369


class Testcapitulo6Exercicio2(LoadData):
    def test_capitulo6_exercicio2_1(self):
        self.load_list()
        retorno = capitulo6_exercicio2(self.lista)
        assert isinstance(retorno, int)
        assert retorno == 1067

    def test_capitulo6_exercicio2_2(self):
        self.load_list()
        retorno = capitulo6_exercicio2(self.lista_1)
        assert isinstance(retorno, int)
        assert retorno == 358

    def test_capitulo6_exercicio2_3(self):
        self.load_list()
        retorno = capitulo6_exercicio2(self.lista_2)
        assert isinstance(retorno, int)
        assert retorno == 340

    def test_capitulo6_exercicio2_4(self):
        self.load_list()
        retorno = capitulo6_exercicio2(self.lista_3)
        assert isinstance(retorno, int)
        assert retorno == 369


class Testcapitulo6Exercicio3(LoadData):
    def test_capitulo6_exercicio3_1(self):
        self.load_list()
        retorno = capitulo6_exercicio3(self.lista)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 448

    def test_capitulo6_exercicio3_2(self):
        self.load_list()
        retorno = capitulo6_exercicio3(self.lista_1)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 152

    def test_capitulo6_exercicio3_3(self):
        self.load_list()
        retorno = capitulo6_exercicio3(self.lista_2)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 149

    def test_capitulo6_exercicio3_4(self):
        self.load_list()
        retorno = capitulo6_exercicio3(self.lista_3)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 147


class Testcapitulo6Exercicio4(LoadData):
    def test_capitulo6_exercicio4_1(self):
        self.load_list()
        retorno = capitulo6_exercicio4(self.lista)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 619

    def test_capitulo6_exercicio4_2(self):
        self.load_list()
        retorno = capitulo6_exercicio4(self.lista_1)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 206

    def test_capitulo6_exercicio4_3(self):
        self.load_list()
        retorno = capitulo6_exercicio4(self.lista_2)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 191

    def test_capitulo6_exercicio4_4(self):
        self.load_list()
        retorno = capitulo6_exercicio4(self.lista_3)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], str)
        assert len(retorno) == 222


class Testcapitulo6Exercicio5(LoadData):
    sobrenome = 'Silva'
    sobrenome2 = 'Aragão'
    def test_capitulo6_exercicio5_1(self):
        self.load_list()
        retorno = capitulo6_exercicio5(self.lista, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 226
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio5(self.lista, self.sobrenome2)
        assert len(retorno) == 213

    def test_capitulo6_exercicio5_2(self):
        self.load_list()
        retorno = capitulo6_exercicio5(self.lista_1, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 65
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio5(self.lista_1, self.sobrenome2)
        assert len(retorno) == 78

    def test_capitulo6_exercicio5_3(self):
        self.load_list()
        retorno = capitulo6_exercicio5(self.lista_2, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 87
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio5(self.lista_2, self.sobrenome2)
        assert len(retorno) == 71

    def test_capitulo6_exercicio5_4(self):
        self.load_list()
        retorno = capitulo6_exercicio5(self.lista_3, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 74
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio5(self.lista_3, self.sobrenome2)
        assert len(retorno) == 64


class Testcapitulo6Exercicio6(LoadData):
    sobrenome = 'Silva'
    sobrenome2 = 'Aragão'
    def test_capitulo6_exercicio6_1(self):
        self.load_list()
        retorno = capitulo6_exercicio6(self.lista, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 10
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio6(self.lista, self.sobrenome2)
        assert len(retorno) == 10

    def test_capitulo6_exercicio6_2(self):
        self.load_list()
        retorno = capitulo6_exercicio6(self.lista_1, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 10
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio6(self.lista_1, self.sobrenome2)
        assert len(retorno) == 10

    def test_capitulo6_exercicio6_3(self):
        self.load_list()
        retorno = capitulo6_exercicio6(self.lista_2, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 10
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio6(self.lista_2, self.sobrenome2)
        assert len(retorno) == 10

    def test_capitulo6_exercicio6_4(self):
        self.load_list()
        retorno = capitulo6_exercicio6(self.lista_3, self.sobrenome)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno) == 10
        assert len(retorno[0]) == 2
        retorno = capitulo6_exercicio6(self.lista_3, self.sobrenome2)
        assert len(retorno) == 10


class Testcapitulo6Exercicio7(LoadData):
    def test_capitulo6_exercicio7_1(self):
        self.load_list()
        email = 'moraesluana@yahoo.com.br'
        retorno = capitulo6_exercicio7(self.lista, email)
        assert isinstance(retorno, tuple)
        assert retorno[0] == 'Letícia Aragão'
        assert retorno[-1] == '02/33'

    def test_capitulo6_exercicio7_2(self):
        self.load_list()
        email = 'moraesluana@yahoo.com.br'
        retorno = capitulo6_exercicio7(self.lista_1, email)
        assert isinstance(retorno, tuple)
        assert retorno[0] == 'Letícia Aragão'
        assert retorno[-1] == '02/33'

    def test_capitulo6_exercicio7_3(self):
        self.load_list()
        email = 'fariasenzo@correia.br'
        retorno = capitulo6_exercicio7(self.lista_2, email)
        assert isinstance(retorno, tuple)
        assert retorno[0] == 'Eloah Fogaça'
        assert retorno[-1] == '08/24'

    def test_capitulo6_exercicio7_4(self):
        self.load_list()
        email = 'eduardo68@hotmail.com'
        retorno = capitulo6_exercicio7(self.lista_3, email)
        assert isinstance(retorno, tuple)
        assert retorno[0] == 'Leandro Nogueira'
        assert retorno[-1] == '04/26'


class Testcapitulo6Exercicio8(LoadData):
    def test_capitulo6_exercicio8_1(self):
        self.load_list()
        retorno = capitulo6_exercicio8(self.lista)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert retorno[0][1] == '971.628.345-82'
        assert len(retorno[0]) == 6
        assert len(retorno) == 1270

    def test_capitulo6_exercicio8_2(self):
        self.load_list()
        email = 'hotmail.com'
        retorno = capitulo6_exercicio8(self.lista_1, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 409

    def test_capitulo6_exercicio8_3(self):
        self.load_list()
        email = 'yahoo.com.br'
        retorno = capitulo6_exercicio8(self.lista_2, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 421

    def test_capitulo6_exercicio8_4(self):
        self.load_list()
        email = 'xyx.com.br'
        retorno = capitulo6_exercicio8(self.lista_3, email)
        assert isinstance(retorno, list)
        assert len(retorno) == 0


class Testcapitulo6Exercicio9(LoadData):
    def test_capitulo6_exercicio9_1(self):
        self.load_list()
        email = 'cardosomaria-clara'
        retorno = capitulo6_exercicio9(self.lista, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 2
        email = 'luiz-felipecarvalho'
        retorno = capitulo6_exercicio9(self.lista, email)
        assert len(retorno) == 1
        email = 'costelaisis'
        retorno = capitulo6_exercicio9(self.lista, email)
        assert len(retorno) == 1

    def test_capitulo6_exercicio9_2(self):
        self.load_list()
        email = 'luiz-felipecarvalho'
        retorno = capitulo6_exercicio9(self.lista_1, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio9_3(self):
        self.load_list()
        email = 'costelaisis'
        retorno = capitulo6_exercicio9(self.lista_2, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio9_4(self):
        self.load_list()
        email = 'cardosomaria-clara'
        retorno = capitulo6_exercicio9(self.lista_3, email)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1


class Testcapitulo6Exercicio10(LoadData):
    def test_capitulo6_exercicio10_1(self):
        self.load_list()
        trecho_endereco = 'Praia de Nunes, 229\nComiteco\n41915587 Nogueira de Costa / SC'
        retorno = capitulo6_exercicio10(self.lista, trecho_endereco)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert retorno[0][0] == 'Yasmin Rodrigues'
        assert len(retorno) == 1
        trecho_endereco = 'Praia de Nunes, 229'
        retorno = capitulo6_exercicio10(self.lista, trecho_endereco)
        assert retorno[0][0] == 'Yasmin Rodrigues'
        assert len(retorno) == 1

    def test_capitulo6_exercicio10_2(self):
        self.load_list()
        trecho_endereco = 'Praia de Nunes, 229\nComiteco\n41915587 Nogueira de Costa / SC'
        retorno = capitulo6_exercicio10(self.lista_1, trecho_endereco)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert retorno[0][0] == 'Yasmin Rodrigues'
        assert len(retorno) == 1
        trecho_endereco = 'Praia de Nunes, 229'
        retorno = capitulo6_exercicio10(self.lista, trecho_endereco)
        assert retorno[0][0] == 'Yasmin Rodrigues'
        assert len(retorno) == 1

    def test_capitulo6_exercicio10_3(self):
        self.load_list()
        trecho_endereco = 'Recanto Viana, 542\nUniversitário\n65799316 Moreira / PI'
        retorno = capitulo6_exercicio10(self.lista_2, trecho_endereco)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert retorno[0][0] == 'Miguel Fernandes'
        assert len(retorno) == 1
        trecho_endereco = 'Recanto Viana, 542'
        retorno = capitulo6_exercicio10(self.lista_2, trecho_endereco)
        assert len(retorno) == 1
        assert retorno[0][0] == 'Miguel Fernandes'
        assert len(retorno) == 1

    def test_capitulo6_exercicio10_4(self):
        self.load_list()
        trecho_endereco = 'Setor Azevedo, 891\nUnião\n46309837 Rodrigues / MA'
        retorno = capitulo6_exercicio10(self.lista_3, trecho_endereco)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert retorno[0][0] == 'Stella Vieira'
        assert len(retorno) == 1


class Testcapitulo6Exercicio11(LoadData):
    def test_capitulo6_exercicio11_1(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio11(self.lista, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 540
        estado = 'SP'
        retorno = capitulo6_exercicio11(self.lista, estado)
        assert len(retorno) == 591

    def test_capitulo6_exercicio11_2(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio11(self.lista_1, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 181
        estado = 'SP'
        retorno = capitulo6_exercicio11(self.lista_1, estado)
        assert len(retorno) == 189

    def test_capitulo6_exercicio11_3(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio11(self.lista_2, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 185
        estado = 'SP'
        retorno = capitulo6_exercicio11(self.lista_2, estado)
        assert len(retorno) == 202

    def test_capitulo6_exercicio11_4(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio11(self.lista_3, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 174
        estado = 'SP'
        retorno = capitulo6_exercicio11(self.lista_3, estado)
        assert len(retorno) == 199


class Testcapitulo6Exercicio12(LoadData):
    def test_capitulo6_exercicio12_1(self):
        self.load_list()
        numero_cartao = '6011709357464080'
        retorno = capitulo6_exercicio12(self.lista, numero_cartao)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio12_2(self):
        self.load_list()
        numero_cartao = '6011709357464080'
        retorno = capitulo6_exercicio12(self.lista_1, numero_cartao)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio12_3(self):
        self.load_list()
        numero_cartao = '36420578601195'
        retorno = capitulo6_exercicio12(self.lista_2, numero_cartao)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio12_4(self):
        self.load_list()
        numero_cartao = '6503668914086049'
        retorno = capitulo6_exercicio12(self.lista_3, numero_cartao)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1


class Testcapitulo6Exercicio13(LoadData):
    def test_capitulo6_exercicio13_1(self):
        self.load_list()
        mes_ano_vencimento = '03/26'
        retorno = capitulo6_exercicio13(self.lista, mes_ano_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 123

    def test_capitulo6_exercicio13_2(self):
        self.load_list()
        mes_ano_vencimento = '03/26'
        retorno = capitulo6_exercicio13(self.lista_1, mes_ano_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 48

    def test_capitulo6_exercicio13_3(self):
        self.load_list()
        mes_ano_vencimento = '03/26'
        retorno = capitulo6_exercicio13(self.lista_2, mes_ano_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 37

    def test_capitulo6_exercicio13_4(self):
        self.load_list()
        mes_ano_vencimento = '03/26'
        retorno = capitulo6_exercicio13(self.lista_3, mes_ano_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 38


class Testcapitulo6Exercicio14(LoadData):
    def test_capitulo6_exercicio14_1(self):
        self.load_list()
        mes_vencimento = 3
        retorno = capitulo6_exercicio14(self.lista, mes_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1290

    def test_capitulo6_exercicio14_2(self):
        self.load_list()
        mes_vencimento = '03'
        retorno = capitulo6_exercicio14(self.lista_1, mes_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 430

    def test_capitulo6_exercicio14_3(self):
        self.load_list()
        mes_vencimento = '03'
        retorno = capitulo6_exercicio14(self.lista_2, mes_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 447

    def test_capitulo6_exercicio14_4(self):
        self.load_list()
        mes_vencimento = '03'
        retorno = capitulo6_exercicio14(self.lista_3, mes_vencimento)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 413


class Testcapitulo6Exercicio15(LoadData):
    def test_capitulo6_exercicio15_1(self):
        self.load_list()
        cpf = '263.041.897-96'
        retorno = capitulo6_exercicio15(self.lista, cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 3
        assert len(retorno) == 1
        assert retorno[0][0] == 'Bárbara Rocha'

    def test_capitulo6_exercicio15_2(self):
        self.load_list()
        cpf = '679.403.521-99'
        retorno = capitulo6_exercicio15(self.lista_1, cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 3
        assert len(retorno) == 1
        assert retorno[0][0] == 'Dra. Letícia Cavalcanti'

    def test_capitulo6_exercicio15_3(self):
        self.load_list()
        cpf = '295.164.308-05'
        retorno = capitulo6_exercicio15(self.lista_2, cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 3
        assert len(retorno) == 1
        assert retorno[0][0] == 'Helena Porto'

    def test_capitulo6_exercicio15_4(self):
        self.load_list()
        cpf = '801.457.926-76'
        retorno = capitulo6_exercicio15(self.lista_3, cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 3
        assert len(retorno) == 1
        assert retorno[0][0] == 'Diogo da Costa'


class Testcapitulo6Exercicio16(LoadData):
    def test_capitulo6_exercicio16_1(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio16(self.lista, estado, 3)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 61
        estado = 'SP'
        retorno = capitulo6_exercicio16(self.lista, estado, 3)
        assert len(retorno) == 46

    def test_capitulo6_exercicio16_2(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio16(self.lista_1, estado,3)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 17
        estado = 'SP'
        retorno = capitulo6_exercicio16(self.lista_1, estado,3)
        assert len(retorno) == 17

    def test_capitulo6_exercicio16_3(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio16(self.lista_2, estado,3)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 26
        estado = 'SP'
        retorno = capitulo6_exercicio16(self.lista_2, estado,3)
        assert len(retorno) == 13

    def test_capitulo6_exercicio11_4(self):
        self.load_list()
        estado = 'SC'
        retorno = capitulo6_exercicio16(self.lista_3, estado,3)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 18
        estado = 'SP'
        retorno = capitulo6_exercicio16(self.lista_3, estado, 3)
        assert len(retorno) == 16


class Testcapitulo6Exercicio17(LoadData):
    def test_capitulo6_exercicio17_1(self):
        self.load_list()
        trecho_endereco = 'Rua'
        sobrenome = 'Silva'
        retorno = capitulo6_exercicio17(self.lista, trecho_endereco, sobrenome)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 2
        assert len(retorno) == 5
        trecho_endereco = 'Avenida'
        retorno = capitulo6_exercicio17(self.lista, trecho_endereco, sobrenome)
        assert len(retorno) == 7

    def test_capitulo6_exercicio17_2(self):
        self.load_list()
        trecho_endereco = 'Rua'
        sobrenome = 'Ribeiro'
        retorno = capitulo6_exercicio17(self.lista_1, trecho_endereco, sobrenome)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 2
        assert len(retorno) == 2
        trecho_endereco = 'Avenida'
        retorno = capitulo6_exercicio17(self.lista, trecho_endereco, sobrenome)
        assert len(retorno) == 5

    def test_capitulo6_exercicio17_3(self):
        self.load_list()
        trecho_endereco = 'Rua'
        sobrenome = 'Silva'
        retorno = capitulo6_exercicio17(self.lista_2, trecho_endereco, sobrenome)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 2
        assert len(retorno) == 4
        trecho_endereco = 'Avenida'
        retorno = capitulo6_exercicio17(self.lista_2, trecho_endereco, sobrenome)
        assert len(retorno) == 3

    def test_capitulo6_exercicio17_4(self):
        self.load_list()
        trecho_endereco = 'Rua'
        sobrenome = 'Silva'
        retorno = capitulo6_exercicio17(self.lista_3, trecho_endereco, sobrenome)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 2
        assert len(retorno) == 1


class Testcapitulo6Exercicio18(LoadData):
    def test_capitulo6_exercicio18_1(self):
        self.load_list()
        dominio = 'gmail.com'
        estado = 'SP'
        retorno = capitulo6_exercicio18(self.lista, dominio, estado)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno[0]) == 6
        assert len(retorno) == 49

    def test_capitulo6_exercicio18_2(self):
        self.load_list()
        dominio = 'gmail.com'
        estado = 'SP'
        retorno = capitulo6_exercicio18(self.lista_1, dominio, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 15
        dominio = 'hotmail.com'
        retorno = capitulo6_exercicio18(self.lista_1, dominio, estado)
        assert len(retorno) == 16

    def test_capitulo6_exercicio18_3(self):
        self.load_list()
        dominio = 'gmail.com'
        estado = 'SP'
        retorno = capitulo6_exercicio18(self.lista_2, dominio, estado)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 16
        dominio = 'hotmail.com'
        retorno = capitulo6_exercicio18(self.lista_2, dominio, estado)
        assert len(retorno) == 21

    def test_capitulo6_exercicio18_4(self):
        self.load_list()
        dominio = 'gmail.com'
        estado = 'SP'
        retorno = capitulo6_exercicio18(self.lista_3, dominio, estado)
        assert isinstance(retorno, list)
        assert len(retorno) == 18
        dominio = 'hotmail.com'
        retorno = capitulo6_exercicio18(self.lista_3, dominio, estado)
        assert len(retorno) == 13


class Testcapitulo6Exercicio19(LoadData):
    def test_capitulo6_exercicio19_1(self):
        self.load_list()
        trecho_nome = 'Thiago'
        trecho_cpf = '451'
        retorno = capitulo6_exercicio19(self.lista, trecho_nome, trecho_cpf)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno[0]) == 6
        assert len(retorno) == 2

    def test_capitulo6_exercicio19_2(self):
        self.load_list()
        trecho_nome = 'Maria'
        trecho_cpf = '295'
        retorno = capitulo6_exercicio19(self.lista_1, trecho_nome, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 5

    def test_capitulo6_exercicio19_3(self):
        self.load_list()
        trecho_nome = 'Isabel'
        trecho_cpf = '925'
        retorno = capitulo6_exercicio19(self.lista_2, trecho_nome, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 1

    def test_capitulo6_exercicio19_4(self):
        self.load_list()
        trecho_nome = 'Fernando'
        trecho_cpf = '621'
        retorno = capitulo6_exercicio19(self.lista_3, trecho_nome, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno) == 3


class Testcapitulo6Exercicio20(LoadData):
    def test_capitulo6_exercicio20_1(self):
        self.load_list()
        estado = 'sp'
        trecho_cpf = '451'
        retorno = capitulo6_exercicio20(self.lista, estado, trecho_cpf)
        assert isinstance(retorno, list)
        assert isinstance(retorno[0], tuple)
        assert len(retorno[0]) == 6
        assert len(retorno) == 9

    def test_capitulo6_exercicio20_2(self):
        self.load_list()
        estado = 'sp'
        trecho_cpf = '295'
        retorno = capitulo6_exercicio20(self.lista_1, estado, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 3

    def test_capitulo6_exercicio20_3(self):
        self.load_list()
        estado = 'sp'
        trecho_cpf = '925'
        retorno = capitulo6_exercicio20(self.lista_2, estado, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno[0]) == 6
        assert len(retorno) == 2

    def test_capitulo6_exercicio20_4(self):
        self.load_list()
        estado = 'SP'
        trecho_cpf = '925'
        retorno = capitulo6_exercicio20(self.lista_3, estado, trecho_cpf)
        assert isinstance(retorno, list)
        assert len(retorno) == 3
