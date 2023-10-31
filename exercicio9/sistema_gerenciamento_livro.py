
class Livro:

    def __init__(self, titulo, autor, genero):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.genero = genero.title()
        self.disponivel = True


    def emprestimo(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso.")
        else:
            print(f"O Livro {self.titulo} está indisponível no momento.")


    def devolucao(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso.")
        else:
            print(f"O Livro {self.titulo} já está disponivel no momento.")



class Biblioteca:
    
    def __init__(self):
        self.catalogo = []

    def adicionar(self, livro):
        self.catalogo.append(livro)
        print(f"O livro {livro.titulo} foi adicionado na biblioteca.")


    def remover(self, livro):
        if (livro in self.catalogo):
            self.catalogo.remove(livro)
            print(f"O livro {livro.titulo} foi removido da biblioteca.")
        else:
            print(f"O livro {livro.titulo} não está na biblioteca.")


    def listar_livros(self):
        if not self.catalogo:
            print("A biblioteca está vazia.")
        else:
            print("-" * 50)
            print("Livros disponíveis")
            for livro in self.catalogo:
                if livro.disponivel:
                    print(f"Título: {livro.titulo} - Autor: {livro.autor} - Gênero: {livro.genero}")
        print("-" * 50)


# criando objetos
livro1 = Livro("Adonai: Meu Criador", "Nícolas", "Religião")
livro2 = Livro("O verdadeiro Ahavah", "Nícolas", "Religião")
livro3 = Livro("A mentira contada para todos", "tontos", "Ficção")

biblioteca = Biblioteca()

biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.adicionar(livro3)
biblioteca.listar_livros()


livro1.emprestimo()
livro2.emprestimo()

biblioteca.listar_livros()

livro2.devolucao()
biblioteca.remover(livro3)

biblioteca.listar_livros()
