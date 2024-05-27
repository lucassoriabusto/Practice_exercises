#!/usr/bin/env python3

import requests
import random

def obtener_nombre_pokemon(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        nombre_pokemon = datos_pokemon['species']['name']
        return nombre_pokemon.capitalize()  # Devuelve el nombre del Pokémon con la primera letra en mayúscula
    else:
        print("Error al obtener los datos del Pokémon.")
        return None

def pokimons():
    numero = random.randint(1, 151)
    nombre_pokemon = obtener_nombre_pokemon(numero)
    if nombre_pokemon:
        while True:
            respuesta = input(f"¿Qué Pokémon es el N°{numero}?:  ")
            if respuesta.lower() == nombre_pokemon.lower():
                print(f"¡Correcto! ¡Es {nombre_pokemon}!")
                break
            else:
                print("Incorrecto. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    pokimons()
