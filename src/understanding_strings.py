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

#Styntax error con strings
message = "Una fortaleza de Python es su comunidad"
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message)

#Concatenacion con f-strings
famous_person = "Charly Mercury"
quote = "Python is love"

#Concatenacion convensional
message = famous_person + "una vez dijo " + quote
print(message)

#Concatenacion con fstrings
"""
    () - se llaman parentesiss
    {} - llaves
    [] - corchetes
"""
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

#Actividad
"""
    1) Elige un personaje famoso e igualalo a una variable de tipo string
    2) Elige un personaje que haya dicho e iguala a una variable de tipo string
    3) Genera un mensaje con las dos variablwes utilizando f-string
    4) Imprime el mensaje
"""
famous_person = "Mario Benedetti"
frase = "No quiero otra compañia que tu risa"
message_f_string = f"{famous_person} una vez dijo {frase}"
print(message_f_string)