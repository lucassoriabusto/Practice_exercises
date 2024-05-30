#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Atributo 
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad < 0:
            print("Edad no válida")
        else:
            self.__edad = edad
            
    def mostrar_detalles(self):
        print(f'Nombre: {self.nombre}, Edad: {self.__edad}')
        
persona1 = Persona("Lucas", 28)

persona1.mostrar_detalles()

persona1.set_edad(29)
print(persona1.get_edad())