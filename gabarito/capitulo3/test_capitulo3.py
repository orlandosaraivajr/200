from capitulo3 import capitulo3_exercicio1
from capitulo3 import capitulo3_exercicio2
from capitulo3 import capitulo3_exercicio3
from capitulo3 import capitulo3_exercicio4
from capitulo3 import capitulo3_exercicio5
from capitulo3 import capitulo3_exercicio6
from capitulo3 import capitulo3_exercicio7
from capitulo3 import capitulo3_exercicio8
from capitulo3 import capitulo3_exercicio9
from capitulo3 import capitulo3_exercicio10
from capitulo3 import capitulo3_exercicio11
from capitulo3 import capitulo3_exercicio12
from capitulo3 import capitulo3_exercicio13
from capitulo3 import capitulo3_exercicio14
from capitulo3 import capitulo3_exercicio15
from capitulo3 import capitulo3_exercicio16
from capitulo3 import capitulo3_exercicio17
from capitulo3 import capitulo3_exercicio18
from capitulo3 import capitulo3_exercicio19
from capitulo3 import capitulo3_exercicio20
import pytest


class Testcapitulo3Exercicio1():
    def test_capitulo3_exercicio1_1(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "José")
        retorno = capitulo3_exercicio1()
        assert retorno == 'José'

    def test_capitulo3_exercicio1_2(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "José da Silva")
        retorno = capitulo3_exercicio1()
        assert retorno == 'José da Silva'

    def test_capitulo3_exercicio1_3(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "")
        retorno = capitulo3_exercicio1()
        assert retorno == ''

    def test_capitulo3_exercicio1_4(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "123 da silva 4")
        retorno = capitulo3_exercicio1()
        assert retorno == '123 da silva 4'


