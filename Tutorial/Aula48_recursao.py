"""
Recursao-> é uma funcao de chama a ela mesma.
"""


def andar(passos):
    if passos==0:
        return
    andar(passos-1)
    print(f"Passo #{passos}")

andar(100)