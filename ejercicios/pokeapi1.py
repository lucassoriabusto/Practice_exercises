#!/usr/bin/env python3

import requests

def obtener_nombre_tipo_pokemon(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        nombre_pokemon = datos_pokemon['species']['name'].capitalize()
        tipos_pokemon = [tipo['type']['name'].capitalize() for tipo in datos_pokemon['types']]
        return nombre_pokemon, tipos_pokemon
    else:
        print("Error al obtener los datos del Pokémon.")
        return None, None

def mostrar_tipos_pokemon():
    numero_pokedex = input("Ingresa el número de Pokédex del Pokémon: ")
    nombre_pokemon, tipos_pokemon = obtener_nombre_tipo_pokemon(numero_pokedex)
    if nombre_pokemon and tipos_pokemon:
        print(f"El Pokémon N°{numero_pokedex} es {nombre_pokemon} y sus tipos son: {', '.join(tipos_pokemon)}")
    else:
        print("Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_tipos_pokemon()
