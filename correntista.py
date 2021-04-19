#limite é o limite que o correntista pode armazenar
class Correntista:
    def __init__(seft,cpf,nome,limite,Conta):
        self.__cpf = cpf
        self.__nome = nome
        self.__limite = limite
        self.__conta = Conta

    def getCpf(self):
        return self.__cpf
    
    def setCpf(cpf):
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome

    def setNome(nome):
        self.__nome = nome

    def getLimite(self):
        return self.__limite
    
    def getLimite(self):
        self.__limite = self.Limite

    def getConta():
        return self.__conta
