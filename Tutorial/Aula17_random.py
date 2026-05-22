"""
devemos importar primeiro o modulo random

Como usar:
random.funcao()
Funcoes/metodos:
randint(inicio,fim)-> retorna um valor no intervalo do [inicio,fim]
random()-> retorna um valor no intervalo de [0,1[
choice(estrutura)-> escolhe um valor aleatorio na estrutura
shuffle(estrurura)-> "baralha" uma estrutra
"""
import random

#print(help(random))

print(random.randint(1,6))#gera um numero aleatorio entre 1 e 6
print(random.random())

opcoes=("pedra","papel","tesoura")
cartas=["2","3","4","5","6","7","8","9","10","j","q","k","M"]
random.shuffle(cartas)
print(random.choice(opcoes))
print(cartas)