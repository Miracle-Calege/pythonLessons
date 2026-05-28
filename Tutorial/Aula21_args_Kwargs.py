"""
*args-> permite passar multiplos argumentos sem key(tuple)
*args-> nos permite que a funcao suporte multiplos argumentos/parametros, onde os elementos sao guardados numa tuple
**kwargs-> permite passar multiplos keyword argument usando(dictionary)
**kwargs->nos permite que a funcao suporte multiplos argumentos/parametros, onde os elementos sao guardados num dictionary
do tipo keyword
"""


def soma(*args):#podemos usar outro nome alem de args
 #print(type(args)) vai exibir o nome estrutura que guarda os elementos(tuple)
        total=0
        for arg in args:
            total += arg
        return total

print(soma(1,2,3,4) )

def endereco(**kwargs):#podemos usar outro nome alem de kwargs
    #print(type(kwargs)) usa um dicionario para guardar os dados
    for key, value in kwargs.items():
        print(f"{key}: {value}")

endereco(rua="1234",apt="100",cidade="Maputo",estado="MI",zip="5420")
