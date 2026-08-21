"""
Para trabalhar com ficheiros vamos importar o modulo os, este modulo permite que o python interaja com o sistema operativo
"""

import os


caminho="teste.txt"# caminho relativo


if os.path.exists(caminho):#verifica se o caminho existe
    print(f"O caminho {caminho} foi encontrado")
    if os.path.isfile(caminho):
         print("É um ficheiro")
    elif os.path.isdir(caminho):
        print("É um directório")

else:
    print(f"O caminho nao foi encontrado")
