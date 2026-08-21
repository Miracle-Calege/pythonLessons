"""
Zip()-> combine varias estruturas de dados, ideal quando queremos iterar sobre todas simultaneamente
"""

nomes=["Spongebob","Patrick","Squidward"]

idades=[30,35,50]

data=tuple(zip(nomes,idades)) #combinamos as estruturas e convertemos em tuplas

#print(data)

for nome,idade in data:
    print(f"{nome} tem {idade} anos de idade")