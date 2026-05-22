"""
Uma coleccao de matriz baseada em lists, ou seja, e um conjuntos de lists
variavel={list1,list2,list3,...}
Acessando:
variavel[linhas][colunas]
exemplo
variavel[0]-> retorna a primeira lista
variavel[0][0]-> retorna o primeiro elemento da primeira lista

NB: tambem podemos criar um 2D tuples ou sets
"""

frutas=["maca","laranja","uva","manga"]
vegetais=["cenoura","batata","beterraba"]
carnes=["frango","peru","porco"]

compras=[frutas,vegetais,carnes]#criamos um list 2D
#
# print(compras)#imprimindo  a estrutura
#
# print(compras[0])#retorna list frutas
# print(compras[0][0])#retorna maca

#acessando os elementos usando uma estrutura for

for lista in compras:#este for acessa as lists
    for elemento in lista:#este for acessa os elementos das lists
        print(elemento, end=" ")
    print()


