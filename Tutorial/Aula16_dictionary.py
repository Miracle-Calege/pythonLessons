"""
Dictionary- uma estrura de pares  {chave:valor}  ordenada e mutaveis.Nao aceita valores duplicados
get(chave)->retorna o elemento da chave
update({chave:valor})-> insere um novo par ou actualizar um existente
pop(chave)-> remove o elemento associado a chave
popItem()-> remove o ultimo elemento
clear()-> remove todos elementos
keys()-> retornas as chaves
values()-> retorna os valores das chaves
items()->retorna uma list 2D de tuples sendo cada tupla um par(chave,valor)

"""

capitais={"MOZ":"Maputo",
          "RSA":"Pretoria",
          "Uganda":"Kampala",
          "Quenia":"Nairobi"}



print(capitais.get("MOZ"))#retorna o valor associado("Maputo"), caso a a chave nao exista retornara none
capitais.update({"Etiopia":"Dododma"})
capitais.update({"MOZ":"Lourenco Marques"})
print(capitais)
capitais.pop("Etiopia")
print(capitais)
capitais.popitem()
print(capitais)
# capitais.clear()
# print(capitais)
print(capitais.keys())
print(capitais.values())
print(capitais.items())


