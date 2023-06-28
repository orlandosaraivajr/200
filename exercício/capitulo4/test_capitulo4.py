from capitulo4 import capitulo4_exercicio1
from capitulo4 import capitulo4_exercicio2
from capitulo4 import capitulo4_exercicio3
from capitulo4 import capitulo4_exercicio4
from capitulo4 import capitulo4_exercicio5
from capitulo4 import capitulo4_exercicio6
from capitulo4 import capitulo4_exercicio7
from capitulo4 import capitulo4_exercicio8
from capitulo4 import capitulo4_exercicio9
from capitulo4 import capitulo4_exercicio10
from capitulo4 import capitulo4_exercicio11
from capitulo4 import capitulo4_exercicio12
from capitulo4 import capitulo4_exercicio13
from capitulo4 import capitulo4_exercicio14
from capitulo4 import capitulo4_exercicio15
from capitulo4 import capitulo4_exercicio16
from capitulo4 import capitulo4_exercicio17
from capitulo4 import capitulo4_exercicio18
from capitulo4 import capitulo4_exercicio19
from capitulo4 import capitulo4_exercicio20

import pytest
from pytest import approx

class Testcapitulo4Exercicio1():
    def test_capitulo4_exercicio1_1(self):
        msg_erro = "Necessário digitar um número"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio1(12, 'palavra')
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio2_2(self):
        retorno = capitulo4_exercicio1(10, 1)
        assert retorno == 11

    def test_capitulo4_exercicio2_3(self):
        retorno = capitulo4_exercicio1(1, 10)
        assert retorno == 11

    def test_capitulo4_exercicio2_4(self):
        retorno = capitulo4_exercicio1(1, 10.2)
        assert retorno == 11


