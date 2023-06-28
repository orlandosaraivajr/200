from capitulo1 import capitulo1_exercicio1
from capitulo1 import capitulo1_exercicio2
from capitulo1 import capitulo1_exercicio3
from capitulo1 import capitulo1_exercicio4
from capitulo1 import capitulo1_exercicio5
from capitulo1 import capitulo1_exercicio6
from capitulo1 import capitulo1_exercicio7
from capitulo1 import capitulo1_exercicio8
from capitulo1 import capitulo1_exercicio9
from capitulo1 import capitulo1_exercicio10
from capitulo1 import capitulo1_exercicio11
from capitulo1 import capitulo1_exercicio12
from capitulo1 import capitulo1_exercicio13
from capitulo1 import capitulo1_exercicio14
from capitulo1 import capitulo1_exercicio15
from capitulo1 import capitulo1_exercicio16
from capitulo1 import capitulo1_exercicio17
from capitulo1 import capitulo1_exercicio18
from capitulo1 import capitulo1_exercicio19
from capitulo1 import capitulo1_exercicio20
import pytest
from pytest import approx


class Testcapitulo1Exercicio1():
    def test_capitulo1_exercicio1_1(self):
        retorno = capitulo1_exercicio1(10, 20)
        assert type(retorno) == int
        assert retorno == 30
        retorno = capitulo1_exercicio1(5, 5)
        assert retorno == 10

    def test_capitulo1_exercicio1_2(self):
        retorno = capitulo1_exercicio1(10.3, 20.7)
        assert type(retorno) == float
        assert retorno == 31
        retorno = capitulo1_exercicio1(5.8, 20.7)
        assert retorno == 26.5

    def test_capitulo1_exercicio1_3(self):
        retorno = capitulo1_exercicio1(10 + 3j, 10 + 3j)
        assert type(retorno) == complex
        assert retorno == 20 + 6j
        retorno = capitulo1_exercicio1(2 + 1j, 1 + 2j)
        assert retorno == 3 + 3j

    def test_capitulo1_exercicio1_4(self):
        retorno = capitulo1_exercicio1(10 + 3j, 20)
        assert type(retorno) == complex
        assert retorno == 30 + 3j


class Testcapitulo1Exercicio2():
    def test_capitulo1_exercicio2_1(self):
        retorno = capitulo1_exercicio2(3, 21)
        assert type(retorno) == int
        assert retorno == 30
        retorno = capitulo1_exercicio2(5, 5)
        assert retorno == 20

    def test_capitulo1_exercicio2_2(self):
        retorno = capitulo1_exercicio2(3.2, 10)
        assert type(retorno) == float
        assert retorno == 19.6
        retorno = capitulo1_exercicio2(2.4, 7)
        assert retorno == 14.2

    def test_capitulo1_exercicio2_3(self):
        retorno = capitulo1_exercicio2(3.2, -5)
        assert type(retorno) == float
        assert retorno == approx(4.6, 2)
        retorno = capitulo1_exercicio2(-2.4, 7)
        assert retorno == approx(-0.199, 2)

    def test_capitulo1_exercicio2_4(self):
        retorno = capitulo1_exercicio2(3, -5)
        assert retorno == 4
        retorno = capitulo1_exercicio2(5, -1)
        assert retorno == 14


class Testcapitulo1Exercicio3():
    def test_capitulo1_exercicio3_1(self):
        retorno = capitulo1_exercicio3(3, 21)
        assert type(retorno) == int
        assert retorno == 30
        retorno = capitulo1_exercicio3(5, 5)
        assert retorno == 20

    def test_capitulo1_exercicio3_2(self):
        retorno = capitulo1_exercicio3(3.2, 10)
        assert type(retorno) == float
        assert retorno == 19.6
        retorno = capitulo1_exercicio3(2.4, 7)
        assert retorno == 14.2

    def test_capitulo1_exercicio3_3(self):
        retorno = capitulo1_exercicio3(-3.2, -5)
        assert retorno == 0
        retorno = capitulo1_exercicio3(-2.4, 7)
        assert retorno == 0

    def test_capitulo1_exercicio3_4(self):
        retorno = capitulo1_exercicio3(-3, -5)
        assert retorno == 0
        retorno = capitulo1_exercicio3(-5, -1)
        assert retorno == 0 


