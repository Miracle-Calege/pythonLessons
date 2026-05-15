import math


#operadores:+(adicao),-(subtraccao),*(multiplicacao),/(divisao),**(potencia),%(modulo),==(igualdade)
#operadores aumentados-> sao usados quando queremos fazer operacoes sobre uma variavel sendo a variavel parte da operacoes
#inves de ser: variavel=variavel+1.Como utilizar: variavel operador=valor.ex:variavel+=1

# amigos=5
#
# amigos=amigos+1#amigos+=1
# print(amigos)
# amigos=amigos-2#amigos-=2
# print(amigos)
# amigos=amigos*3#amigos*=3
# print(amigos)
# amigos=amigos/2#amigos/=2
# print(amigos)
# amigos=amigos**3#amigos**=3
# print(amigos)
# amigos=amigos%2#amigos%=2
# print(amigos)

#***********************************************************************************
#usando funcoes matematicas
#round(variavel)-> arredonda o valor
#abs(variavel)-> retorna o valor absoluto da variavel
#pow(base,expoente)->faz uma potencia
#max(valor1,valor2,...)-> retorna o maior valor
#min(valor1,valor2,...)-> retorna o menor valor



# x=3.14
# y=-4
# z=5
#
# resultado=round(x)
# print(resultado)
# print(abs(y))
# print(pow(y,z))
# print(max(x,y,z))
# print(min(x,y,z))

#*******************************************************************************8
#Para usar as funcoes abaixo devemos importa o modulo Math
#para usar elementos deste modulo :math.elemento/funcao
#sqrt(valor)-> retorna a raiz quadrado desse valor
#ceil(valor)->arredonda um valor para cima
#floor(valor)->arredonda um valor para baixo

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.1))
print(math.floor(9.1))
