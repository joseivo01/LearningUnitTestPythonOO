from random import randint

import Conta from conta

#classe focada em executar as funções do banco
class Banco:
    #TO DO: toda essa classe python e aplicar seus respectivos testes unitários...

    contas = []
    def criarConta(nome,cpf):
        conta = Conta()
        #adicionar um a um
        conta.numero(geradorDeNumeroConta())

    #gerador de numeros
    def geradorDeNumeroConta():
        sorteado = sample(range(0, 100), 4)
        return sorteado
