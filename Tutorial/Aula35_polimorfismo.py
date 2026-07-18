"""
Poliformismo-> uma palavra grega que significa muitas formas

Polimorfismo pode ser atingido via:
1.Heranca
2.Duck typing
"""

from abc import ABC, abstractmethod

class Forma:

    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio

    def area(self):
        return 3.14*self.raio**2

class Quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado**2

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura*0.5


formas=[Circulo(4),Quadrado(5),Triangulo(6,7)]

for forma in formas:
    print(f"{forma.area()}")

