class Cliente:

    def __init__(self, nome):
        self.nome = nome

    #Os métodos que dão acesso são nomeados como properties
    #É utilizado para dar acesso aos metodos sem a utilização de ()
    @property
    def nome(self): 
       return self.nome.title()