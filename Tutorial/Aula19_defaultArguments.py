"""
default arguments-> um valor padrao para certos parametros, e usado quando o argumento e omitido quando invocamos a funcao

Construcao:
def nomeFuncao(y,x=valor):

NB:def nomeFuncao(x=valor,y): colocar assim estaria errado, devemos primeiro colocar os argumentos "normais" e depois o default
chamada::

nomeFuncao(y)

NB:Para default argumentos inicializamos o parametro com um valor e na chamada usamos apenas o parametro que nao foi inicializado
"""

def preco(preco,desconto=0,taxa=0.05):
    return preco *(1-desconto) * (1+ taxa)

#print(preco(500))
print(preco(500,0.1))#mas se adicionarmos um argumento correspondente ao desconto ou taxa o compilador vai usar esse valor colocado e nao o default.