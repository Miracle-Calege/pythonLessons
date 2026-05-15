#typeCasting-> e o processo de converter o valor de um tipo de dado para o outro

#typeCast explicita-> quando a conversao e feita pelo programador
nome="Miracle Calege"
idade=20
media=16.5
estudante=True

#para saber o tipo de dados de uma variavel usamos a funcao: type(variavel)

print(type(nome))# o output sera str(string)
print(type(idade))# o output sera int(integer)
print(type(media))# o output sera float(float)
print(type(estudante))# o output sera bool(boolean)


#float(variavel), int(variavel), str(variavel),bool(variavel): as funcoes convertem a variaveis para float,int,string e bool respectivamente
#bool(variavel)-> retorna True sempre sempre que a variavel for diferente de 0 ou ""
idade=float(idade)
media=int(media)
print(idade)#idade vai ser impressa com uma casa decimal
print(media)# a media vai ser impressa sem a casa decimal

#typeCast implicita
x=2
y=2.0

x=x/y
print(x)#x vai ser impresso com uma casa decimal automaticamente
