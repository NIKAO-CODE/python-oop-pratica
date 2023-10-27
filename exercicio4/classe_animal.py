
class Animal:

    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    
    def emitir_som(self):
        if (self.especie == "cachorro"):
            return "AuAuAu"
        elif (self.especie == "gato"):
            return "MiauMiauMiau"
        else:
            return "PiuPiuPiu"

    
cachorro = Animal("Kimi", "cachorro", 12)
gato = Animal("Billy", "gato", 5)
passaro = Animal("Bird", "passáro", 1)

print("{} faz: {}".format(cachorro.nome, cachorro.emitir_som()))
print("{} faz: {}".format(gato.nome, gato.emitir_som()))
print("{} faz: {}".format(passaro.nome, passaro.emitir_som()))
