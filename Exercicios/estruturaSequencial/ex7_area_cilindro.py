
"""
Aulas:introducao,entradaDados,Math,typecasting
"""
import math


raio=float(input("Insira o raio:"))
altura=float(input("Insira altura:"))

volume=math.pi*raio**2*altura
area=2*math.pi*(raio**2+raio*altura)

print(f"Volume:{volume} e Area:{area}")