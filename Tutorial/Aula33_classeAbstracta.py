"""
classes abstractas sao aqueles que nao podem ser instanciadas(nao podemos criar um objecto com elas)
Podem ter tambem metodos abstractos(sem implementacao)

NB:precisamos de fazer este import: from abc import ABC, abstractmethod

1.Tornar a classe abstracta
class nome(ABC):


2.tornar o metodo abstracto
@abstractmethod

def nome(self):
"""
from abc import ABC, abstractmethod

#para tornarmos o metodo abstracto devemos passar como parametro o ABC

class Veiculo(ABC):

    #para indicar que o metodo e abstracto devemos usar : @abstractmethod
    @abstractmethod
    def ir(self):
        pass

    @abstractmethod
    def parar(self):
        pass


   # veiculo=Veiculo() esta instancia nao sera possivel

#se uma classe estiver a herdar de uma classe abstracta e obriga a implementar os metodos abstractos
#quando implementarmos os metodos abstractos removemos a notacao

class Carro(Veiculo):

    def ir(self):
       print("Em movimento")


    def parar(self):
        print("Em repouso")



carro=Carro()

carro.ir()
carro.parar()