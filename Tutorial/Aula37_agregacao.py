""""
Agregacao-> e a representacao de uma relacao onde contem a referencia de um ou mais objectos independentes
NB:Cada objecto pode existir de forma independente


Na agregacao os objectos sao criados separadamente
"""

class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.livros=[]#criamos uma biblioteca que tem um lista de livros

    def adicionarLivros(self,livro):
        self.livros.append(livro)

    def exibirLivros(self):
        return [f"{livro.titulo} por {livro.autor}" for livro in self.livros]

class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

#criamos a biblioteca
biblioteca=Biblioteca("Brazzau Mazula")

#criamos os livros
livro1=Livro("Paulina Chiziane","Baladas de amor ao vento")
livro2=Livro("Mia Couto","Ultimo voo do flamingo")
livro3=Livro("Ungulane ba kha cossa","Ualalapi")


biblioteca.adicionarLivros(livro1)
biblioteca.adicionarLivros(livro2)
biblioteca.adicionarLivros(livro3)
print(biblioteca.nome)

print(biblioteca.exibirLivros())