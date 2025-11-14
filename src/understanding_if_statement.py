cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

# El condicional es el corazon de un if
car = 'bmw'
print(car == 'bmw') #True

#Condicional false
car = 'Audi'
print(car == 'audi')

# Posible solucion a entradas del usuario
car = 'Audi'
print(car.lower() == 'audi') #True

#Operadores relacionales != para determinar desigualdad
requested_topping = 'mushroom'
if requested_topping != 'anchovies': #True
    print("Hold the anchovies!")

#Comparaciones numericas
age = 18 #Entero
print(age == 18)

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta otra vez")

age = 17
print(age < 21) #True
print(age <= 21)#True
print(age > 21)#False
print(age >= 21)#False

#Multiples condiciones
age_0 = 22
age_1 = 18

#Operacion and
print(age_0 >= 21 and age_1 >= 21) #False
print(age_0 >= 21 and age_1 >= 18) #True

#Operacion or
print(age_0 >= 21 or age_1 >= 21) #True
print(age_0 >= 23 and age_1 >= 21) #True

"""
    Para preguntarnos si un valor especifico esta en una lista,
    podemos utilizar el siguiente comparador:
"""

motorcycles = ['mortalica', 'honda', 'vento', 'yamaha']
moto_charly_wants = 'italica'
print(moto_charly_wants in motorcycles) #False
print("honda" in motorcycles)

"""
    Para preguntarnos si un valor especifico NO esta en una lista,
    podemos utilizar el siguiente comparador:

    value not in list
"""
banned_students = ['jorge', 'carlos', 'moyra', 'gus', 'hots']
user = 'mauro'
print(user not in banned_students) # True
print('jorge' not in banned_students) # False

"""
    if statement
        syntax
    ii condition:
        do something

    if condition:
        do something
    else:
        do something else
"""

age = input("\n ¿Dime cual es tu edad?")
print(age)

if age >= 18:
    print("Eres mayor de edad, vota")

else:
    print("Eres menor de edad, no votes")