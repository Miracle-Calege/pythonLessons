


"""
os metodos len(),in e clear(0 tambem funcionam para set.

Metodos:
add(elemento)-> adiciona o elemento
remove(elemento)->remove elemento
pop()-> remove o primeiro elemento na estrutura


"""

frutas={"maca","laranja","uva","manga"}


print(frutas)#se formos a repetir varias vezes a impressao notaremos que a ordem dos elementos e alterada

# print(help(frutas))
# print(dir(frutas))

frutas.add("ananas")
print(frutas)
frutas.remove("uva")
print(frutas)
frutas.add("ananas")#esta accao nao tera efeito porque o elemento ja faz parte da estrutura
print(frutas)

