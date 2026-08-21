#exception->um evento que interrompe o fluxo normal de um programa(ex: divisao de um numero por zero).

"""
Estrutura
try:
codigo que pode

except Exception:
tratamento da exception

finally:(opcional)-> sempre é executado
codigo pertinente

"""
try:
    numero=int(input("Digite um numero: "))
    print(1/numero)
except ZeroDivisionError:# inves de colocar ZeroDivisionError poderiamos colocal Exception que pega todas as exceptions mas é boa prática especificar o tipo de exceccao.
    print("Nao pode dividir por zero")

except ValueError:
    print("Insira numeros")

finally:
    print("O finally sempre executa")