from datetime import datetime

class Livro:

    def __init__(self, titulo, autor, ano_publicacao, genero, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.numero_paginas = numero_paginas

    
    def imprime_informacoes(self):
        print("O livro {} foi publicado em {} seu gênero é {} possui {} páginas e foi escrito por {}.".format(self.titulo, self.ano_publicacao, self.genero, self.numero_paginas, self.autor))

    
    def anos_desde_publicacao(self):
        ano_atual = datetime.now().year
        diferenca_de_ano = ano_atual - self.ano_publicacao

        return diferenca_de_ano


livro1 = Livro("Messias: Ahavah", "Nícolas Nascimento", 2020, "Religião", 333)


livro1.imprime_informacoes()
print("Se passaram {} anos desde a publicação do livro.".format(livro1.anos_desde_publicacao()))
