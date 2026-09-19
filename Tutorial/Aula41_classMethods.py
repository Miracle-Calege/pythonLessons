"""
Class methods-> geralmente usados para criar um constructor alternativo ou manipular variáveis da classe. Sao acessados usando o nome da classe.metodo.
"""

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)


p = Person.from_birth_year("Jake", 2000)
print(p.name)
print(p.age)