class Testcapitulo3Exercicio2():
    def test_capitulo3_exercicio2_1(self, monkeypatch):
        responses = iter(['José'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio2()
        assert retorno == 'Seu nome é José'

    def test_capitulo3_exercicio2_2(self, monkeypatch):
        responses = iter(['José da Silva'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio2()
        assert retorno == 'Seu nome é José da Silva'

    def test_capitulo3_exercicio2_3(self, monkeypatch):
        responses = iter([''])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio2()
        assert retorno == 'Seu nome é '

    def test_capitulo3_exercicio2_4(self, monkeypatch):
        responses = iter(['123 da silva 4'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio2()
        assert retorno == 'Seu nome é 123 da silva 4'


class Testcapitulo3Exercicio3():
    def test_capitulo3_exercicio3_1(self, monkeypatch):
        responses = iter(['123 da silva 4', '15'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio3()
        assert retorno == '123 da silva 4 - 15'

    def test_capitulo3_exercicio3_2(self, monkeypatch):
        responses = iter(['José da Silva', '25'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio3()
        assert retorno == 'José da Silva - 25'

    def test_capitulo3_exercicio3_3(self, monkeypatch):
        responses = iter(['José da Silva', '40'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio3()
        assert retorno == 'José da Silva - 40'

    def test_capitulo3_exercicio3_4(self, monkeypatch):
        responses = iter(['', '25'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio3()
        assert retorno == ' - 25'


class Testcapitulo3Exercicio4():
    def test_capitulo3_exercicio4_1(self, monkeypatch):
        responses = iter(['123 da silva 4', '15'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio4()
        assert retorno == '123 da silva 4 - 15 anos'

    def test_capitulo3_exercicio3_2(self, monkeypatch):
        responses = iter(['José da Silva', '25'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio4()
        assert retorno == 'José da Silva - 25 anos'

    def test_capitulo3_exercicio3_3(self, monkeypatch):
        responses = iter(['José da Silva', '40'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio4()
        assert retorno == 'José da Silva - 40 anos'

    def test_capitulo3_exercicio3_4(self, monkeypatch):
        responses = iter(['', '25'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio4()
        assert retorno == ' - 25 anos'


class Testcapitulo3Exercicio5():
    def test_capitulo3_exercicio5_1(self, monkeypatch):
        responses = iter(['17'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio5()
        assert retorno 

    def test_capitulo3_exercicio5_2(self, monkeypatch):
        responses = iter(['18'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio5()
        assert not retorno 

    def test_capitulo3_exercicio5_3(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '18.5'"
        responses = iter(['18.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio5()
        assert str(error.value) == msg_erro

    def test_capitulo3_exercicio5_4(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '17.5'"
        responses = iter(['17.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio5()
        assert str(error.value) == msg_erro

    
class Testcapitulo3Exercicio6():
    def test_capitulo3_exercicio6_1(self, monkeypatch):
        responses = iter(['17'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio6()
        assert type(retorno) is str
        assert retorno == '22'
 
    def test_capitulo3_exercicio6_2(self, monkeypatch):
        responses = iter(['18'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio6()
        assert type(retorno) is str
        assert retorno == '23'

    def test_capitulo3_exercicio6_3(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '18.5'"
        responses = iter(['18.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio6()
        assert str(error.value) == msg_erro

    def test_capitulo3_exercicio6_4(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '17.5'"
        responses = iter(['17.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio6()
        assert str(error.value) == msg_erro


class Testcapitulo3Exercicio7():
    def test_capitulo3_exercicio7_1(self, monkeypatch):
        responses = iter(['17'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio7()
        assert type(retorno) is str
        assert retorno == '22 anos'

    def test_capitulo3_exercicio7_2(self, monkeypatch):
        responses = iter(['18'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio7()
        assert type(retorno) is str
        assert retorno == '23 anos'

    def test_capitulo3_exercicio7_3(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '18.5'"
        responses = iter(['18.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio7()
        assert str(error.value) == msg_erro

    def test_capitulo3_exercicio7_4(self, monkeypatch):
        msg_erro = "invalid literal for int() with base 10: '17.5'"
        responses = iter(['17.5'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(ValueError) as error:
            capitulo3_exercicio7()
        assert str(error.value) == msg_erro


class Testcapitulo3Exercicio8():
    def test_capitulo3_exercicio8_1(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio8('123mudar')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio8_2(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio8('123MUDAR')
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio8_3(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio8('123MuDaR')
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio8_4(self, monkeypatch):
        responses = iter(['123MUDAR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio8('123MUDAR')
        assert type(retorno) is bool
        assert retorno


class Testcapitulo3Exercicio9():
    def test_capitulo3_exercicio9_1(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio9('123mudar')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio9_2(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio9('123MUDAR')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio9_3(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio9('123MuDaR')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio9_4(self, monkeypatch):
        responses = iter(['123MUDAR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio9('123MUDAR')
        assert type(retorno) is bool
        assert retorno

    
class Testcapitulo3Exercicio10():
    def test_capitulo3_exercicio10_1(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio10('Silva')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio10_2(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio10('SILVA')
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio10_3(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio10('Jo')
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio10_4(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio10('João')
        assert type(retorno) is bool
        assert not retorno


class Testcapitulo3Exercicio11():
    def test_capitulo3_exercicio11_1(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio11()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio11_2(self, monkeypatch):
        responses = iter(['José Júnior Alves'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio11()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio11_3(self, monkeypatch):
        responses = iter(['Palavra com As'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio11()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio11_4(self, monkeypatch):
        responses = iter(['P@l@vr@ sem @s'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio11()
        assert type(retorno) is bool
        assert not retorno


class Testcapitulo3Exercicio12():
    def test_capitulo3_exercicio12_1(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio12()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio12_2(self, monkeypatch):
        responses = iter(['JOSÉ DA SILVA JÚNIOR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio12()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio12_3(self, monkeypatch):
        responses = iter(['José'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio12()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio12_4(self, monkeypatch):
        responses = iter(['JOSÉ'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio12()
        assert type(retorno) is bool
        assert retorno


class Testcapitulo3Exercicio13():
    def test_capitulo3_exercicio13_1(self, monkeypatch):
        responses = iter(['José da Silva Júnior'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio13()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio13_2(self, monkeypatch):
        responses = iter(['JOSÉ DA SILVA JÚNIOR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio13()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio13_3(self, monkeypatch):
        responses = iter(['josé da silva'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio13()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio13_4(self, monkeypatch):
        responses = iter(['josé'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio13()
        assert type(retorno) is bool
        assert retorno


class Testcapitulo3Exercicio14():
    def test_capitulo3_exercicio14_1(self, monkeypatch):
        responses = iter(['José'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio14()
        assert type(retorno) is str
        assert retorno == 'Nome Simples'

    def test_capitulo3_exercicio14_2(self, monkeypatch):
        responses = iter(['JOSÉ JÚNIOR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio14()
        assert type(retorno) is str
        assert retorno == 'Nome Composto'

    def test_capitulo3_exercicio14_3(self, monkeypatch):
        responses = iter(['José da Silva'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio14()
        assert type(retorno) is str
        assert retorno == 'Nome Composto'

    def test_capitulo3_exercicio14_4(self, monkeypatch):
        responses = iter(['João'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio14()
        assert type(retorno) is str
        assert retorno == 'Nome Simples'


class Testcapitulo3Exercicio15():
    def test_capitulo3_exercicio15_1(self, monkeypatch):
        responses = iter(['José'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio15()
        assert type(retorno) is str
        assert retorno == 'ésoJ'

    def test_capitulo3_exercicio15_2(self, monkeypatch):
        responses = iter(['JOSÉ JÚNIOR'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio15()
        assert type(retorno) is str
        assert retorno == 'ROINÚJ ÉSOJ'

    def test_capitulo3_exercicio15_3(self, monkeypatch):
        responses = iter(['José da Silva'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio15()
        assert type(retorno) is str
        assert retorno == 'avliS ad ésoJ'

    def test_capitulo3_exercicio15_4(self, monkeypatch):
        responses = iter(['João'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio15()
        assert type(retorno) is str
        assert retorno == 'oãoJ'
        

class Testcapitulo3Exercicio16():
    def test_capitulo3_exercicio16_1(self, monkeypatch):
        responses = iter(['senha1', 'senha1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio16()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio16_2(self, monkeypatch):
        responses = iter(['senha1', 'senha2'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio16()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio16_3(self, monkeypatch):
        responses = iter(['Senha1', 'senha1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio16()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio16_4(self, monkeypatch):
        responses = iter(['Senha1', 'senh@1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio16()
        assert type(retorno) is bool
        assert not retorno


class Testcapitulo3Exercicio17():
    def test_capitulo3_exercicio17_1(self, monkeypatch):
        responses = iter(['senha1', 'senha1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio17()
        assert type(retorno) is str
        assert retorno == 'Senhas são idênticas'

    def test_capitulo3_exercicio17_2(self, monkeypatch):
        responses = iter(['senha1', 'senha2'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio17()
        assert type(retorno) is str
        assert retorno == 'Senhas diferentes'

    def test_capitulo3_exercicio17_3(self, monkeypatch):
        responses = iter(['Senha1', 'senha1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio17()
        assert type(retorno) is str
        assert retorno == 'Senhas diferentes'

    def test_capitulo3_exercicio17_4(self, monkeypatch):
        responses = iter(['Senha1', 'senh@1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio17()
        assert type(retorno) is str
        assert retorno == 'Senhas diferentes'


class Testcapitulo3Exercicio18():
    def test_capitulo3_exercicio18_1(self, monkeypatch):
        responses = iter(['123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio18()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio18_2(self, monkeypatch):
        responses = iter(['senha1', '123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio18()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio18_3(self, monkeypatch):
        responses = iter(['senha1', 'senha2', '123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio18()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio18_4(self, monkeypatch):
        responses = iter(['senha1', 'senha2','senha1','123senha', '123mudar'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio18()
        assert type(retorno) is bool
        assert retorno


class Testcapitulo3Exercicio19():
    def test_capitulo3_exercicio19_1(self, monkeypatch):
        responses = iter(['Frase sem vogal'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio19()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio19_2(self, monkeypatch):
        responses = iter(['A frase tem vogal'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio19()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio19_3(self, monkeypatch):
        responses = iter(['Ovo'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio19()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio19_4(self, monkeypatch):
        responses = iter(['ovO'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio19()
        assert type(retorno) is bool
        assert retorno


class Testcapitulo3Exercicio20():
    def test_capitulo3_exercicio20_1(self, monkeypatch):
        responses = iter(['Frase sem vogal no final'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio20()
        assert type(retorno) is bool
        assert not retorno

    def test_capitulo3_exercicio20_2(self, monkeypatch):
        responses = iter(['Frase termina com a vogal e'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio20()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio20_3(self, monkeypatch):
        responses = iter(['Ovo'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio20()
        assert type(retorno) is bool
        assert retorno

    def test_capitulo3_exercicio20_4(self, monkeypatch):
        responses = iter(['ovO'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        retorno = capitulo3_exercicio20()
        assert type(retorno) is bool
        assert retorno