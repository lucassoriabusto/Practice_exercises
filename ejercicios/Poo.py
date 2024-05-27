#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_detalles(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Crear objetos de la clase Persona
persona1 = Persona('Alice', 30)
persona2 = Persona('Bob', 25)

# Mostrar detalles de las personas
persona1.mostrar_detalles()
persona2.mostrar_detalles()
