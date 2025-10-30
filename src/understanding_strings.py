"""
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples
    '' o dobles comillas "" es considerado un string

        "Esto es un string"
        'Esto tambien es un string'

        'Le dije a un amigo, "¡Python es mi lenguaje favorito!"'
        "El lenguaje Python lleva el nombre por Monty Python,
        no por la serpiente"

"""

name = "clase de programacion"
print(name)
print(name.title())

"""

Un metodo es una accion que python puede realizar
en un fragmaneto de datos o sobre una variable.

El punto . despues de una variable seguida 
del metodo title() dice que se tiene que ejecutar
el metodo title() de la variable name.

Tod0s los metodos van seguidos de parentesis 
porque en ocuasiones necesitan informacion adicional
para funcionar, lo cual iria dentro de los parentesis.
En esta ocasion el metodo .title() no requiere
informacion adicional para ejecutarse
"""

print(name.upper())
print(name.lower())

#Concatenacion de Strings
print("CONCATENACION DE STRINGS")
first_name = "charly "
last_name = "mercury"
full_name = first_name + last_name
print(full_name)

print("Hola, " + full_name.title() + "!")