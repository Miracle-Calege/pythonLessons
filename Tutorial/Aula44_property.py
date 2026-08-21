"""
@property-> é um decorator usado para definir um metodo como propriedade(permitindo que seja acessado como um atributo)

@property antes do metodos para indicar

usamos a keyword "del" para deletar os metodos

NB: Os getters só levam @property
    Os setter @atributo.setter
    Os deleter @atributo.deleter

"""


class Rectangle:

    def __init__(self, largura, altura):
        self._largura = largura#o "_" antes dos atributos torna os atributos protected
        self._altura = altura

    @property
    def width(self):
        return f"{self._largura:.1f}cm"

    @property
    def height(self):
        return f"{self._altura:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._largura = new_width
        else:
            print("O largura deve ser maior que 0")

    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._altura = new_height
        else:
            print("O altura deve ser maior que 0")


    @width.deleter
    def width(self):
        del self._largura
        print("O largura foi apagada")

    @height.deleter
    def height(self):
        del self._altura
        print("O altura foi apagada")


rectangle=Rectangle(3,4)

#setters
rectangle.width=5
rectangle.height=7



print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height