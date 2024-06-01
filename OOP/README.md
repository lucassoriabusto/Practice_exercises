# Introducción a la Programación Orientada a Objetos (POO) en Python

La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza "objetos" y "clases" para organizar el código.

## Conceptos Clave

1. **Clases y Objetos:**
   - **Clase:** Es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
   - **Objeto:** Es una instancia de una clase. Cada objeto puede tener diferentes valores para los atributos definidos en la clase.

2. **Atributos y Métodos:**
   - **Atributo:** Es una variable que pertenece a una clase o a un objeto.
   - **Método:** Es una función que pertenece a una clase. Los métodos pueden modificar los atributos de un objeto o realizar operaciones con ellos.

3. **Encapsulamiento:**
   - Es el principio de ocultar los detalles internos de una clase y exponer solo lo necesario. Se puede controlar el acceso a los atributos y métodos usando modificadores de acceso.

4. **Herencia:**
   - Permite crear nuevas clases basadas en clases existentes. La nueva clase (subclase) hereda los atributos y métodos de la clase base (superclase), permitiendo reutilizar el código.

5. **Polimorfismo:**
   - Permite tratar objetos de diferentes clases de manera uniforme a través de una interfaz común. Esto significa que, aunque los objetos sean de diferentes clases, pueden ser tratados de la misma manera si comparten un método con el mismo nombre. Los métodos pueden ser redefinidos en las subclases, permitiendo que cada clase implemente su propia versión del método.
--------------------------------------------------------

## Ejercicios Básicos

### Ejercicio 1: Crear una Clase y Objetos
Crea una clase llamada `Persona` con los atributos `nombre` y `edad`, y un método que imprima los detalles de la persona.

### Ejercicio 2: Herencia
Crea una clase `Estudiante` que herede de la clase `Persona` e incluya un atributo `grado` y un método que imprima los detalles del estudiante.

### Ejercicio 3: Encapsulamiento
Modifica la clase `Persona` para que el atributo `edad` sea privado y proporciona métodos para obtener y modificar su valor de manera controlada.

### Ejercicio 4: Polimorfismo
Crea una función que acepte cualquier objeto que tenga un método `mostrar_detalles` y lo llame.
