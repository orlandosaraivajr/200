from capitulo5 import capitulo5_exercicio1
from capitulo5 import capitulo5_exercicio2
from capitulo5 import capitulo5_exercicio3
from capitulo5 import capitulo5_exercicio4
from capitulo5 import capitulo5_exercicio5
from capitulo5 import capitulo5_exercicio6
from capitulo5 import capitulo5_exercicio7
from capitulo5 import capitulo5_exercicio8
from capitulo5 import capitulo5_exercicio9
from capitulo5 import capitulo5_exercicio10
from capitulo5 import capitulo5_exercicio11
from capitulo5 import capitulo5_exercicio12
from capitulo5 import capitulo5_exercicio13
from capitulo5 import capitulo5_exercicio14
from capitulo5 import capitulo5_exercicio15
from capitulo5 import capitulo5_exercicio16
from capitulo5 import capitulo5_exercicio17
from capitulo5 import capitulo5_exercicio18
from capitulo5 import capitulo5_exercicio19
from capitulo5 import capitulo5_exercicio20

import pytest
from pytest import approx

class Testcapitulo5Exercicio1():
    def test_capitulo5_exercicio1_1(self):
        msg_erro = "Necessário digitar um número"
        with pytest.raises(ValueError) as error:
            capitulo5_exercicio1([], 'palavra')
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio2_2(self):
        retorno = capitulo5_exercicio1([1 , 2 , 3], 1)
        assert retorno == [1 , 2 , 3 , 1 ]

    def test_capitulo5_exercicio2_3(self):
        retorno = capitulo5_exercicio1([], 10)
        assert retorno == [10]

    def test_capitulo5_exercicio2_4(self):
        retorno = capitulo5_exercicio1([1,2,3,4,5], 10.2)
        assert retorno == [1,2,3,4,5,10.2]


