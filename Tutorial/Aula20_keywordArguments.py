"""
keyword arguments-> e um argumento precedido por um identificador que ajuda na legibilidade
E vantajoso pois nao ha obrigatoriedade dos argumentos seguires a ordem dos parametros

ex:

Criacao:
def nomeFuncao(x,y):

chamada:

nomeFuncao(y=10,x=7) assim o compilador sabera a que parametro cada valor pertence

"""


def ola(saudacoes,titulo,primeiro,ultimo):
    print(f"{saudacoes} {titulo} {primeiro} {ultimo}")


ola(primeiro="Miracle",titulo="sr",saudacoes="Cordiais saudacoes!",ultimo="Calege")