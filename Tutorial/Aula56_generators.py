"""
Generator->éé uma tipo de funcao especial que retorna um objecto iterator. Invés de "return" para retornar um único valor, usa "yield"(nao impede que o codigo que vem abaixo do yield seja executado) para produzir uma série de resultados.
"""

def fun(max):#criamos a funçao
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1


for n in fun(5):#percorremos a funçao
    print(n)