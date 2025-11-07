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
"""
    Agregar elementos a una lista
"""
print("\nAgregar elementos a una lista")
motorcycles.append("ducati")
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

#Agregar elementos en una posicion especifica
motorcycles.insert(1, "bmw")
print(motorcycles) #Salida: ['honda', 'bmw', 'yamaha', 'suzuki', 'ducati']

"""
    Eliminar elementos de una lista
        -del: Elimina un elemento de una lista en una posicion especifica usando su indice.
    La declaracion del index elimina el elemtp en la posicion especificada.
"""
print("\nEliminar elementos de una lista")
del motorcycles[2]
print(motorcycles) #Salida: ['honda', 'bmw', 'suzuki', 'ducati']


"""
    Eliminar elementos de una lista
        -pop(): Elimina un elemento de una lista y lo devuelve para su uso posterior.
    El metodo pop() elimina el ultimo elemento de la lista si no se especifica un indice
"""
print("\nEliminar elementos de una lista con pop()")
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()
print(motorcycles) 
print(f'La motocicleta que fue eliminada es: {popped_motorcycle}')

"""
    Eliminar elementos de una lista
        -pop(index): Elimina un elemento de una lista en una posicion especifica usando su indice.
    El metodo pop(index) toma un argumento de indice que especifica la posicion del elemento a eliminar.
"""
print("\nEliminar elementos de una lista con pop(index)")
motorcycles = ["honda", "yamaha", "suzuki"]
first_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta que fue eliminada es: {first_motorcycle}')

"""
    Eliminar elementos de una lista
        -remove(value): Elimina un elemento de una lista por su valor.
    El metodo remove(valor) busca el valor especificado y lo elimina de la lista.
"""
print("\nEliminar elementos de una lista con remove(value)")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.remove("suzuki")
print(motorcycles)

#Ejemplo practico del metodo remove()
names = ["ana", "carlos", "maria", "juan"]
print("\nEjemplo practico del metodo remove()")
print(names)
deleted_name = input("Ingresa un nombre para eliminar de la lista: ")
names.remove(deleted_name.strip().lower())
print(names)

"""
    Ordenar elementos en una lista
        -sort(): Ordena los elementos de una lista en orden alfabetico o numerico.
    El metodo sort() modifica la lista original para que sus elementos esten en orden.
"""

cars = ["bmw", "audi", "toyota", "subaru", "ford", "kia"]
print("\nOrdenar elementos en una lista con sort()")
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

"""
    Invertir el orden de los elementos en una lista
        -reverse(): Invierte el orden de los elementos en una lista.
    Metodo reverse()
"""

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print("\nInvertir el orden de los elementos en una lista con reverse()")
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

"""
    Obtener la longitud de una lista
        -len(): Devuelve el numero de elementos en una lista.
    Metodo built-in len()
"""

cars = ["bmw", "audi", "toyota", "subaru"]
print("\nObtener la longitud de una lista con len()")
print(f'La cantidad de elementos en la lista es: {len(cars)}')

"""
    Metodo built-in 
        sorted(): Devuelve una nueva lista temporalmente
    
"""

favorite_students = ["jorge", "Jose", "carlos", "emiliano"]
print(favorite_students)

print(sorted(favorite_students))