"""
Funcoes lambdas-> sao pequenas funcoes anonimas para usar uma unica vez,recebam qualquer numero de argumentos
Sao bastante uteis com funcoes de ordem superior : map(),sort(),etc

sintaxe:

lambda parametros:expressao
"""

#Neste caso inicializamos a variavel dobro com o resultado .
#A funcao dobra o valor do x

dobro=lambda x:x*2

#passamos o argumento na variavel
print(dobro(5))

somar=lambda a,b:a+b

print(somar(2,3))

max=lambda x,y:x if x>y else y
min=lambda x,y:x if x<y else y

full_name=lambda nome, apelido:nome+" "+apelido

print(max(4,5))
print(min(4,5))
print(full_name("Miracle","Calege"))

