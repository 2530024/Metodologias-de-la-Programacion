"""
    Las listas tambien pueden almacenar numeros y de hecho, son ideales para almacenarlos.
    Python ofrece cantidad de funciones integradas para trabajar con listas de numeros.

    Por ejemplo, funcion range() 
"""

#La funcion range() genera una serie de numeros, en un rango especifico
numbers = list(range(1,6))
print(numbers) #Salida [1, 2, 3, 4, 5]
print(type(numbers))

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)
    print(type(num))

for num in range(1,6):
    print(num)

for num in range(1, 10, 2): #Numeros impares
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) #Salida

for num in range(2, 10, 2): #Numeros pares
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) #Salida [2, 4, 6, 8]

# El ciclo while tambien puede ser utilizado para generar una lista de numeros
count = 1
numbers = []
while count < 6:
    numbers.append(count)
    count += 1
print(numbers) #Salida [1, 2, 3, 4, 5]

## Podemos crear cualquier tipo de listas de numeros
## utilizando range() y list()
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) #Salida [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Metodos built-in para listas de numeros
print("\n Metodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista original: {digits}")
print(f"Minimo: {min(digits)}") #Salida Minimo: 0
print("Valor maximo:", max(digits)) #Salida Valor maximo: 9
print("Suma de todos los elementos:", sum(digits)) #Salida Suma de todos los elementos: 45