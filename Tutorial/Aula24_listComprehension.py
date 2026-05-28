"""
List comprehension-> e uma forma concisa de criar lists em python compacta e mais facil

Formula:

[instrucao estrutura de iteracao condicao]


"""
#forma tradicional
double=[]
for x in range(1,11):
    double.append(x*2)

print(double)

#list comprehension somente com estrutura de iteracao
doubles=[x*2 for x in range(1,11)]# crio um array cujo cada elemento sera duplicado

print(doubles)

#list comprehension com estrutura de iteracao e condicao

numeros=[-1,-2,3,-4,5,-6]

positivos=[num for num in numeros if num>=0] #retorna numeros positivos

print(positivos)