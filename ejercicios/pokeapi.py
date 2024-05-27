#!/usr/bin/env python3

import requests


def pokeapi():
    pokemon = input("Dime el numero o nombre del pokedex: ")
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        #Obteniendo la respuesta de la solicitud GET y guardándola en formato JSON
        datos_pokemon = response.json()
        
        nombre_pokemon, tipos = dato_pokemon(datos_pokemon)
        
        print(f"Nombre: {nombre_pokemon} y su(s) tipo(s) son: {tipos}")
    else:
        print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')


def dato_pokemon(datos_pokemon):
        nombre_pokemon = datos_pokemon["name"].capitalize()
        tipo_pokemon = datos_pokemon["types"]
        tipos = []
        for tipo in tipo_pokemon:
            tipos.append(tipo["type"]["name"].capitalize())
            
        # join combina elementos de un iterable en una cadena con un separador específico.
        tipos = " y ".join(tipos)
        return nombre_pokemon, tipos
    
     

if __name__ == "__main__":
    pokeapi()