class Testcapitulo1Exercicio4():
    def test_capitulo1_exercicio4_1(self):
        retorno = capitulo1_exercicio4(2)
        assert type(retorno) == int
        assert retorno == 8
        assert capitulo1_exercicio4(3) == 27

    def test_capitulo1_exercicio4_2(self):
        retorno = capitulo1_exercicio4(0)
        assert retorno == 0

    def test_capitulo1_exercicio4_3(self):
        retorno = capitulo1_exercicio4(-3)
        assert retorno == 0

    def test_capitulo1_exercicio4_4(self):
        retorno = capitulo1_exercicio4(5)
        assert retorno == 125


class Testcapitulo1Exercicio5():
    def test_capitulo1_exercicio5_1(self):
        assert capitulo1_exercicio5(10, 2) == 10
        assert capitulo1_exercicio5(10, 3) == 15

    def test_capitulo1_exercicio5_2(self):
        assert capitulo1_exercicio5(15, 10) == 75
        assert capitulo1_exercicio5(15, 12) == 90

    def test_capitulo1_exercicio5_3(self):
        assert capitulo1_exercicio5(12, 3) == 18
        assert capitulo1_exercicio5(12, 8) == 48

    def test_capitulo1_exercicio5_4(self):
        assert capitulo1_exercicio5(7, 3) == 10.5
        assert capitulo1_exercicio5(7, 5) == 17.5


class Testcapitulo1Exercicio6():
    def test_capitulo1_exercicio6_1(self):
        assert capitulo1_exercicio6(100) == approx(37.7778, 0.002)
 
    def test_capitulo1_exercicio6_2(self):
        assert capitulo1_exercicio6(32) == approx(0, 0.002)

    def test_capitulo1_exercicio6_3(self):
        assert capitulo1_exercicio6(200) == approx(93.333, 0.002)


    def test_capitulo1_exercicio6_4(self):
        assert capitulo1_exercicio6(50) == approx(10, 0.002)


class Testcapitulo1Exercicio7():
    def test_capitulo1_exercicio7_1(self):
        assert capitulo1_exercicio7(1000, 1, 0.1) == approx(100, 0.002)
        assert capitulo1_exercicio7(1000, 2, 0.1) == approx(200, 0.002)
        assert capitulo1_exercicio7(1000, 3, 0.1) == approx(300, 0.002)
        assert capitulo1_exercicio7(1000, 4, 0.1) == approx(400, 0.002)

    def test_capitulo1_exercicio7_2(self):
        assert capitulo1_exercicio7(100, 1, 0.1) == approx(10, 0.002)
        assert capitulo1_exercicio7(100, 2, 0.1) == approx(20, 0.002)
        assert capitulo1_exercicio7(100, 3, 0.1) == approx(30, 0.002)
        assert capitulo1_exercicio7(100, 4, 0.1) == approx(40, 0.002)

    def test_capitulo1_exercicio7_3(self):
        assert capitulo1_exercicio7(1000, 1, 0.025) == approx(25.0, 0.002)
        assert capitulo1_exercicio7(1000, 2, 0.025) == approx(50, 0.002)
        assert capitulo1_exercicio7(1000, 3, 0.025) == approx(75, 0.002)
        assert capitulo1_exercicio7(1000, 4, 0.025) == approx(100, 0.002)

    def test_capitulo1_exercicio7_4(self):
        assert capitulo1_exercicio7(500, 1, 0.025) == approx(12.5, 0.002)
        assert capitulo1_exercicio7(500, 2, 0.025) == approx(25, 0.002)
        assert capitulo1_exercicio7(500, 3, 0.025) == approx(37.5, 0.002)
        assert capitulo1_exercicio7(500, 4, 0.025) == approx(50, 0.002)


