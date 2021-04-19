class Datas:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return "Data: {}/{}/{}".format(self.dia, self.mes, self.ano)
