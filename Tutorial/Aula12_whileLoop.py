#while loop->executa algumas instrucoes enquanto a condicao for verdadeira

"""
Estrutura:
while condicao:
instrucao

"""

"""
nome=input("Insira o seu nome: ")

while nome == "":
    print("Nao inseriste o teu nome: ")
    nome = input("Insira o seu nome: ")
print(f"ola{nome}")#esta linha deve estar alinhada com o while para indicar que nao faz parte do loop
"""

"""

idade=int(input("Insira sua idade: "))
while idade < 0:
    print("Idade nao pode ser menor que zero")
    idade = int(input("Insira sua idade: "))
print(f"Tu tens {idade} anos")
"""
comida=input("Insira sua comida: ")
while  comida != 'q':
    print(comida)
    comida = input("Insira sua comida: ")
print(f"Pressionou q")