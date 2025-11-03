#Numbers

"""
    Integers - Enteros

    Son numeros sin punto decimal
    -infty, ... -2, -1, 0, 1, 2, ..., infty

    Ejemplo:
        Tipado dinamico
        age = 33

        Los podemos sumar (+), restar(-), multiplicar (*) y dividir (/)
        Potencias (**2, **3)

        Modulo (Dividendo%Divisor)
"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2
power = number_1 ^ number_2

print("suma: " , suma)
print("resta :" , resta)
print("multiplicacion: ", multiplicacion)
print("division: ",  division)
print("modulo: ", modulo)
print("power: ", power)

print("La suma es del tipo ", type(suma))
print("La resta es del tipo ", type(resta))
print("La multiplicacion es del tipo ", type(multiplicacion))
print("La division es del tipo ", type(division))
print("La modulo es del tipo ", type(modulo))
print("La power es del tipo ", type(power))

#Floats
"""
    Floats - Flotantes

    Son numeros con punto decimal
    van desde -infty infty

    Ejemplo:

        Tipado dinamico
        age = 25.5

        Los podemos sumar (+), restar(-), multiplicar (*) y dividir (/)
        Potencias (**2, **3)

        Modulo (Dividendo%Divisor)
"""

print(0.1+0.2)
print(0.99-0.35)
print(0.4*0.5)
print(0.6/0.2)

#Imprimir la edad de alguien
age = 32
messge = "Charly tiene " + str(age) + " años."

"""
    Type Error: Python no puede reconocer el tipo de informacion que se esta utilizando.

    Para convertir a string utilizo: str()
"""
message_f = f"Charly tiene {age} años."

print(message_f)