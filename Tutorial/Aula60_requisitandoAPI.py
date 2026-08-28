from urllib import response

#devemos importar o modulo request(geralmente temos que baixar)
import requests

#url

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    #estamos a seguir a estrutura do url do site pokeapi
    url=f"{base_url}/pokemon/{name}"
    response = requests.get(url)#retorna um objecto do tipo response com um status code(ex: 404 significa pagina nao enncontrada)
    if response.status_code == 200:
        pokemon_data=response.json()#vai ser exibido em forma de json
        return pokemon_data
    else:
        print(f"data not retrieved{response.status_code}")
pokemon_name="pikachu"#podemos colocar qualquer nome de um pokemon

pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name:{pokemon_info["name"]}")
    print(f"Id:{pokemon_info["id"]}")
    print(f"Height:{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")