class Testcapitulo1Exercicio8():
    def test_capitulo1_exercicio8_1(self):
        assert capitulo1_exercicio8(1000, 1, 0.1) == approx(1100, 0.002)
        assert capitulo1_exercicio8(1000, 2, 0.1) == approx(1200, 0.002)
        assert capitulo1_exercicio8(1000, 3, 0.1) == approx(1300, 0.002)
        assert capitulo1_exercicio8(1000, 4, 0.1) == approx(1400, 0.002)

    def test_capitulo1_exercicio8_2(self):
        assert capitulo1_exercicio8(100, 1, 0.1) == approx(110, 0.002)
        assert capitulo1_exercicio8(100, 2, 0.1) == approx(120, 0.002)
        assert capitulo1_exercicio8(100, 3, 0.1) == approx(130, 0.002)
        assert capitulo1_exercicio8(100, 4, 0.1) == approx(140, 0.002)

    def test_capitulo1_exercicio8_3(self):
        assert capitulo1_exercicio8(1000, 1, 0.025) == approx(1025.0, 0.002)
        assert capitulo1_exercicio8(1000, 2, 0.025) == approx(1050, 0.002)
        assert capitulo1_exercicio8(1000, 3, 0.025) == approx(1075, 0.002)
        assert capitulo1_exercicio8(1000, 4, 0.025) == approx(1100, 0.002)

    def test_capitulo1_exercicio8_4(self):
        assert capitulo1_exercicio8(500, 1, 0.025) == approx(512, 0.002)
        assert capitulo1_exercicio8(500, 2, 0.025) == approx(525, 0.002)
        assert capitulo1_exercicio8(500, 3, 0.025) == approx(537, 0.002)
        assert capitulo1_exercicio8(500, 4, 0.025) == approx(550, 0.002)


class Testcapitulo1Exercicio9():
    def test_capitulo1_exercicio9_1(self):
        assert capitulo1_exercicio9(1000, 1, 0.1) == approx(1100, 0.002)
        assert capitulo1_exercicio9(1000, 2, 0.1) == approx(1210, 0.002)
        assert capitulo1_exercicio9(1000, 3, 0.1) == approx(1331, 0.002)
        assert capitulo1_exercicio9(1000, 4, 0.1) == approx(1464, 0.002)

    def test_capitulo1_exercicio9_2(self):
        assert capitulo1_exercicio9(100, 1, 0.1) == approx(110, 0.002)
        assert capitulo1_exercicio9(100, 2, 0.1) == approx(121, 0.002)
        assert capitulo1_exercicio9(100, 3, 0.1) == approx(133, 0.002)
        assert capitulo1_exercicio9(100, 4, 0.1) == approx(146.4, 0.002)

    def test_capitulo1_exercicio9_3(self):
        assert capitulo1_exercicio9(1000, 1, 0.025) == approx(1025, 0.002)
        assert capitulo1_exercicio9(1000, 2, 0.025) == approx(1050.625, 0.002)
        assert capitulo1_exercicio9(1000, 3, 0.025) == approx(1076.89, 0.002)
        assert capitulo1_exercicio9(1000, 4, 0.025) == approx(1103.812, 0.002)

    def test_capitulo1_exercicio9_4(self):
        assert capitulo1_exercicio9(500, 1, 0.025) == approx(512, 0.002)
        assert capitulo1_exercicio9(500, 2, 0.025) == approx(525.31, 0.002)
        assert capitulo1_exercicio9(500, 3, 0.025) == approx(538.44, 0.002)
        assert capitulo1_exercicio9(500, 4, 0.025) == approx(551.90, 0.002)


