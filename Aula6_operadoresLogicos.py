"""
and->e verdadeira se todas as condicoes forem verdadeiras
or->e verdadeira se pelo menos uma das condicoes for verdadeira
not-> altera o valor logico da variavel
"""

# temp=25
# if temp>=0 and temp<=30:
#     print("Temperatura esta boa")# para a condicao acima este sera o output
# else:
#     print("Temperatura esta ma")

# temp=40
# if temp<=0 or temp >=30:
#     print("Temperatura esta ma")# para a condicao acima este sera o output
# else:
#     print("Temperatura esta boa")

ensolarado=True

if not ensolarado:# agora o valor logico de ensolarado e false
    print("ensolarado")
else:
    print("nublado")# esta linha sera impressa

    #escrever if ensolarado: -> e o mesmo que escrever if True:. NB: Mesmo que o valor de ensolarado seja false(na linha 19)