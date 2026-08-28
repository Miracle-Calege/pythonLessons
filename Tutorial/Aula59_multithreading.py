"""
multithreading->usado para executar múltiplas tarefas simultaneamente/concorrentemente
ideal para funcoes de I/O ler ficheiros ou buscar dados de APIs.
"""

#importamos o modulo threading
import threading

#estamos a usar para simular um tempo
import time

def walk_dog(first,last):
    time.sleep(8)#executa depois de 8 segundos.
    print(f"you finish Walking dog{first} {last}")


def take_out_trash():
    time.sleep(2)
    print("you finish take out trash")

def get_mail():
    time.sleep(4)
    print("you finish getting mail")
#
# walk_dog()
# take_out_trash()
# get_mail()

#criamos uma thread e determinado qual metodo executar
chore1=threading.Thread(target=walk_dog,args=("puff","doo"))#se o metodo tiver um argumentos usamos args, e colocamos "," para indicar que só e um elemento
chore1.start()#iniciamos a thread

chore2=threading.Thread(target=take_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()

#determina que as threads terminem para executar o resto do programa(imprimir a linha 44)
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")