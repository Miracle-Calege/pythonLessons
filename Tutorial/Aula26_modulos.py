"""
modulo-> um ficheiro contendo codigo que tu possa querer incluir no seu programa

para incluir um modulo usamos :import nomeModulo
"""


#print(help("modules")) lista os modulos disponiveis

#print(help("math")) podemos usar o help para listar as especificacoes de um modulo especifico

# import  math #importamos o modulo
# import math as m#importamos o modulo e dados um alias(um nickname, esse nickname sera usado para acessar elementos) ideal para casos onde o nome do modulo e longo
# from math import pi#para importar um item especifico do modulo(neste caso usamos o nome do elemento directamente)
#
# #Para acessar as propriedade e metodos do modulo usamos nome do modulo.elemento/metodo
# print(math.pi)
# print(m.pi)
# print(pi)


"""
criacao de um modulo:
1.Criar um arquivo.py com os metodos e variaveis desejadas
2.No ficheiro actual(que esta a trabalhar nele) importar o arquivo.py criado no ponto 1.

"""
import Modulo_Exemplo_aula26

print(Modulo_Exemplo_aula26.pi)

print(Modulo_Exemplo_aula26.quadrado(2))
