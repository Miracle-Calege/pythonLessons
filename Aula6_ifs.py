# if-> e uma estrutura de condicao que determina a execucao de determinadas instrucoes consoante ao cumprimento de determinadas condicoes

"""
estrutura:

if condicao:
instrucao
elif condicao: -> caso a instrucao acima nao seja cumprida
instrucao
else:  -> usado caso nenhuma das condicoes seja cumprida
instrucao
"""


idade=int(input("Insira sua idade:"))
if idade>=100:
    print("muito velho")
if idade>=18:
    print("Maior de 18")
elif idade<0:
    print("feto")
else:
    print("Cresca")