class Testcapitulo4Exercicio2():
    def test_capitulo4_exercicio2_1(self, monkeypatch):
        responses = iter([12, 'Palavra'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        msg_erro = "Necessário digitar um número"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio2()
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio2_2(self, monkeypatch):
        responses = iter(['Palavra', 12])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        msg_erro = "Necessário digitar um número"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio2()
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio2_3(self, monkeypatch):
        responses = iter([6, 12])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo4_exercicio2()
        assert retorno == 18

    def test_capitulo4_exercicio2_4(self, monkeypatch):
        responses = iter(['6', '12'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo4_exercicio2()
        assert retorno == 18


class Testcapitulo4Exercicio3():
    def test_capitulo4_exercicio3_1(self):
        assert capitulo4_exercicio3(1000, 1, 0.1) == approx(100, 0.002)
        assert capitulo4_exercicio3(1000, 4, 0.1) == approx(400, 0.002)
        assert capitulo4_exercicio3(1000, 1, 0.01) == approx(10, 0.002)
        assert capitulo4_exercicio3(1000, 1, 0.999) == approx(999, 0.002)

    def test_capitulo4_exercicio3_2(self):
        msg_erro = "Juros precisa ser maior ou igual a zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio3(1000, 1, -0.01)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio3_3(self):
        msg_erro = "Juros precisa ser maior ou igual a zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio3(1000, 1, 0)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio3_4(self):
        assert capitulo4_exercicio3(1000, 1, 1) == approx(1000, 0.002)
        

class Testcapitulo4Exercicio4():
    def test_capitulo4_exercicio4_1(self):
        assert capitulo4_exercicio4(1000, 1, 0.1) == approx(100, 0.002)
        assert capitulo4_exercicio4(1000, 4, 0.1) == approx(400, 0.002)
        assert capitulo4_exercicio4(1000, 1, 0.01) == approx(10, 0.002)
        assert capitulo4_exercicio4(1000, 1, 0.999) == approx(999, 0.002)

    def test_capitulo4_exercicio4_2(self):
        msg_erro = "Juros precisa ser maior ou igual a zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio4(1000, 1, -0.01)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio4_3(self):
        msg_erro = "Juros precisa ser maior ou igual a zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio4(1000, 1, 0)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio4_4(self):
        assert capitulo4_exercicio4(1000, 1, 0.999999) == approx(999, 0.002)
        msg_erro = "Juros precisa ser menor que um"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio4(1000, 1, 1)
        assert str(error.value) == msg_erro
        

class Testcapitulo4Exercicio5():
    def test_capitulo4_exercicio5_1(self):
        assert capitulo4_exercicio5(3) == 27
        assert capitulo4_exercicio5(3.0) == 27
        assert capitulo4_exercicio5('3') == 27

    def test_capitulo4_exercicio5_2(self):
        assert capitulo4_exercicio5(2) == 8
        assert capitulo4_exercicio5(2.0) == 8
        assert capitulo4_exercicio5('2') == 8

    def test_capitulo4_exercicio5_3(self):
        msg_erro = "Erro ao converter oi em inteiro"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio5('oi')
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio5_4(self):
        msg_erro = "Erro ao converter [1, 2, 3] em inteiro"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio5([1,2,3])
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio6():
    def test_capitulo4_exercicio6_1(self):
        resultado = capitulo4_exercicio6('Palavra hacker')
        assert resultado == 'P@l@vr@ h@ck$r'

    def test_capitulo4_exercicio6_2(self):
        resultado = capitulo4_exercicio6('o dia está lindo')
        assert resultado == '0 dY@ $stá lYnd0'

    def test_capitulo4_exercicio6_3(self):
        msg_erro = "O argumento precisa ser string"
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio6(4.5)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio6_4(self):
        msg_erro = "O argumento precisa ser string"
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio6(4.5)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio7():
    def test_capitulo4_exercicio7_1(self, monkeypatch):
        responses = iter(['17'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo4_exercicio7()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo4_exercicio7_2(self, monkeypatch):
        responses = iter(['18'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo4_exercicio7()
        assert type(retorno) is bool
        assert not retorno 

    def test_capitulo4_exercicio7_3(self, monkeypatch):
        msg_erro = "Idade precisa ser número conversível para inteiro"
        responses = iter(['18.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio7()
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio7_4(self, monkeypatch):
        msg_erro = "Idade precisa ser número conversível para inteiro"
        responses = iter(['17.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio7()
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio8():
    def test_capitulo4_exercicio8_1(self):
        assert capitulo4_exercicio8('Palavra') == 'arvalaP'

    def test_capitulo4_exercicio8_2(self):
        assert capitulo4_exercicio8('Palavra Invertida') == 'aditrevnI arvalaP'

    def test_capitulo4_exercicio8_3(self):
        retorno = capitulo4_exercicio8(5)
        assert type(retorno) == TypeError
        assert str(retorno) == "'int' object is not subscriptable"

    def test_capitulo4_exercicio8_4(self):
        retorno = capitulo4_exercicio8(5.1)
        assert type(retorno) == TypeError
        assert str(retorno) == "'float' object is not subscriptable"


class Testcapitulo4Exercicio9():
    def test_capitulo4_exercicio9_1(self):
        retorno = capitulo4_exercicio9(10, 2)
        assert type(retorno) == float
        assert retorno == 5.0
        retorno = capitulo4_exercicio9(10, 5)
        assert type(retorno) == float
        assert retorno == 2.0

    def test_capitulo4_exercicio9_2(self):
        retorno = capitulo4_exercicio9(100, 2)
        assert type(retorno) == float
        assert retorno == 50.0
        retorno = capitulo4_exercicio9(0, 2)
        assert type(retorno) == float
        assert retorno == 0.0

    def test_capitulo4_exercicio9_3(self):
        retorno = capitulo4_exercicio9(10, 'oi mundo')
        assert type(retorno) == ValueError
        assert str(retorno) == "could not convert string to float: 'oi mundo'"

    def test_capitulo4_exercicio9_4(self):
        retorno = capitulo4_exercicio9(10, 0)
        assert type(retorno) == ZeroDivisionError
        assert str(retorno) == "float division by zero"

 
class Testcapitulo4Exercicio10():
    def test_capitulo4_exercicio10_1(self):
        retorno = capitulo4_exercicio10(10, 2)
        assert type(retorno) == float
        assert retorno == 5.0
        retorno = capitulo4_exercicio10(10, 5)
        assert type(retorno) == float
        assert retorno == 2.0

    def test_capitulo4_exercicio10_2(self):
        retorno = capitulo4_exercicio10(100, 2)
        assert type(retorno) == float
        assert retorno == 50.0
        retorno = capitulo4_exercicio10(0, 2)
        assert type(retorno) == float
        assert retorno == 0.0

    def test_capitulo4_exercicio10_3(self):
        msg_erro = "Erro ao converter argumentos."
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio10(4, 'oi mundo')
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio10_4(self):
        msg_erro = "Não é divisível por zero."
        with pytest.raises(ZeroDivisionError) as error:
            capitulo4_exercicio10(4, 0)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio11():
    def test_capitulo4_exercicio11_1(self):
        assert capitulo4_exercicio11(10) == 10
        assert capitulo4_exercicio11(9.99) == 9.99
        assert capitulo4_exercicio11(9.999) == 9.999

    def test_capitulo4_exercicio11_2(self):
        assert capitulo4_exercicio11(1) == 1
        assert capitulo4_exercicio11(0.1) == 0.1
        assert capitulo4_exercicio11(0.01) == 0.01
        assert capitulo4_exercicio11(0) == 0

    def test_capitulo4_exercicio11_3(self):
        msg_erro = "Valor maior que dez"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio11(15)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio11(10.0001)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio11_4(self):
        msg_erro = "Valor menor que zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio11(-0.001)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio12():
    def test_capitulo4_exercicio12_1(self):
        assert capitulo4_exercicio12(7, 5) == 6
        assert capitulo4_exercicio12(8, 5) == 6.5
        assert capitulo4_exercicio12(8, 4) == 6
        assert capitulo4_exercicio12(6, 3) == 4.5

    def test_capitulo4_exercicio12_2(self):
        msg_erro = "Valor menor que zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio12(6, -1)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio12(-6, 1)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio12_3(self):
        msg_erro = "Valor maior que dez"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio12(6, 10.5)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio12(16, 9)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio12_4(self):
        msg_erro = "Argumento passado não é conversível para float"
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio12('oi mundo', 10)
        assert str(error.value) == msg_erro
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio12(1, 'oi mundo')
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio13():
    def test_capitulo4_exercicio13_1(self):
        assert capitulo4_exercicio13(7, 5) == approx(5.666, 0.001)
        assert capitulo4_exercicio13(8, 5) == approx(6, 0.001)
        assert capitulo4_exercicio13(8, 4) == approx(5.333, 0.001)
        assert capitulo4_exercicio13(6, 3) == approx(4, 0.001)

    def test_capitulo4_exercicio13_2(self):
        msg_erro = "Valor menor que zero"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio13(6, -1)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio13(-6, 1)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio13_3(self):
        msg_erro = "Valor maior que dez"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio13(6, 10.5)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio13(16, 9)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio13_4(self):
        msg_erro = "Argumento passado não é conversível para float"
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio13('oi mundo', 10)
        assert str(error.value) == msg_erro
        with pytest.raises(TypeError) as error:
            capitulo4_exercicio13(1, 'oi mundo')
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio14():
    def test_capitulo4_exercicio14_1(self):
        assert capitulo4_exercicio14(1.75, 80) == approx(26.122, 0.001)
        assert capitulo4_exercicio14(1.75, 90) == approx(29.3877, 0.001)
        assert capitulo4_exercicio14(1.75, 100) == approx(32.653, 0.001)
        assert capitulo4_exercicio14(0.41, 50) == approx(297.441, 0.001)
        assert capitulo4_exercicio14(0.40, 50) == approx(312.499, 0.001)

    def test_capitulo4_exercicio14_2(self):
        assert capitulo4_exercicio14(1.65, 80) == approx(29.384, 0.001)
        assert capitulo4_exercicio14(1.65, 90) == approx(33.057, 0.001)
        assert capitulo4_exercicio14(1.65, 100) == approx(36.730, 0.001)
        assert capitulo4_exercicio14(1.95, 50) == approx(13.149, 0.001)
        assert capitulo4_exercicio14(1.95, 200) == approx(52.596, 0.001)

    def test_capitulo4_exercicio14_3(self):
        msg_erro = "Peso fora dos parâmetros (50 e 200)"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio14(1.75, 49)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio14(1.75, 201)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio14_4(self):
        msg_erro = "Altura fora dos parâmetros (0.40 e 2.10)"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio14(2.11, 100)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio14(0.39, 100)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio15():
    def test_capitulo4_exercicio15_1(self):
        assert capitulo4_exercicio15(60) == approx(37.2822, 0.002)
        assert capitulo4_exercicio15(72) == approx(44.7387, 0.002)

    def test_capitulo4_exercicio15_2(self):
        assert capitulo4_exercicio15(0) == approx(0.0, 0.002)
        assert capitulo4_exercicio15(100) == approx(62.1371, 0.002)

    def test_capitulo4_exercicio15_3(self):
        msg_erro = "Kilometro fora dos parâmetros (0.0 e 100)"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio15(101)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio15_4(self):
        msg_erro = "Kilometro fora dos parâmetros (0.0 e 100)"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio15(-0.01)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio16():
    def test_capitulo4_exercicio16_1(self):
        assert capitulo4_exercicio16(100, 20) == 1000
        assert capitulo4_exercicio16(100, 30) == 1500

    def test_capitulo4_exercicio16_2(self):
        assert capitulo4_exercicio16(15, 10) == 75
        assert capitulo4_exercicio16(15, 12) == 90

    def test_capitulo4_exercicio16_3(self):
        msg_erro = "Argumento não pode ser negativo"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio16( -1, 12)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio16( 1, -2)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio16( -1, -2)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio16_4(self):
        msg_erro = "Base não pode ser menor que a altura"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio16( 8, 9)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio17():
    def test_capitulo4_exercicio17_1(self):
        assert capitulo4_exercicio17(10, 5, 4) == 30
        assert capitulo4_exercicio17(24, 9, 15) == 247.5

    def test_capitulo4_exercicio17_2(self):
        assert capitulo4_exercicio17(10, 6, 5) == 40
        assert capitulo4_exercicio17(22, 8, 15) == 225

    def test_capitulo4_exercicio17_3(self):
        msg_erro = "Argumento não pode ser negativo"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio17( -13, 12, 12)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio17( 13, -12, 12)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio17( -1, -2, -4)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio17_4(self):
        msg_erro = "Base maior não pode ser menor ou igual a base menor"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio17( 10, 11, 5)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio18():
    def test_capitulo4_exercicio18_1(self):
        assert capitulo4_exercicio18(500, 0.1) == 50
        assert capitulo4_exercicio18(50, 0.1) == 5

    def test_capitulo4_exercicio18_2(self):
        assert capitulo4_exercicio18(1000, 0.1) == 100
        assert capitulo4_exercicio18(100, 0.1) == 10

    def test_capitulo4_exercicio18_3(self):
        msg_erro = "Porcentagem precisa estar entre 0 e 1"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio18( 100, 0)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio18( 100, -0.001)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio18( 100, 1.001)
        assert str(error.value) == msg_erro
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio18( 100, 1)
        assert str(error.value) == msg_erro

    def test_capitulo4_exercicio18_4(self):
        msg_erro = "Valor precisa ser positivo"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio18( -100, 0.5)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio19():
    def test_capitulo4_exercicio19_1(self):
        assert capitulo4_exercicio19(500) == 450
        assert capitulo4_exercicio19(50) == 45

    def test_capitulo4_exercicio19_2(self):
        assert capitulo4_exercicio19(1000) == 900
        assert capitulo4_exercicio19(100) == 90

    def test_capitulo4_exercicio19_3(self):
        assert capitulo4_exercicio19(1000) == 900
        assert capitulo4_exercicio19(100) == 90

    def test_capitulo4_exercicio19_4(self):
        msg_erro = "Valor precisa ser positivo"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio19( -100)
        assert str(error.value) == msg_erro


class Testcapitulo4Exercicio20():
    def test_capitulo4_exercicio20_1(self):
        assert capitulo4_exercicio20(500) == 425
        assert capitulo4_exercicio20(50) == 42.5

    def test_capitulo4_exercicio20_2(self):
        assert capitulo4_exercicio20(1123) == 954.55
        assert capitulo4_exercicio20(100) == 85

    def test_capitulo4_exercicio20_3(self):
        assert capitulo4_exercicio20(1000) == 850
        assert capitulo4_exercicio20(100) == 85

    def test_capitulo4_exercicio20_4(self):
        msg_erro = "Valor precisa ser positivo"
        with pytest.raises(ValueError) as error:
            capitulo4_exercicio20( -100)
        assert str(error.value) == msg_erro
