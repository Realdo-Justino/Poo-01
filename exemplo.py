class carro:
    def __init__(self,modelo,ano,cor):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        pass

meu_carro=carro("fusca",1987,"azul")

print(meu_carro.modelo)