""""
Composition->e uma relacao onde um objecto possui o outro em que um nao pode existir sem o outro

composicao-> cria-se os objectos secundarios dentro do objecto principal

ex:criamos o motor e os pneus dentro do carro(do seu constructor)

se deletarmos o carro tudo desaparece

"""

class Motor:
    def __init__(self,cavalos):
        self.cavalos = cavalos

class Pneu:
    def __init__(self,tamanho):
        self.tamanho = tamanho

class Carro:
    def __init__(self,marca,modelo,cavalos,tamanho):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(cavalos)
        self.cavalos = cavalos
        self.pneu =[Pneu(tamanho) for roda in range(4)]#vai criar 4 pneus

    def exibirCarro(self):
        return f"{self.marca} {self.modelo} {self.motor.cavalos} {self.pneu[0].tamanho}"


carro=Carro("ford","Mustang",500,18)
print(carro.exibirCarro())
