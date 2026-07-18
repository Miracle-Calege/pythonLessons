"""
Variaveis de classe-> sao aquelas partilhadas por todas as instancias da classe, sao aquelas criadas fora do constructor
Variaveis de instancia-> aquelas criadas dentro do constructor

NB: É boa práctica usar variaveis de classe usando nome da classe
"""


class Estudante:
    ano=2024
    numeroEstudante=0
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        Estudante.numeroEstudante+=1



estudante1=Estudante("Miracle Calege", 18)
estudante2=Estudante("Siswe Calege", 20)

print(estudante1.nome)
print(estudante1.idade)
print(Estudante.ano)
print(Estudante.numeroEstudante)

