class moto:
    def __init__(self,modelo,ano,cor):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        pass

minha_moto=moto("F-324",2005,"preta")
sua_moto=moto("F-4535",2002,"cinza")

print("Minha moto\nCor",minha_moto.cor,"\nAno",minha_moto.ano,"\nModelo",minha_moto.modelo)
print("\n\n")
print("Sua moto\nCor",sua_moto.cor,"\nAno",sua_moto.ano,"\nModelo",sua_moto.modelo)