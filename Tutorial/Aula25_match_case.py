"""
Match-case -> e uma alternativa para o uso de varios if's.Assemelha-se a switch em outra linguagens

Estrutura:

def funcao(variavel_a_ser_analisada):
match variavel_a_ser_analisada:

case x:
    instrucao

  .
  .
  .
  .
  .

"""

def semana(dia):
    match dia:

        case "Domingo":
            return "Domingo"
        case "Segunda":
            return "Segunda"
        case "Terca":
            return "Terca"
        case "Quarta":
            return "Quarta"
        case "Quinta":
            return "Quinta"
        case "Sexta":
            return "Sexta"
        case "Sabado":
            return "Sabado"

        case _: #usado caso a entrada nao corresponda a nenhuma das opcoes
            return "Invalido"

print(semana("Domingo"))


def weekend(dia):
    match dia:
        case "Sabado"| "Domingo": #|-> ou
            return True

        case "Ssegunda" | "Terca"| "Quarta"| "Quinta"|"Sexta":
            return False

print(weekend("Domingo"))