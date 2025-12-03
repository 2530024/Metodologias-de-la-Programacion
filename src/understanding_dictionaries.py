#Simple dictionary
alien_0 = {'color': 'green', 'points': 5}

#The simpliest dictionary
alien_1 = {'color': 'yellow'}

#Accessing values in a dictionary
print(alien_0['color'])
print(alien_1['color'])

#Empty
alien_2 = {}

#Modifying values in a dictionary
alien_2 = {'color': 'red'}
alien_2['color'] = 'blue'

#Adding new key values pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

##Dictionaty to store similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#Looping throgh all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for key in favorite_languages.keys():
    print(key.title())

for value in favorite_languages.values():
    print(value.title)

#Nesting dictionaries

##Listas de diccionarios
##Listas en diccionarios
##Diccionarios en diccionarios
"""
    Listas dentro de diccionarios
    un diccionario puede almacenar cualquier tipo de dato como valor
     
    Sintaxis:
    diccionario = {
    "clave": [valor1, valor2, valor3]
    }
    Ejemplo:
    estudiante = {
    "nombre": "Luis",
    "calificaciones": [9, 8, 10, 7]
}

print(estudiante["calificaciones"][2])   # Acceder al tercer elemento → 10
"""

"""
    Diccionarios dentro de diccionarios

    Sintaxis:
    diccionario = {
    "clave1": {
        "subclave1": valor,
        "subclave2": valor
    },
    "clave2": {
        "subclaveA": valor,
        "subclaveB": valor
    }
}
    Ejemplo:
    usuarios = {
    "user01": {
        "nombre": "Ana",
        "edad": 20
    },
    "user02": {
        "nombre": "Carlos",
        "edad": 25
    }
}
print(usuarios["user02"]["nombre"])  # Acceso a un valor interno → "Carlos"
"""

#Estudiar el metodo get() de los diccionarios