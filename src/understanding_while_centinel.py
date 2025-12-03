"""
    Vamos a realizar un programa que sume numeros hasta que
    el usuario escriba la palabra "Salir"

    El programa tambien debe decirme cuantos numeros ingreso el usuario,
    cual fue el minimo y cual fue el maximo.

"""
cont = 0
suma = 0
number_min = None
number_max = None
while True:
    print("Ingresa la palabra 'salir' para terminar")
    user_input = input("Enter a number: ")
    if user_input == "salir":
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad no valida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        break
    cont += 1
    suma += quantity
    if number_min is None or number_min > quantity:
        number_min = quantity
    if number_max is None or number_max < quantity:
        number_max = quantity
print("SUM: ", suma)
print("Cont: ", cont)
print("Maximo: ", number_max)
print("Minimo: ", number_min)