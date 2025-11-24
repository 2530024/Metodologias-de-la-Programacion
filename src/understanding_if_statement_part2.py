"""
    Vamos a realizar un programa que pregunte
    al usuario por su edad y muestre un mensaje
    diferente segun el rango de edad en el que 
    se encuentre:
"""
op = 1
while op == 1:
    try:
        age = int(input("Por favor, Ingrese su edad: "))
        if age >= 18:
            print("Eres mayor de edad")
        elif age <18:
            print("Usted es carcel")
        else: 
            print("¿Esta usted vivo?")
        op = int(input("Quieres continuar? 1)Si 2)No  :"))
    except:
        print("Tuviste un error")
    
age = 0
try:
    age = int(input("Por favor, introduce tu edad:"))
except:
    age = -1
    print("Tuviste un error, ingresaste un caracter no valido")
if age > 100:
    print("Tienes mas de un siglo de vida.")
elif age >= 18 and age <=100:
    print("Eres mayor de edad")
elif age < 18 and age >= 0:
    print("Eres menor de edad")
else:
    print("Edad no valida")
"""
    Hacer un programa que pregunte la edad de una persona y respona lo siguiente
        -SI la edad es menor e igual a 4 entonces la entrada es gratuita
        -Si la edad es menor e igual a 18m, pero mayor que 4
        entonces la entrada cuesta $200
        -Si la edad es mayor que 18, entonces la entrada cuesta $400

"""
#Tarea
try:
    age = int(input("Por Favor, Ingrese su edad:"))
    if age <= 4:
        print("La entrada es gratuita")
    elif age <= 18 and age > 4:
        print("La entrada cuesta $200")
    elif age > 18:
        print("La entrada cuesta $400")
    else:
        print("Error")
except:
    print("Tuviste un error")    

#Multiple
guisos = ["desgebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Si hay")
else:
    print("No hay")
if "tamales" in guisos:
    print("Si hay")
else:
    print("No hay")
if "salsa verde" in guisos:
    print("Si hay")
else:
    print("No hay")