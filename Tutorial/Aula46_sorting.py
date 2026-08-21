"""
Para ordenar in python usamos o metodo sort() or sorted().

usamos sort() com listas

sorted() com tuples,dicionarios e objectos.NB: O sorted metodo depois de ordenar retorna uma lista, por isso devemos fazer um cast
"""

#*****************Lista************************
frutas=["banana","orange","apple","coconut"]

frutas.sort()#organiza os elementos em ordem crescente.
# frutas.sort(reverse=True) coloca em ordem decrescente

print(frutas)

#*****************Tuplas************************
frutas2=("banana","orange","apple","coconut")

frutas2=tuple(sorted(frutas2))#cast
print(frutas2)


#************************dicionario*******************************


frutas3={"banana":105,"orange":73,"apple":72,"coconut":354}

frutas3=dict(sorted(frutas3.items()))

print(frutas3)