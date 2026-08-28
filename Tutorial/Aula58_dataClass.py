"""
data class->é um tipo de classe que guardada dados e evita que escrevamos muitos "boilerplate code"
Gera automaticamente : __init__,__repr__,__eq__
"""

#fazemos este import para classificarmos uma classe como dataclass
from dataclasses import dataclass,field#importamos também o field para a linha 15

#marcamos  a classe com @dataclass
@dataclass #(frozen=True) #faz com que os objectos sejam imutáveis(nao vamos poder inicializar com outro valor)
class Person:
#inves de criamos um constructor listamos os atributos e os seus tipos
    name:str
    age:int
    password:str=field(repr=False)#torna oculto esta atributo quando imprimirmos o objecto
    is_alive:bool=True
    def __post_init__(self):#é um magic method executado logo apos init
        if self.age < 0:
            raise ValueError("Age can't be negative")

person1=Person(name="Miracle", age=30,password="jsjsjs")
print(person1)
person2=Person("Siswe",20,password="jdjdjkdmjdok")
print(person2)