#from conta import Conta

#funciona passar um objeto no init de uma classe python, mesmo sem necessidade de importar para o arquivo
class Correntista:
    def __init__(self, nome, cpf, Conta):
        self.__cpf = cpf
        self.__nome = nome
        #limite está em conta não em correntista
        #self.__limite = limite
        self.__conta = Conta

    def getCpf(self):
        return self.__cpf
    
    def setCpf(cpf):
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome

    def setNome(nome):
        self.__nome = nome
        
    #tá tudo tranquilo enquanto não tá usando esse metodo...
    def addConta(self):
        self.__conta = Conta()
        
    def getConta(self):
        if(self.__conta == None):
            raise RuntimeError("Cliente não possui conta no banco")
        return self.__conta
        
