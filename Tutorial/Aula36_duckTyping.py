"""
duck typing-> e o outro jeito de implementar polimorfismo sem precisar de usar heranca
Os objectos devem ter o minimo de atributos e metodos necessarios
"""

class Animal:
    alive=True

class Cao(Animal):

    def falar(self):
        print("Woof!")

class Gato(Animal):
    def falar(self):
        print("Meow!")

class Carro:# assim que o carro tem o mesmo metodo que os de mais vai ser considerado do mesmo tipo que os de mais
    def falar(self):
        print("HONK!")

animais=[Cao(),Gato(),Carro()]

for animal in animais:
    animal.falar()
