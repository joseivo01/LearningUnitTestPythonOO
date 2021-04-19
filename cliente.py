class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    #Os métodos que dão acesso são nomeados como properties
    #É utilizado para dar acesso aos metodos sem a utilização de ()
   
    def get_nome(self): 
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
        
    def get_cpf(self): 
        return self.nome

    def set_cpf(self, cpf):
        self.cpf = cpf