"""
heranca multipla->é o acto de herda de uma ou mais classes

class filha(pai1,pai2,...paiN):

Multiplos niveis de heranca-> herdar de um pai de herda de outro
ex:coelho herda de presa e presa herda de animal
"""

class Animal:
    def __init__(self,nome):
      self.nome = nome

    def comer(self):
     print(f'{self.nome} esta Comendo')

    def dormir(self):
     print(f'{self.nome} esta Dormindo')

class Presa(Animal):
    def fugir(self):
        print(f'{self.nome} esta Fugindo')


class Predador(Animal):
    def cacar(self):
        print(f'{self.nome} esta Cacando')

class Coelho(Presa):
    pass

class Gaviao(Predador):
    pass

class Peixe(Presa,Predador):#O peixe herda caracteristicas de presa e de predador
    pass



coelho=Coelho("Bunny")
gaviao=Gaviao("Tony")
peixe=Peixe("Memo")

coelho.comer()
coelho.dormir()
coelho.fugir()
