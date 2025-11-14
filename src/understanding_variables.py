message = "This is my first variable!"
another_message = "Hello, World!"

print(message)
print(another_message)

print(message, another_message, message, another_message)
print(another_message, message)
"""
Los nombres de las variables en Python deben nombrarse solo con:

    - Las letras, numeros y guion bajos (espacios)
    -deben comenzar con una letra o con guieno bajo, pero NO con numero:
        ejemplo correcto : mensaje_1 ( :) )
        ejemplo incorrecto : 1_mensaje ( :( )
    -no utilizar palabras reservadas de Python para nombrar variables o archivos
    -no utilizar palabras reservadas de Python para nombrar variables o archivos
    -nombres cortos ser cortos, pero descriptivos
    -ser en ingles
    -nombres de las variables en minusculas,
"""

charly_message = "Charly es un buen profe"
print (charly_message)
print (charly_message)

"""
Traceback: Es un registro de donde el interprete 
        tuvo problemas para ejecutar el codigo

    Ejemplo 
    Traceback (most recent call last):
        File "C:/Users/selen/Proyectos/Metodologias-de-la-Programacion/src/understanding_variables.py", line 25, in <module>
        print(charly_mesage)
    NameError: name 'charly_mesage' is not defined

    NameError: Significa que la variable no tiene valor de una variable asignada
"""

##Variables de tipo boolano
game_active = True
can_edit = False
