"""
nested loop-> e a ocorrencia de um loop dentro do outro
loop externo:
    loop interno:
"""

for x in range(3):#conta de 0 ate 2(tres vezes)
    for  i in range (1,10):
        print(i,end="")
    print()    # este print deve estar alinha ao loop interno para indicar que nao faz parte do interno, mas sim do externo
