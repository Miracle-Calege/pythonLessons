"""
escopo de variavel-> onde uma variavel e visivel e acessavel
scope resolution-> (LEGB) Local-> Enclosed(metodos dentro de outro metodo)-> Global->Built-in(a ordem hierarquica e essa)

Local-> variavel declarada dentro de uma funcao(acessivel e visivel dentro da funcao)

"""
#ambas funcoes podem ter o mesmo nome porque sao locais,visiveis e acessaveis dentro do metodo

# def funcao():
#     a=1
#     print(a)
#
# def funcao2():
#     a=2
#     print(a)
#
  #global-> todos tem acesso, sao declaradas fora de um metodo
a=1
def funcao():
    print(a)


def funcao2():
    print(a)

funcao()
funcao2()

#built in-> variaveis de modulos

from Modulo_Exemplo_aula26 import pi
print(pi)