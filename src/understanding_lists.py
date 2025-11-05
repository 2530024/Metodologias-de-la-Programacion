# LISTAS
# Una lista es una coleccion de elementos en un orden particular.
# Se puede crear una lista colocando los elementos entre corchetes [] y separando los elementos con comas.
fruits = ["manzana", "banana", "cereza", "durazno"]
print(fruits) #Salida: ['manzana', 'banana', 'cereza', 'durazno']

# Acceder a elementos de una lista
print(fruits[0].upper()) #Salida: manzana
print(fruits[1]) #Salida: Banana
print(fruits[2].title()) #Salida: cereza
print(fruits[3].find("z")) 
# print(fruits[4]) # Esto generaria un error de indice fuera de rango

#Acceder al ultimo elemento de una lista
print(fruits[-1]) #Salida: durazno
print(fruits[-2]) #Salida: cereza
print(fruits[-3]) #Salida: banana

my_favorite_fruit = fruits[2].title()
message = f'Mi fruta favorita es la {my_favorite_fruit}.'
print(message) #Salida: Mi fruta favorita es la Banana.

motorcycles = ["honda", "yamaha", "suzuki"]
#Agregar elementos a una lista
motorcycles.append("ducati")
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

#Agregar elementos en una posicion especifica
motorcycles.insert(1, "bmw")
print(motorcycles) #Salida: ['honda', 'bmw', 'yamaha', 'suzuki', 'ducati']

#Eliminar elementos de una lista
del motorcycles[2]
print(motorcycles) #Salida: ['honda', 'bmw', 'suzuki', 'ducati']