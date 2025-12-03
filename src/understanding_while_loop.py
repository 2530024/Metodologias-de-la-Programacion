"""

    Utilizamos el while loop para ejecutar un bloque de
    codigo mientras una condicion sea verdadera.
    Estructura basica del while loop en Python:
    while condicion:
        #Bloque de codigo a ejecutar
"""

#Ejemplo basico de un while loop
#Verificar si un numero esta en un
#rango especifico (10 y 20)

while True:
    try:
        numero = int(input("Ingresa un numero ENTERO entre 10 y 20:"))
        if 10 <= numero <= 20:
            print("Gracias! Has ingresado un numero valido.")
            break
        else:
            print("Numero invalido. Intenta de nuevo.")
    except ValueError:
        print("Entrada invalida. Por favor ingresa un numero entero.")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break