"""
Objecto-> um conjunto de atributos(variaveis) e metodos(funcoes) relacionaos

Para criar objectos precisamos de classes

para criarmos uma class usamos a palavra class nomeClasse:
ex: class Animal:

Para criarmos um objecto precisamos de um metodo especial chamado contructor:

def__init__(self, atributo1,atributo2,...atributoN):
 self.atributo1 = atributo1
 .
 .
 .
 self.atributoN = atributoN

NB:O self sempre estará presente, pois refere-se ao proprio objecto

ex:  def __init__(self,modelo,ano,cor,aVenda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.aVenda = aVenda

Para instanciarmos um objecto fazemos o seguinte:
nomeAsuaEscolha=Objecto(atributo1,...atributoN)


NB:print(Objecto) nao vai imprimir o objecto, mas sim o endereco de memoria onde esta localizado
Para imprimir os atributos devemos fazer : print(Nome.atributo)

*************************Metodos******************************
NB:criamos do mesmo jeito que criamos funcoes, mas neste caso o self sera sempre o primeiro parametro
"""

class Carro:
    def __init__(self,modelo,ano,cor,aVenda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.aVenda = aVenda

    def conduzir(self):
            print(f"Conduzindo{self.modelo}")


    def parar(self):
            print(f"Parado")

    def caracteristicas(self):
        print(f"{self.modelo}  {self.ano}  {self.cor}  {self.aVenda}")