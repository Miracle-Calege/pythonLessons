#se quisermos ler um json devemos fazer este import
import json

#se quisermos ler um csv devemos fazer este import
import csv

#caminho do ficheiro
file_path="/home/miracle-calege/Documents/learningPython/Tutorial/output.csv"

#caso uma excepcao possa ocorrer
try:
#a funcao open vai acessar o caminho com o modo de leitura e retornará um ficheiro que chamaremos de file
    with open(file_path, "r") as file:
    #o conteudo a ser lido serao guardado na variável content
        #content=file.read() lendo um txt
        #content=json.load(file) lendo json
        content=csv.reader(file)
        for line in content:#lemos linha a linha
            print(line)

except FileNotFoundError:
    print("ficheiro nao encontrado")