#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crea una clase Estudiante que herede de la clase Persona       
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}")
        
persona1 = Estudiante("Lucas", 28, "1°")

persona1.mostrar_detalles()
        