class Testcapitulo5Exercicio2():
    def test_capitulo5_exercicio2_1(self, monkeypatch):
        responses = iter(['Palavra'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        msg_erro = "Necessário digitar um número ponto-flutuante"
        with pytest.raises(ValueError) as error:
            capitulo5_exercicio2([])
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio2_2(self, monkeypatch):
        responses = iter([12.5])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo5_exercicio2([])
        assert retorno == [12.5]

    def test_capitulo5_exercicio2_3(self, monkeypatch):
        responses = iter([12])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo5_exercicio2([])
        assert retorno == [12]

    def test_capitulo5_exercicio2_4(self, monkeypatch):
        responses = iter(['6'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo5_exercicio2([1,2,3])
        assert retorno == [1 , 2 , 3 , 6]


class Testcapitulo5Exercicio3():
    def test_capitulo5_exercicio3_1(self):
        lista_in = [1,2,3,'oi',4]
        lista_out = [1,2,3,4]
        assert capitulo5_exercicio3(lista_in) == lista_out

    def test_capitulo5_exercicio3_2(self):
        lista_in = ['1','2','3','oi','4']
        lista_out = []
        assert capitulo5_exercicio3(lista_in) == lista_out

    def test_capitulo5_exercicio3_3(self):
        lista_in = [1.1, 2 ,'3','oi', 4]
        lista_out = [2, 4]
        assert capitulo5_exercicio3(lista_in) == lista_out

    def test_capitulo5_exercicio3_4(self):
        lista_in = [1, 2 ,'3','oi',4]
        lista_out = [1, 2, 4]
        assert capitulo5_exercicio3(lista_in) == lista_out
        

class Testcapitulo5Exercicio4():
    def test_capitulo5_exercicio4_1(self):
        lista_in = [1 , 2 , 3 , 4]
        param1 = 'oi mundo'
        assert capitulo5_exercicio4(lista_in, param1) == [1 , 2 , 3 , 4, 'oi mundo']

    def test_capitulo5_exercicio4_2(self):
        lista_in = [1 , 2 , 3 , 4]
        param1 = 20
        assert capitulo5_exercicio4(lista_in, param1) == lista_in

    def test_capitulo5_exercicio4_3(self):
        lista_in = [1 , 2 , 3 , 4]
        param1 = ['oi', 'mundo']
        assert capitulo5_exercicio4(lista_in, param1) == lista_in

    def test_capitulo5_exercicio4_4(self):
        lista_in = [1 , 2 , 3 , 4]
        param1 = 20.5
        assert capitulo5_exercicio4(lista_in, param1) == lista_in
        

class Testcapitulo5Exercicio5():
    def test_capitulo5_exercicio5_1(self):
        lista_in = [1 , 2 , 3 , 4]
        assert capitulo5_exercicio5(lista_in) == 4

    def test_capitulo5_exercicio5_2(self):
        lista_in = [1 , 2 ]
        assert capitulo5_exercicio5(lista_in) == 2

    def test_capitulo5_exercicio5_3(self):
        string_in = 'oi mundo'
        assert capitulo5_exercicio5(string_in) == 8
        string_in = 'oi'
        assert capitulo5_exercicio5(string_in) == 2

    def test_capitulo5_exercicio5_4(self):
        lista_in = []
        assert capitulo5_exercicio5(lista_in) == 0
        lista_in = [[1,2], [3,4]]
        assert capitulo5_exercicio5(lista_in) == 2

 
class Testcapitulo5Exercicio6():
    def test_capitulo5_exercicio6_1(self):
        lista_in = [1 , 2 , 3 , 4]
        assert capitulo5_exercicio6(lista_in) == 4

    def test_capitulo5_exercicio6_2(self):
        lista_in = [1 , 2 ]
        assert capitulo5_exercicio6(lista_in) == 2

    def test_capitulo5_exercicio6_3(self):
        string_in = 'oi mundo'
        msg_erro = "O argumento precisa ser lista"
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio6(string_in)
        assert str(error.value) == msg_erro

        string_in = 'oi'
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio6(string_in)
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio6_4(self):
        lista_in = []
        assert capitulo5_exercicio6(lista_in) == 0
        lista_in = [[1,2], [3,4]]
        assert capitulo5_exercicio6(lista_in) == 2


class Testcapitulo5Exercicio7():
    def test_capitulo5_exercicio7_1(self):
        lista_in = [1 ,'oi', 2 ,'mundo', 3 , 4]
        assert capitulo5_exercicio7(lista_in) == ['oi','mundo']

    def test_capitulo5_exercicio7_2(self):
        lista_in = [1 , 2 ]
        assert capitulo5_exercicio7(lista_in) == []

    def test_capitulo5_exercicio7_3(self):
        lista_in_fail = 'oi mundo'
        msg_erro = "O argumento precisa ser lista"
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio7(lista_in_fail)
        assert str(error.value) == msg_erro

        lista_in_fail = 42
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio7(lista_in_fail)
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio7_4(self):
        lista_in = []
        assert capitulo5_exercicio7(lista_in) == []
        lista_in = [[1,2], [3,4]]
        assert capitulo5_exercicio7(lista_in) == []


class Testcapitulo5Exercicio8():
    def test_capitulo5_exercicio8_1(self):
        lista_in = [1 ,'oi', 2 ,'mundo', 3 , 4]
        assert capitulo5_exercicio8(lista_in) == 2

    def test_capitulo5_exercicio8_2(self):
        lista_in = [1 , 2 ]
        assert capitulo5_exercicio8(lista_in) == 0

    def test_capitulo5_exercicio8_3(self):
        lista_in_fail = 'oi mundo'
        msg_erro = "O argumento precisa ser lista"
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio8(lista_in_fail)
        assert str(error.value) == msg_erro

        lista_in_fail = 42
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio8(lista_in_fail)
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio8_4(self):
        lista_in = []
        assert capitulo5_exercicio8(lista_in) == 0
        lista_in = [[1,2], [3,4]]
        assert capitulo5_exercicio8(lista_in) == 0


class Testcapitulo5Exercicio9():
    def test_capitulo5_exercicio9_1(self):
        lista_in = [1 ,'oi', 2 ,'mundo', 3 , 4]
        assert capitulo5_exercicio9(lista_in) == 10

    def test_capitulo5_exercicio9_2(self):
        lista_in = [1 , 2 ]
        assert capitulo5_exercicio9(lista_in) == 3

    def test_capitulo5_exercicio9_3(self):
        lista_in_fail = 'oi mundo'
        msg_erro = "O argumento precisa ser lista"
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio9(lista_in_fail)
        assert str(error.value) == msg_erro

        lista_in_fail = 42
        with pytest.raises(TypeError) as error:
                capitulo5_exercicio9(lista_in_fail)
        assert str(error.value) == msg_erro

    def test_capitulo5_exercicio9_4(self):
        lista_in = []
        assert capitulo5_exercicio9(lista_in) == 0
        lista_in = [5,5,5,10]
        assert capitulo5_exercicio9(lista_in) == 25


class Testcapitulo5Exercicio10():
    def test_capitulo5_exercicio10_1(self):
        lista_in = [1,2.0,3,'oi',4.2]
        lista_out = [2.0, 4.2]
        assert capitulo5_exercicio10(lista_in) == lista_out

    def test_capitulo5_exercicio10_2(self):
        lista_in = ['1','2',3,'oi',4.2]
        lista_out = [4.2]
        assert capitulo5_exercicio10(lista_in) == lista_out

    def test_capitulo5_exercicio10_3(self):
        lista_in = [1.1, 2 ,'3','oi', 4.2]
        lista_out = [1.1, 4.2]
        assert capitulo5_exercicio10(lista_in) == lista_out

    def test_capitulo5_exercicio10_4(self):
        lista_in = [1, 2 ,'3','oi',4]
        lista_out = []
        assert capitulo5_exercicio10(lista_in) == lista_out


class Testcapitulo5Exercicio11():
    def test_capitulo5_exercicio11_1(self):
        lista_in = [1,2.0 , 3,'oi',4.2]
        lista_out = [1, 3, 2.0, 4.2]
        assert capitulo5_exercicio11(lista_in) == lista_out

    def test_capitulo5_exercicio11_2(self):
        lista_in = ['1','2',3,'oi',4.2]
        lista_out = [3, 4.2]
        assert capitulo5_exercicio11(lista_in) == lista_out

    def test_capitulo5_exercicio11_3(self):
        lista_in = [1.1, 2 ,'3','oi', 4.2]
        lista_out = [2, 1.1, 4.2]
        assert capitulo5_exercicio11(lista_in) == lista_out

    def test_capitulo5_exercicio11_4(self):
        lista_in = [1, 2 ,'3','oi',4]
        lista_out = [1, 2, 4]
        assert capitulo5_exercicio11(lista_in) == lista_out


class Testcapitulo5Exercicio12():
    def test_capitulo5_exercicio12_1(self):
        lista_in = [1,2.0 , 3,'oi',4.2]
        lista_out = [2.0, 4.2, 1, 3]
        assert capitulo5_exercicio12(lista_in) == lista_out

    def test_capitulo5_exercicio12_2(self):
        lista_in = ['1','2',3,'oi',4.2]
        lista_out = [4.2, 3]
        assert capitulo5_exercicio12(lista_in) == lista_out

    def test_capitulo5_exercicio12_3(self):
        lista_in = [1.1, 2 ,'3','oi', 4.2]
        lista_out = [ 1.1, 4.2, 2]
        assert capitulo5_exercicio12(lista_in) == lista_out

    def test_capitulo5_exercicio12_4(self):
        lista_in = [1, 2 ,'3','oi',4]
        lista_out = [1, 2, 4]
        assert capitulo5_exercicio12(lista_in) == lista_out


class Testcapitulo5Exercicio13():
    def test_capitulo5_exercicio13_1(self):
        lista_in = [1, 2.0 , 3,'oi',4.2]
        lista_out = [1, 4.2]
        assert capitulo5_exercicio13(lista_in) == lista_out

    def test_capitulo5_exercicio13_2(self):
        lista_in = ['1','2',3,'oi',4.2]
        lista_out = ['1',4.2]
        assert capitulo5_exercicio13(lista_in) == lista_out

    def test_capitulo5_exercicio13_3(self):
        lista_in = [1.1, 2 ,'3','oi', 4.2]
        lista_out = [ 1.1, 4.2]
        assert capitulo5_exercicio13(lista_in) == lista_out

    def test_capitulo5_exercicio13_4(self):
        lista_in = [1]
        lista_out = []
        assert capitulo5_exercicio13(lista_in) == lista_out


class Testcapitulo5Exercicio14():
    def test_capitulo5_exercicio14_1(self):
        lista_in = [1, 2.0 ,[], 3,'oi',4.2, [5,6]]
        lista_out = [[],[5,6]]
        assert capitulo5_exercicio14(lista_in) == lista_out

    def test_capitulo5_exercicio14_2(self):
        lista_in = ['1',[1,2,3], '2', ['a','b',3] , 3,'oi',4.2]
        lista_out = [[1,2,3],['a','b',3]]
        assert capitulo5_exercicio14(lista_in) == lista_out

    def test_capitulo5_exercicio14_3(self):
        lista_in = [[1, 1], [2,2] ,'3','oi', 4.2]
        lista_out = [[1, 1], [2,2]]
        assert capitulo5_exercicio14(lista_in) == lista_out

    def test_capitulo5_exercicio14_4(self):
        lista_in = [1]
        lista_out = []
        assert capitulo5_exercicio14(lista_in) == lista_out


class Testcapitulo5Exercicio15():
    def test_capitulo5_exercicio15_1(self):
        lista_in = [1.2,'mundo', 1, 2]
        item = 1.2
        assert capitulo5_exercicio15(lista_in, item)

    def test_capitulo5_exercicio15_2(self):
        lista_in = ['Oi','mundo']
        item = 'mundo'
        assert capitulo5_exercicio15(lista_in, item)
        item = 'Mundo'
        assert not capitulo5_exercicio15(lista_in, item)

    def test_capitulo5_exercicio15_3(self):
        lista_in = [[1, 1], [2,2] ,'3','oi', 4.2]
        item = [1, 1]
        assert capitulo5_exercicio15(lista_in, item)
        item = (1, 1)
        assert not capitulo5_exercicio15(lista_in, item)

    def test_capitulo5_exercicio15_4(self):
        lista_in = [1, 2, 3 , 4 , 1]
        item = 1
        assert capitulo5_exercicio15(lista_in, item)
        item = '1'
        assert not capitulo5_exercicio15(lista_in, item)


class Testcapitulo5Exercicio16():
    def test_capitulo5_exercicio16_1(self):
        lista_in = [1, 2, 3]
        assert capitulo5_exercicio16(lista_in) == lista_in
        lista_in = [1, 2, 3 , 4 , 5]
        assert capitulo5_exercicio16(lista_in) == lista_in

    def test_capitulo5_exercicio16_2(self):
        lista_in = ['1',[1,2,3], '2', ['a','b',3] , 3,'oi',4.2]
        lista_out = [[1, 2, 3], '2', 'oi', 4.2]
        assert capitulo5_exercicio16(lista_in) == lista_out

    def test_capitulo5_exercicio16_3(self):
        lista_in = ['0','1','2','3','4','5','6']
        lista_out = ['1', '2', '5', '6']
        assert capitulo5_exercicio16(lista_in) == lista_out

    def test_capitulo5_exercicio16_4(self):
        lista_in = [1,2,3,4,5,6,7,8,9,10]
        lista_out = [2, 3, 6, 7, 8, 9,10]
        assert capitulo5_exercicio16(lista_in) == lista_out


class Testcapitulo5Exercicio17():
    def test_capitulo5_exercicio17_1(self):
        lista_in = list(range(5))
        lista_out = [2, 3, 4]
        assert capitulo5_exercicio17(lista_in) == lista_out

    def test_capitulo5_exercicio17_2(self):
        lista_in = list(range(10))
        lista_out = [7, 8, 9]
        assert capitulo5_exercicio17(lista_in) == lista_out

    def test_capitulo5_exercicio17_3(self):
        lista_in = list(range(15))
        lista_out = [12, 13, 14]
        assert capitulo5_exercicio17(lista_in) == lista_out

    def test_capitulo5_exercicio17_4(self):
        lista_in = list(range(20))
        lista_out = [17, 18, 19]
        assert capitulo5_exercicio17(lista_in) == lista_out


class Testcapitulo5Exercicio18():
    def test_capitulo5_exercicio18_1(self):
        lista_in = list(range(5))
        lista_out = [4, 3, 2]
        assert capitulo5_exercicio18(lista_in) == lista_out

    def test_capitulo5_exercicio18_2(self):
        lista_in = list(range(10))
        lista_out = [9, 8, 7]
        assert capitulo5_exercicio18(lista_in) == lista_out

    def test_capitulo5_exercicio18_3(self):
        lista_in = list(range(15))
        lista_out = [14, 13, 12]
        assert capitulo5_exercicio18(lista_in) == lista_out

    def test_capitulo5_exercicio18_4(self):
        lista_in = list(range(20))
        lista_out = [19, 18, 17]
        assert capitulo5_exercicio18(lista_in) == lista_out


class Testcapitulo5Exercicio19():
    def test_capitulo5_exercicio19_1(self):
        lista_in = list(range(5))
        lista_out = [0, 1]
        assert capitulo5_exercicio19(lista_in) == lista_out

    def test_capitulo5_exercicio19_2(self):
        lista_in = list(range(10))
        lista_out = [0, 1]
        assert capitulo5_exercicio19(lista_in) == lista_out

    def test_capitulo5_exercicio19_3(self):
        lista_in = list(range(15))
        lista_out = [0, 1]
        assert capitulo5_exercicio19(lista_in) == lista_out

    def test_capitulo5_exercicio19_4(self):
        lista_in = list(range(20))
        lista_out = [0, 1]
        assert capitulo5_exercicio19(lista_in) == lista_out


class Testcapitulo5Exercicio20():
    def test_capitulo5_exercicio20_1(self):
        lista_in = list(range(5))
        lista_out = [4, 3, 2, 1, 0]
        assert capitulo5_exercicio20(lista_in) == lista_out

    def test_capitulo5_exercicio20_2(self):
        lista_in = list(range(10))
        lista_out = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        assert capitulo5_exercicio20(lista_in) == lista_out

    def test_capitulo5_exercicio20_3(self):
        lista_in = list(range(15))
        lista_out = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        assert capitulo5_exercicio20(lista_in) == lista_out

    def test_capitulo5_exercicio20_4(self):
        lista_in = list(range(20))
        lista_out = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        assert capitulo5_exercicio20(lista_in) == lista_out