from capitulo0 import capitulo0_exercicio1
from capitulo0 import capitulo0_exercicio2
from capitulo0 import capitulo0_exercicio3


import pytest


class Testcapitulo0Exercicio1():
    def test_capitulo0_exercicio1_1(self):
        retorno = capitulo0_exercicio1()
        assert type(retorno) == str

    def test_capitulo0_exercicio1_2(self):
        retorno = capitulo0_exercicio1()
        assert len(retorno) == 8

    def test_capitulo0_exercicio1_3(self):
        retorno = capitulo0_exercicio1()
        assert retorno.upper() == 'OI MUNDO'

    def test_capitulo0_exercicio1_4(self):
        retorno = capitulo0_exercicio1()
        assert retorno == 'Oi Mundo'


class Testcapitulo0Exercicio2():
    def test_capitulo0_exercicio2_1(self):
        retorno = capitulo0_exercicio2('Pessoas')
        assert type(retorno) == str
        retorno = capitulo0_exercicio2('Mundo')
        assert type(retorno) == str

    def test_capitulo0_exercicio2_2(self):
        retorno = capitulo0_exercicio2('Pessoas')
        assert len(retorno) == 10
        retorno = capitulo0_exercicio2('Mundo')
        assert len(retorno) == 8

    def test_capitulo0_exercicio2_3(self):
        retorno = capitulo0_exercicio2('Pessoas')
        assert retorno == 'Oi Pessoas'
        retorno = capitulo0_exercicio2('Mundo')
        assert retorno == 'Oi Mundo'

    def test_capitulo0_exercicio2_4(self):
        retorno = capitulo0_exercicio2('MuNdo')
        assert retorno == 'Oi MuNdo'
        retorno = capitulo0_exercicio2('MUNDO')
        assert retorno == 'Oi MUNDO'


class Testcapitulo0Exercicio3():
    def test_capitulo0_exercicio3_1(self):
        retorno = capitulo0_exercicio3(4, 21)
        assert type(retorno) == int
        assert retorno == 25
        retorno = capitulo0_exercicio3(5, 5)
        assert retorno == 10

    def test_capitulo0_exercicio3_2(self):
        retorno = capitulo0_exercicio3(3.2, 10)
        assert type(retorno) == float
        assert retorno == 13.2
        retorno = capitulo0_exercicio3(2.4, 7)
        assert retorno == 9.4

    def test_capitulo0_exercicio3_3(self):
        retorno = capitulo0_exercicio3(-5.0, -5)
        assert retorno == -10
        retorno = capitulo0_exercicio3(-2.4, -1)
        assert retorno == -3.4

    def test_capitulo0_exercicio3_4(self):
        retorno = capitulo0_exercicio3(-3, -5)
        assert retorno == -8
        retorno = capitulo0_exercicio3(-5, -1)
        assert retorno == -6 
        retorno = capitulo0_exercicio3(-5, 1)
        assert retorno == -4

