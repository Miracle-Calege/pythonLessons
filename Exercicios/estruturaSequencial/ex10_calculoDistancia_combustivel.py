"""
Aulas:entradaDados,typecasting
"""
tempo=int(input("Insira a quantidade de horas viajadas:"))
velocidade=int(input("Insira a velocidade media viajada"))

distancia=tempo*velocidade

litros=distancia/12

print(f"Para {distancia}km foram gastos {litros} litros de combustivel")