class Testcapitulo1Exercicio10():
    def test_capitulo1_exercicio10_1(self):
        assert capitulo1_exercicio10(1000, 1, 0.1) == approx(100, 0.002)
        assert capitulo1_exercicio10(1000, 2, 0.1) == approx(210, 0.002)
        assert capitulo1_exercicio10(1000, 3, 0.1) == approx(331, 0.002)
        assert capitulo1_exercicio10(1000, 4, 0.1) == approx(464, 0.002)

    def test_capitulo1_exercicio10_2(self):
        assert capitulo1_exercicio10(100, 1, 0.1) == approx(10, 0.002)
        assert capitulo1_exercicio10(100, 2, 0.1) == approx(21, 0.002)
        assert capitulo1_exercicio10(100, 3, 0.1) == approx(33.1, 0.002)
        assert capitulo1_exercicio10(100, 4, 0.1) == approx(46.4, 0.002)

    def test_capitulo1_exercicio10_3(self):
        assert capitulo1_exercicio10(1000, 1, 0.025) == approx(25, 0.002)
        assert capitulo1_exercicio10(1000, 2, 0.025) == approx(50.625, 0.002)
        assert capitulo1_exercicio10(1000, 3, 0.025) == approx(76.89, 0.002)
        assert capitulo1_exercicio10(1000, 4, 0.025) == approx(103.812, 0.002)

    def test_capitulo1_exercicio10_4(self):
        assert capitulo1_exercicio10(500, 1, 0.025) == approx(12.5, 0.002)
        assert capitulo1_exercicio10(500, 2, 0.025) == approx(25.31, 0.002)
        assert capitulo1_exercicio10(500, 3, 0.025) == approx(38.44, 0.002)
        assert capitulo1_exercicio10(500, 4, 0.025) == approx(51.90, 0.002)

 
class Testcapitulo1Exercicio11():
    def test_capitulo1_exercicio11_1(self):
        assert capitulo1_exercicio11(60) == approx(37.2822, 0.002)

    def test_capitulo1_exercicio11_2(self):
        assert capitulo1_exercicio11(72) == approx(44.7387, 0.002)

    def test_capitulo1_exercicio11_3(self):
        assert capitulo1_exercicio11(100) == approx(62.1371, 0.002)

    def test_capitulo1_exercicio11_4(self):
        assert capitulo1_exercicio11(120) == approx(74.56, 0.002)


class Testcapitulo1Exercicio12():
    def test_capitulo1_exercicio12_1(self):
        assert capitulo1_exercicio12(60) == approx(16.66, 0.002)

    def test_capitulo1_exercicio12_2(self):
        assert capitulo1_exercicio12(72) == approx(20, 0.002)

    def test_capitulo1_exercicio12_3(self):
        assert capitulo1_exercicio12(100) == approx(27.77, 0.002)

    def test_capitulo1_exercicio12_4(self):
        assert capitulo1_exercicio12(120) == approx(33.333, 0.002)


class Testcapitulo1Exercicio13():
    def test_capitulo1_exercicio13_1(self):
        assert capitulo1_exercicio13(1.70, 75) == approx(25.95, 0.002)

    def test_capitulo1_exercicio13_2(self):
        assert capitulo1_exercicio13(1.70, 80) == approx(27.681, 0.002)
        
    def test_capitulo1_exercicio13_3(self):
        assert capitulo1_exercicio13(1.60, 75) == approx(29.296, 0.002)

    def test_capitulo1_exercicio13_4(self):
        assert capitulo1_exercicio13(1.60, 80) == approx(31.249, 0.002)


