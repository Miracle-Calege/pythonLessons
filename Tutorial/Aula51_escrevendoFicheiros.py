import csv
import json

from Tutorial.Aula50_fileDetection import caminho

txt_data="Eu gosto de lasanha"


caminho="output.csv"

funcionario={
    "Nome":"Miracle Calege",
    "idade":20,
    "ocupacao":"estudante"
}

funcionario2=[["Nome","idade","ocupacao"],
              ["Calege Miracle",20,"Estudante"],
              ["Siswe Calege",20,"PCA"]]

# a funcao open(caminhoFicheiro,"mode") as nomeObjectoFicheiro(geralmente é file). essa funcao abre o ficheiro. with trata do fechamento do ficheiro,mode: r-ler,w-sobrescreve sobre os dados que já estavam no ficheiro(apaga os dados anteriores),x->escrevemos sobre um ficheiro que ainda nao existe,a->novos dados serao anexados aos dados anteriores
with open(caminho,"w") as arquivo:
    #arquivo.write(txt_data)#usamos o metodo write() para escrever sobre o ficheiro
    #json.dump(funcionario,arquivo,indent=4)#este metodo transforma o dicionario em um ficheiro json,indent nos permite determinar a identacao do conteudo.
    writer=csv.writer(arquivo)#writer é um objecto que nos permite acessar a este metodos
    for row in funcionario2:
        writer.writerow(row)# escreve o conteudo nas linhas do ficheiro


    print(f"{caminho} foi criado com sucesso")


