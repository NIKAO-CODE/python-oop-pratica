class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descrever_pessoa(self):
        print(f"Nome: {self.nome} - Idade: {self.idade}")


class Turma:
    def __init__(self, disciplina):
        self.disciplina = disciplina
        self.alunos_matriculados = []
        self.qtd_alunos_matriculados = 0

    def matricular_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)
        self.qtd_alunos_matriculados += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        if self.matricula == 2023:
            disciplinas = ["Algoritmos", "Estrutura de Dados"]
            print(f"Disciplinas do aluno {self.nome}: {disciplinas}")
        else:
            print("Matrícula inválida.")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self, turma):
        if turma.qtd_alunos_matriculados > 0:
            print("Os alunos da turma são:")
            for aluno in turma.alunos_matriculados:
                aluno.descrever_pessoa()
        else:
            print("Não há alunos na turma.")


# Criação dos objetos Aluno, Turma e Professor
aluno1 = Aluno("Nícolas", 27, 2023)
aluno2 = Aluno("Mariana", 24, 2023)
aluno1.estudar()

turma_algoritmos = Turma("Algoritmos")
turma_algoritmos.matricular_aluno(aluno1)
turma_algoritmos.matricular_aluno(aluno2)

professor1 = Professor("Itche Baran", 68, "Algoritmos")
professor1.descrever_pessoa()
professor1.ensinar(turma_algoritmos)
