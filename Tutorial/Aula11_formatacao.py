#formatacao={valor:flags} formata um valor baseado na flag inserida

preco1=3.14159
preco2=-987.65
preco3=1200.34
#f-> determina o numero de casas decimais a serem exibidas em numeros decimais.
#Estrutura: .numeroCasasDesejadasf.
print(f"preco 1 e {preco1:.2f}")# serao exibidos os precos com 2 casas decimais
print(f"preco 2 e {preco2:.3f}")# serao exibidos os precos com 3 casas decimais
print(f"preco 3 e {preco3:.5f}")# serao exibidos os precos com 5 casas decimais

#numeros(numero apos ":")-> determina o espaco para a quantidade de digitos a serem exibidos(o espaco e acrescentado no lado esquerdo)
print(f"Preco 1 e {preco1:10}")#vai ser exibido em espaco para albergar 10 digitos/numeros
print(f"Preco 2 e {preco2:10}")
print(f"Preco 3 e {preco3:10}")

#padding-> colocamos o valor para fazer o padding + o espaco para a quantidade de digitos
#Estrutura: zeroEspacoDigitos

print(f"Preco 1 e {preco1:010}")#vai ser adicionado zero para preencher o espaco a esquerda
print(f"Preco 2 e {preco2:010}")
print(f"Preco 3 e {preco3:010}")

#right justify.
#Estrutura: > quantidade de digitos a serem exibidos
print(f"Preco 1 e {preco1:>10}")
print(f"Preco 2 e {preco2:>10}")
print(f"Preco 3 e {preco3:>10}")

#left justify.
#Estrutura: < quantidade de digitos a serem exibidos
print(f"Preco 1 e {preco1:<10}")
print(f"Preco 2 e {preco2:<10}")
print(f"Preco 3 e {preco3:<10}")

#centralizado
#Estrutura: ^ quantidade de digitos a serem exibidos
print(f"Preco 1 e {preco1:^10}")
print(f"Preco 2 e {preco2:^10}")
print(f"Preco 3 e {preco3:^10}")

#Exibir o "+"
#Estrutura: +
print(f"Preco 1 e {preco1:+}")
print(f"Preco 2 e {preco2: }")
print(f"Preco 3 e {preco3: }")

#Exibir o ",".Separa cada milhar por virgula
#Estrutura: ,
print(f"Preco 1 e {preco1:,}")
print(f"Preco 2 e {preco2: ,}")
print(f"Preco 3 e {preco3: ,}")

#E possivel misturar flags
#Estrutura {valor:flag flag2 flag3 flagN}

print(f"Preco 1 e {preco1:+,.2f}")
print(f"Preco 2 e {preco2:+,.2f}")
print(f"Preco 3 e {preco3:+,.2f}")