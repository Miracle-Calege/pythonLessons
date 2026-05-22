"""
collection-> uma estrutura usada para guardar multiplos valores
list=[] ordenados e mutaveis.Aceita dados duplicados
set={} desordenadas e imutaveis.Nao aceita dados duplicados
tuples=() ordenada e imutavel.Aceita dados duplicados.Mais rapido

Como usar:
variavel= {dado1,dado2,dado3,...}.se usarmos "{}" e uma set, "[]" list e "()" tuple.
Para acessar a posicoes variavel/{ind}/[ind]/(ind).O mesmo feito em strings
dir(variavel)->retorna todos os metodos disponiveis para estrutura
help(variavel)->retorna todos os metodos disponiveis e as descricoes para estrutura
Metodos:
len(variavel)->retorna o tamanho da estrutura
"elemento"/valor in variavel->retorna um valor logico verificando se o elemento faz parte da estrutura
append(elemento)-> adiciona o elemento ao fim da lista
remove(elemento)-> remove o elemento da lista
insert(indice,elemento)-> insere o elemento no indice especificado
sort()-> organiza a lista em ordem crescente
reverse()->organizar a lista em ordem decrescente
clear()->apaga todos elementos
index(valor)-> retorna o indice o valor/elemento
count(elemento)->conta quantas vezes o elemento aparece na lista

"""


frutas=["maca","laranja","uva","manga"]
#
# print(frutas)#imprimindo a lista
# print(frutas[1])#imprime laranja
# print(frutas[0:3:2])

# for fruta in frutas:#iterando pela lista
#     print(fruta)
#
# print(dir(frutas))
# print(help(frutas))

print(len(frutas))
print("banana" in frutas)
frutas.append("banana")
print(frutas)
frutas.remove("maca")
print(frutas)
frutas.insert(0,"morango")
print(frutas)
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
# frutas.clear()
# print(frutas)
print(frutas.index("morango"))
print(frutas.count("morango"))
