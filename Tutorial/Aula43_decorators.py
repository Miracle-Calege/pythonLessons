"""
Decorator-> é uma funcao que estende o comportamento de uma outra funcao. Passa a funcao base como argumento

NB:Podemos ter mais de um decorator na funcao base
"""

def add_sprinkle(func):#nosso decorator. func referencia a funcao get_ice_cream
    def wrapper():#nossa funcao interna
        print("You add sprinkles!")# essa linha agora também sera executada e aparecerá antes do "Here is your ice cream!"
        func()
    return wrapper


@add_sprinkle #devemos adicionar o nome do decorator em cima da funcao base
def get_ice_cream(): #funcao base
    print("Here is your ice cream!")


get_ice_cream()