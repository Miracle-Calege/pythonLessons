"""
expressoes condicionais->e o uso de condicionais(if-else) de forma simplificada(em uma linha)
estrutura:
instrucao se a condicao for verdadeira if condicao else instrucao se a condicao for falsa
"""

num=6
a=6
b=7

# print("Positivo" if num>0  else "negativo")

# resultado="par" if num%2==0 else "impar" #o resultado da condicional seja armazenado na variavel
# print(resultado)
max= a if a>b else b #retorna a variavel que cumprir com a condicao
print(max)