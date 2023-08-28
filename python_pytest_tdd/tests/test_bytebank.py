from codigo.bytebank import Funcionario
import pytest
from pytest import mark

# Crie uma classe chamada Test classe
# Crie uma função cujo nome descreva o teste, ainda que fique comprido. O nome da função deve ser o mais verboso possível
# coloque na função três situações:
#   Given-Contexto
#   When-Ação
#   Then-Desfecho
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-contexto
        esperado = 23

        Funcionario_teste = Funcionario('Test', entrada, 1111) # Criando objeto da classe
        
        resultado = Funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    @mark.skip (reason="Não quero executar isso agora")
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000 

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # given
        esperado = 100

        funcionario_teste = Funcionario('', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 # given

            funcionario_teste = Funcionario('', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus() # when

            assert resultado # then
    
    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000 # given
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        Funcionario_test = Funcionario(nome, data_nascimento, salario)
        resultado = Funcionario_test.__str__() # when

        assert resultado == esperado # then