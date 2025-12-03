"""
    Vamos a realizar un programa que 
    defina un PIN como contraseña

    Despues vamos a darle 3 intentos al usuario
    para escribir el pin 

    Si el usuario escuribe correctamente el
    pin, el programa debe mostrar un mensaje de 
    Acceso Permitido

    Si el usaurio se equivoca, el programa debe decirle
    cuantos intentos le quedan y el caso de que no le queden intentos
    el mensaje debe decir Acceso Denegado
    excediste tus intentos
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    user_pin = input("Escribe tu PIN: ")
    if user_pin == CORRECT_PIN:
        print("Acceso Permitido")
        break
    else:
        intents += 1
        remaining_attempts = MAX_ATTEMPTS - intents
        if remaining_attempts > 0:
            print(f"PIN incorrecto. Te quedan {remaining_attempts} intentos.")
        else:
            print("Acceso Denegado. Excediste tus intentos.")