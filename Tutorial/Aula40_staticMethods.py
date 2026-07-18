"""
Metodos estaticos-> sao aqueles que pertencem a classe e nao somente a uma instancia

Devemos adicionar acima do metodo @staticmethod para tornar o metodo estatico

Para acessar o metodo estatico so usamos o nome da classe.metodo()
"""

class Funcionario:
    def __init__(self,nome,posicao):
        self.nome = nome
        self.posicao = posicao

    def info(self):
        return f"{self.nome}={self.posicao}"


    @staticmethod
    def posicaoValida(posicao):
        valido=["Gerente","Caixa","Cook","Jardineiro"]
        return  posicao in valido


print(Funcionario.posicaoValida("cientista"))