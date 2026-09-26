"""
Aulas:funcoes,variaveis,introducao
"""


salario_minimo=float(input("Insira o salario minimo:"))
quantidade_quilowatts=float(input("Insira a quantidade quilowatss:"))

def valor_quilowatts(salario_minimo):
    return (1/7*salario_minimo)/100

def valor_a_pagar(quantidade_qilowatts,salario_minimo):
    return (quantidade_qilowatts*1/7*salario_minimo)/100

def valor_a_pagar_com_desconto():
    return valor_a_pagar(quantidade_quilowatts,salario_minimo)-valor_a_pagar(quantidade_quilowatts,salario_minimo)*0.1

print(f"Valor em meticais por quilowatt:{valor_quilowatts(salario_minimo)} mzn")
print(f"Valor em meticais por pagar:{valor_a_pagar(quantidade_quilowatts,salario_minimo)} mzn")
print(f"Valor em meticais com desconto:{valor_a_pagar_com_desconto()} mzn")