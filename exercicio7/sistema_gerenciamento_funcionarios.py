
class Funcionario:

    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, percentual):
        salario_ajustado = self.salario + ((self.salario * percentual) / 100)

        return salario_ajustado
        

class Empresa:

    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
        print("Funcionário(a) contratado(a): {}".format(funcionario.nome))

    def listar_funcionarios(self):
        print("Funcionários: {}: {}".format(self.nome, [funcionario.nome for funcionario in self.funcionarios]))



google = Empresa("Google")

funcionario1 = Funcionario("Nícolas", 27, "Data Enginnier", 7000.0)
funcionario2 = Funcionario("Mariana", 24, "Architect", 10000.0)

google.contratar(funcionario1)
google.contratar(funcionario2)

google.listar_funcionarios()

salario_ajustado = funcionario1.aumentar_salario(10)
print("O funcionário {} teve um aumento e seu novo salário é {}".format(funcionario1.nome, salario_ajustado))
