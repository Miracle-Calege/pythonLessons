"""
Aulas:entradaDados,typecasting,variaveis,introducao
"""
segundos=float(input("Insira a quantidade de segundos:"))


segundo=segundos%60

quociente=segundos/60

minutos=quociente%60

horas=quociente/60

print(f"{horas}:{minutos}:{segundo}")