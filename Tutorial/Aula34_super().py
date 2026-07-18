"""
Super()->funcao usada nas classes filhas para chamar metodos da classe pai(superclasse)
permite herdar funcionalidade dos metodos herdados

Inves de repetirmos os mesmos atributos em classes diferentes podemos criar uma classe generica que tera todos atributos em comum e que serao herdados por outras classes
esses atributos comuns serao partilhados usando o super().constructor(atributos)

super().metodo-> estamos a herdar a mesma implementacao do metodo da superclasse
ou podemos subscrever(chamar o metodo que esta na superclasse mas dar uma implementacao diferente)

"""
class Forma:
    #constructor com os atributos comuns
    def __init__(self,cor,preenchido):
        self.cor = cor
        self.preenchido = preenchido
    def descricao(self):
        print(f"{self.preenchido} - {self.cor}")

class Circulo(Forma):
    def __init__(self,cor,preenchido,raio):
        #super() chamando o constructor da superclasse
        super().__init__(cor,preenchido)
        self.raio = raio

    #sobrescrevemos este metodo
    def descricao(self):
        print(f"Area:{3.14*self.raio*self.raio}")


class Quadrado(Forma):
    def __init__(self,cor,preenchido,largura):
        super().__init__(cor, preenchido)
        self.largura = largura



class Triangulo(Forma):
    def __init__(self,cor,preenchido,largura,altura):
        super().__init__(cor, preenchido)
        self.largura = largura
        self.altura = altura


circulo=Circulo("red",True,10)

#print(circulo.cor)

circulo.descricao()