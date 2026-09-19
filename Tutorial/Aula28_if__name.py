"""
if __name__ == '__main__':->

__name__-> é uma variável que sempre que corremos o script será incializado por __main__

Quando este ficheiro é executado como módulo em outro ficheiro o __name__ passa a ser inicializado pelo nome do ficheiro.NB:Quando importamos um ficheiro esse ficheiro é automaticamente executado, por isso no ficheiro2 o ficheiro "if_name" é executado primeiro.

É ideal para evitarmos que o código que um ficheiro esteja a ser executado no nosso ficheiro actual simplesmente porque fizemos import do ficheiro/modulo

"""
print(f'nome:{__name__}')

if __name__ == '__main__':
    print('__name__equals__main__')#Logo como o este ficheiro foi importado no ficheiro2 está instruçao nao será executada porque o __name__=Aula28_if__name