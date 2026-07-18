"""
Heranca-> e o processo de um objecto herdar caracteristicas de um outro

Para uma classe herdar a outro usa a seguinte estrutura:

class filho(pai): -> o filho herda as caracteristicas do pai

NB:A classe filha alem de herdas as caracteristicas do pai tambem pode ter as suas proprias
"""


class Animal:
    def __init__(self,nome):
        self.nome = nome
        self.estaVivo=True

    def comer(self):
        print(f"{self.nome} esta comendo")

    def dormir(self):
        print(f"{self.nome} esta dormir")

class Cao(Animal):
    def latir(self):
        print("Uff")

class Gato(Animal):
    def miar(self):
        print("Miau")

class Rato(Animal):
    def Som(self):
        print("Som de rato")


snop=Cao('Snop')
gato=Gato('xipixe')
mouse=Rato('Mouse')
snop.comer()
snop.dormir()
snop.latir()
print(snop.nome)
print(snop.estaVivo)
gato.miar()
print(gato.nome)
print(mouse.nome)
mouse.Som()