"""
Aulas:introducao,variaveis
"""
salario_hora=14800
horas_trabalhadas=168
desconto=9.14

salario_bruto=salario_hora*horas_trabalhadas
print(f"salario antes do desconto:{salario_bruto}")
salario_liquido=salario_bruto-salario_bruto*(desconto/100)
print(f"salario depois do desconto:{salario_liquido}")

