class Conta:

    # self é a referência que sabe encontrar o objeto construído em memória.
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        return "O titular: {} possui um saldo de {}R$".format(self.__titular, self.__saldo)
        
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.get_saldo() < valor):
            raise RuntimeError("Valor de saldo insuficiente")
        self.__saldo -= valor

    def transfere(self, valor, destino):
        if(self.get_saldo() < valor):
            raise RuntimeError("Valor de saldo insuficiente")
        if(destino == None):
            raise RuntimeError("Destinatario não existe!")
        if(destino.get_limite_disponivel() < valor):
            raise RuntimeError("Destinatario não possui limite disponivel suficiente")
        self.saca(valor)
        destino.deposita(valor)
        
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite_total(self):
        return self.__limite
    
    def get_limite_disponivel(self):
        #limite disponivel é o limite total menos oque que já tem
        limite_disponivel_uso = self.get_limite_total() - self.get_saldo()
        return limite_disponivel_uso
    
    def set_limite(self, limite):
        self.__limite = limite


pass
   
