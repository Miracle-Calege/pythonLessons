"""
Aulas:entradaDados,introducao,modulo,Math,typecasting
"""
import  ex8_modulo as op

base=float(input("Insira o valor da base:"))
altura=float(input("Insira o valor da altura:"))

print(f"Area:{op.areaRectangulo(base,altura)}")
print(f"Perimetro:{op.perimetro(base,altura)}")
print(f"Diagonal:{op.diagonal(base,altura)}")