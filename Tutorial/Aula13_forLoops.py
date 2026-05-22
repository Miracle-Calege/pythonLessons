"""
for loop-> executa um instrucao durante um numero fixo de vezes que itera num intervalo

Estrutura:

for variavel in range(inicio, fim,variacao):
instrucao

variavel-> e que vai assumir os valores no intervalo
nb:fim=fim-1, ou seja nao alcancaremos o valor actual do fim mas sim o seu antecesssor

continue-> usado para saltar uma iteracao
break-> usado para parar o for numa iteracao
"""

# for  i  in range (1,11):
#     print(i)
#
# print("fim")
#
#
#
#
# for  i  in range (1,11,2):
#     print(i)
#     print("o for varia 2 iteracoes")
# print("fim")

for i in range(1,10):
    if i % 2 == 0:
        continue
    else :
        print(i)
print("imprimimos apenas numeros impares")

for i in range(1,10):
    if i == 3:
       break
    else:
       print(i)
print("imprimimos ate 2")

for  i  in reversed(range(1,11,2)):#usamos a funcao reversed para reverter a ordem de impressao
    print(i)
print("fim")

card="1234-5678-9012-3456"

for i in card: #iterando sobre uma string
    print(i)

for i in range(1,10):
 print(i,end="")#print imprime e salta uma linha, usamos o end para determinar o comportamento do print