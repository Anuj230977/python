import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
#trying input
pokemon_name = input("Enter Pokémon name: ")
#pokemon_name = "Dolliv"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    #print(f"Name: {pokemon_info["name"].capitalize()}")
    #print(f"Id: {pokemon_info["id"]}")
    #print(f"Height: {pokemon_info["height"]}")
    #print(f"Weight: {pokemon_info["weight"]}")
    #trying to get output in float decimal format.
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height'] / 10:.2f} m")
    print(f"Weight: {pokemon_info['weight'] / 10:.2f} kg")
    #sucessfully printed the pokemon info
else:
    print("No Pokémon data found.")    