"""
    Functions

    Las funciones son bloques de codigo diseñados
    para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ha definido 
    en un a funcion, tenemos que llamar el nombre de la
    funcion responsable de esto.

    Definicion de una funcion (Syntax)

    def nombre_de_la_funcion(parametros):
        Acciones
"""
"""
def saludar(nombre):
    print(f"Hola {nombre}, bienvenido a Python")

def sumar(a, b):
    return a + b

nombre = input("Escribe tu nombre:")
saludar(nombre)

a = float(input("Escribe el primer numero a sumar: "))
b = float(input("Escribe el segundo numero a sumar: "))
resultado = sumar(a, b)
print("La suma de a y b es: ", resultado)
"""

"""
    Vamos ha realizar un programa que genere
    el nombre completo de una persona

    Vamos a pasarle primet nombre, el segundo 
    y el apelldio
    
    La funcion debe generar el nombre completo
    y regresarlo
"""

def create_full_name(first_name, last_name, middle_name="",):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

user_first_name = input("Enter your first name: ").strip().lower()
user_middle_name = input("Enter your middle name: ").strip().lower()
user_last_name = input("Enter your last name: ").strip().lower()
full_name = create_full_name(user_first_name, user_last_name, user_middle_name)
print("Your full name is: ", full_name)

#Argumentos Clave -> Keyword Arguments
full_name_key = create_full_name(
    first_name=user_first_name,
    last_name=user_last_name,
    middle_name=user_middle_name)

## Parametros opcionales
profe_falso = create_full_name(user_first_name, user_last_name, user_middle_name)
print(profe_falso)


##Temas para esdudiar a futuro tarea para 2 años
# funciones: args, kwargs
# manejo de datos: abrir archivos, csv, .json, .yml, .txt, 
# Argumentos por linea de comando - sys
# cli - command line interface
# generadores, iteradores, yield
# Testing -> 