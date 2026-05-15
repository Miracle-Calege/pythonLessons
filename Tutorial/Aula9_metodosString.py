"""
len(variavel)-> retorna o tamanho da string
Os metodos abaixos sao acessados:
variavel.metodo()

find(valor)/rFind(valor)-> retorna a posicao da primeira /ultima ocorrencia respectivamente do argumento.Retorna -1 se nao tiver nenhma ocorrencia do argumento fornecido
capitalize()-> coloca o primeiro caracter em maiusculo
upper()->coloca o todos os  caracteres em maiusculo
lower()->coloca o todos os  caracteres em minusculo
isDigit()-> retorna um valor logico(bool) para verificar se a string e composta por digitos
isalpha()->retorna um valor logico(bool) para verificar se a string e composta por caracter alfabetos(se a palavra tiver espaco vai retornar false)
count(valor)-> conta quantas occorencia desse valor existem
replace(valor,substituto)-> substitui o valor por um outro
help(tipo de dados)-> retorna um guia do usuario de algumas funcoes
"""


# print(help(str))

username=input("Digite o seu username: ")

if len(username)>12:
    print("O seu username nao pode ter mais de 12 caracteres")
elif not username.find(" ")==-1:# se o retorno for diferente de -1
    print("seu username nao pode ter espacos em branco")
elif not username.isalpha():
    print("seu username nao pode ter digitos")
else:
    print(f"Bem vindo {username}")