
class Veiculo:

    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False


class Moto(Veiculo):
    
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada


class Carro(Veiculo):
    
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
    

moto = Moto("Honda", "CBR500", 2021, 500)
carro = Carro("Mitsubishi", "ASX", 2023, "Hatch")

moto.desligar()
carro.ligar()

print("Meu carro está ligado? {}".format(carro.ligado))
print("Minha moto está ligada? {}".format(moto.ligado))
