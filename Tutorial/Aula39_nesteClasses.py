"""
Nested class-> uma classe dentro da outra

No exemplo abaixo a classe Funcionario esta dentro da classe Empresa
"""

class Empresa:
    class Funcionario:
        def __init__(self,nome,posicao):
            self.nome = nome
            self.posicao = posicao

        def detalhar(self):
            return f"{self.nome} {self.posicao}"

    def __init__(self,nome):
        self.nome = nome
        self.funcionarios = []

    def adicionarfuncionario(self,nome,posicao):
         novoFuncionario = self.Funcionario(nome,posicao)
         self.funcionarios.append(novoFuncionario)


    def listarfuncionarios(self):
        return [funcionario.detalhar() for funcionario in self.funcionarios]



empresa=Empresa("Clicks e Bits")

empresa.adicionarfuncionario("Miracle","PCA")
empresa.adicionarfuncionario("Siswe","Desenvolvedor de Software")

print(empresa.listarfuncionarios())