class Testcapitulo1Exercicio14():
    def test_capitulo1_exercicio14_1(self):
        assert capitulo1_exercicio14(1, 1) == approx(1, 0.002)
        assert capitulo1_exercicio14(6, 6) == approx(6, 0.002)
        assert capitulo1_exercicio14(10, 10) == approx(10, 0.002)

    def test_capitulo1_exercicio14_2(self):
        assert capitulo1_exercicio14(1, 7) == approx(5, 0.002)
        assert capitulo1_exercicio14(6, 7) == approx(6.66, 0.002)
        assert capitulo1_exercicio14(10, 7) == approx(8, 0.002)

    def test_capitulo1_exercicio14_3(self):
        assert capitulo1_exercicio14(7, 1) == approx(3, 0.002)
        assert capitulo1_exercicio14(7, 6) == approx(6.33, 0.002)
        assert capitulo1_exercicio14(7, 10) == approx(9, 0.002)

    def test_capitulo1_exercicio14_4(self):
        assert capitulo1_exercicio14(-1, 1) == approx(0.333, 0.002)
        assert capitulo1_exercicio14(-6, 6) == approx(2, 0.002)
        assert capitulo1_exercicio14(-10, 10) == approx(3.33, 0.002)


class Testcapitulo1Exercicio15():
    def test_capitulo1_exercicio15_1(self):
        assert capitulo1_exercicio15(1, 2, 3) == approx(2.25, 0.002)
        assert capitulo1_exercicio15(2, 2, 2) == approx(2, 0.002)
        assert capitulo1_exercicio15(3, 2, 1) == approx(1.75, 0.002)

    def test_capitulo1_exercicio15_2(self):
        assert capitulo1_exercicio15(2, 4, 6) == approx(4.5, 0.002)
        assert capitulo1_exercicio15(4, 4, 4) == approx(4, 0.002)
        assert capitulo1_exercicio15(6, 4, 2) == approx(3.5, 0.002)

    def test_capitulo1_exercicio15_3(self):
        assert capitulo1_exercicio15(1, 5, 10) == approx(6.5, 0.002)
        assert capitulo1_exercicio15(5, 5, 5) == approx(5, 0.002)
        assert capitulo1_exercicio15(10, 5, 1) == approx(4.25, 0.002)

    def test_capitulo1_exercicio15_4(self):
        assert capitulo1_exercicio15(-5, 0, 5) == approx(1.25, 0.002)
        assert capitulo1_exercicio15(0, 0, 0) == approx(0, 0.002)
        assert capitulo1_exercicio15(5, 0, -5) == approx(-1.25, 0.002)
        

class Testcapitulo1Exercicio16():
    def test_capitulo1_exercicio16_1(self):
        assert capitulo1_exercicio16(1, 2, 3, 4) == approx(3, 0.002)
        assert capitulo1_exercicio16(4, 3, 2, 1) == approx(2, 0.002)
        assert capitulo1_exercicio16(2, 1, 2, 3) == approx(2.285, 0.002)

    def test_capitulo1_exercicio16_2(self):
        assert capitulo1_exercicio16(7, -1, 3, 12) == approx(6.857, 0.002)
        assert capitulo1_exercicio16(2, 4, 3, 7) == approx(4.714, 0.002)
        assert capitulo1_exercicio16(7, 3, 4, 2) == approx(3.428, 0.002)
        

    def test_capitulo1_exercicio16_3(self):
        assert capitulo1_exercicio16(5, 6, 7, 9) == approx(7.428, 0.002)
        assert capitulo1_exercicio16(9, 6, 7, 9) == approx(8, 0.002)
        assert capitulo1_exercicio16(5, 6, 7, 5) == approx(5.714, 0.002)
        assert capitulo1_exercicio16(1, 6, 7, 9) == approx(6.857, 0.002)

    def test_capitulo1_exercicio16_4(self):
        assert capitulo1_exercicio16(1, 2, 3, 10) == approx(5.57, 0.002)
        assert capitulo1_exercicio16(2, 2, 2, 10) == approx(5.42, 0.002)
        assert capitulo1_exercicio16(3, 2, 1, 10) == approx(5.28, 0.002)
        assert capitulo1_exercicio16(10, 2, 1, 3) == approx(3.285, 0.002)


