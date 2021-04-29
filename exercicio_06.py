class moto:
    def __init__(self,modelo,ano,cor):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        
class moto2(moto):
    def __init__(self,modelo,ano,cor,km):
        super().__init__(modelo,ano,cor)
        self.km=km
minha_moto=moto2("F-324",2005,"preta",12)
sua_moto=moto2("F-4535",2002,"cinza",15)

print("Minha moto\nCor",minha_moto.cor,"\nAno",minha_moto.ano,"\nModelo",minha_moto.modelo,"\nKM",minha_moto.km)
print("\n\n")
print("Sua moto\nCor",sua_moto.cor,"\nAno",sua_moto.ano,"\nModelo",sua_moto.modelo,"\nKM",sua_moto.km)