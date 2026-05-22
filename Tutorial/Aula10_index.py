#indexacao-> e o acesso de elementos de uma sequencia usando
# [incio:fim:passo]


numero="1234-5678-9012-3456"

#print(numero[0]) acessamos o primeiro caracter da string
print(numero[0:4])#imprime os valores da posicao inicio ate a posicao fim-1.podemos colocar so o fim(ex: [:4]) o compilador vai concluir que estamos a partir de zero
print(numero[5:9])#se colocarmos [5:](vao ser impressos todos os numeros a partir de 5)
print(numero[-1])# -1 retornar o ultimo valor, -2 o penultimo assim sucessivamente

# passo

print(numero[::2])#imprime elemento em cada intervalo de dois, partindo do indice zero


ultimos_digitos=numero[-4:]
print(f"-{ultimos_digitos}")
