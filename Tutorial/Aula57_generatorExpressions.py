"""
Generator expressions-> é uma forma mais curta e compacta de criar generator sem  usar uma funcai. Similar a listcomprehension.

Estrutura:

objecto=(instrucao  iteraçao)

"""

generator = (num ** 2 for num in range(10))
for num in generator:
    print(num)