"""
iterable-> e um objecto ou coleccao que pode retorna os seus elementos um por um permitindo iterando sobre o loop

Estrutura:

for var in estrutura: o var vai pegar cada elemento  da estrutura de dados
print(var)-> caso queiramos imprimir

"""

numeros=[1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero, end=" ")

print()

for  numero in reversed(numeros):#na ordem inversa
        print(numero, end=" -")