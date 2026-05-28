"""
Membership operator-> e usado para testar se um valor ou variavel esta numa sequencia(string,list,tuple,set ou dictionary)
in-> verifica se esta
not if-> verifica se nao esta
"""

palavra="maca"

letra=input("Adivinhe a letra : ")

# if letra in palavra:
#     print(f"esta {letra}")
# else:
#     print(f"nao esta {letra}")

if letra not  in palavra:
    print(f"nao esta {letra}")
else:
    print(f"esta {letra}")