class Testcapitulo1Exercicio17():
    def test_capitulo1_exercicio17_1(self):
        assert not capitulo1_exercicio17(1, 2, 3, 4)
        assert not capitulo1_exercicio17(4, 3, 2, 1)
        assert not capitulo1_exercicio17(2, 1, 2, 3)

    def test_capitulo1_exercicio17_2(self):
        assert capitulo1_exercicio17(7, -1, 3, 12)
        assert not capitulo1_exercicio17(2, 4, 3, 7)
        assert not capitulo1_exercicio17(7, 3, 4, 2)

    def test_capitulo1_exercicio17_3(self):
        assert capitulo1_exercicio17(5, 6, 7, 9)
        assert capitulo1_exercicio17(9, 6, 7, 9)
        assert capitulo1_exercicio17(5, 6, 7, 5)
        assert capitulo1_exercicio17(1, 6, 7, 9)

    def test_capitulo1_exercicio17_4(self):
        assert capitulo1_exercicio17(1, 2, 3, 10)
        assert capitulo1_exercicio17(2, 2, 2, 10)
        assert capitulo1_exercicio17(3, 2, 1, 10)
        assert not capitulo1_exercicio17(10, 2, 1, 3)


class Testcapitulo1Exercicio18():
    def test_capitulo1_exercicio18_1(self):
        assert not capitulo1_exercicio18(1)
        assert not capitulo1_exercicio18(3)
        assert not capitulo1_exercicio18(5)
        assert not capitulo1_exercicio18(7)


    def test_capitulo1_exercicio18_2(self):
        assert capitulo1_exercicio18(2)
        assert capitulo1_exercicio18(4)
        assert capitulo1_exercicio18(6)
        assert capitulo1_exercicio18(8)

    def test_capitulo1_exercicio18_3(self):
        assert not capitulo1_exercicio18(33)
        assert capitulo1_exercicio18(42)
        assert capitulo1_exercicio18(44)
        assert not capitulo1_exercicio18(81)

    def test_capitulo1_exercicio18_4(self):
        assert not capitulo1_exercicio18(1001)
        assert capitulo1_exercicio18(1200)
        assert capitulo1_exercicio18(3244)
        assert not capitulo1_exercicio18(4581)


class Testcapitulo1Exercicio19():
    def test_capitulo1_exercicio19_1(self):
        assert capitulo1_exercicio19(10)
        assert not capitulo1_exercicio19(15)
        assert not capitulo1_exercicio19(3)
        assert not capitulo1_exercicio19(6)

    def test_capitulo1_exercicio19_2(self):
        assert capitulo1_exercicio19(30)
        assert not capitulo1_exercicio19(45)
        assert capitulo1_exercicio19(60)
        assert not capitulo1_exercicio19(65)

    def test_capitulo1_exercicio19_3(self):
        assert capitulo1_exercicio19(60)
        assert not capitulo1_exercicio19(66)
        assert capitulo1_exercicio19(120)
        assert capitulo1_exercicio19(140)

    def test_capitulo1_exercicio19_4(self):
        assert capitulo1_exercicio19(600)
        assert capitulo1_exercicio19(660)
        assert capitulo1_exercicio19(1200)
        assert capitulo1_exercicio19(1400)


class Testcapitulo1Exercicio20():
    def test_capitulo1_exercicio20_1(self):
        assert not capitulo1_exercicio20(10)
        assert capitulo1_exercicio20(15)
        assert not capitulo1_exercicio20(3)
        assert not capitulo1_exercicio20(6)

    def test_capitulo1_exercicio20_2(self):
        assert capitulo1_exercicio20(30)
        assert capitulo1_exercicio20(45)
        assert capitulo1_exercicio20(60)
        assert not capitulo1_exercicio20(65)

    def test_capitulo1_exercicio20_3(self):
        assert capitulo1_exercicio19(60)
        assert not capitulo1_exercicio19(66)
        assert capitulo1_exercicio19(120)
        assert capitulo1_exercicio19(140)

    def test_capitulo1_exercicio20_4(self):
        assert capitulo1_exercicio20(600)
        assert capitulo1_exercicio20(660)
        assert capitulo1_exercicio20(1200)
        assert not capitulo1_exercicio20(1400)