
class Pessoa:

    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero


pessoa1 = Pessoa("Nícolas", 27, "masculino")
pessoa2 = Pessoa("Mariana", 24, "feminino")

print("O {} está com {} anos e é do sexo {}.".format(pessoa1.nome, pessoa1.idade, pessoa1.genero))
print("A {} está com {} anos e é do sexo {}.".format(pessoa2.nome, pessoa2.idade, pessoa2.genero))
