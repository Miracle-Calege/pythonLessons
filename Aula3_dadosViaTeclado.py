
#para receber um dado via teclado usamos a funcao input("mensagem")
#todos dados recebidos via teclados sao considerados string

nome=input("Insira o seu nome:")# a variavel nome vai guardar o input
idade=input("Insira sua idade:")#opcao: idade=int(input("Insira sua idade:"))
idade=int(idade)
idade=idade+1# essa operacao nao seria possivel se nao tivessemos convertido a idade para int
print(f"O teu nome e: {nome}")
print(f"Idade: {idade}")
