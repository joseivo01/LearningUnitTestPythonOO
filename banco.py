from random import randint

import Conta from conta

#classe focada em executar as funções do banco
class Banco:

    contas = []


    def criarConta(nome,cpf):
        conta = Conta()
        #adicionar um a um
        conta.numero(geradorDeNumeroConta())

    #gerador de numeros
    def geradorDeNumeroConta():
        sorteado = sample(range(0, 100), 4)
        return sorteado
