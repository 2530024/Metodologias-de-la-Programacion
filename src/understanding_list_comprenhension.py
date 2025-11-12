#List comprenhensions
"""
    Ula list comprenhension combina el for loop
    y la creacion de nuevos elementos en una sola
    linea de codigo y tambien, automaticamente
    agrega el nuevo elemtnto a la lista, es decir,
    sin utilizar el append
"""

squares=[value**2 for value in range(1,11)]
print(squares)

#Numeros pares con el range
even_number_0_100 = list(range(0,101,2))
print(even_number_0_100)

#Numeros pares utilizando el list comprenhension
evens_list_compre = [value for value in range(0,101) if value%2 ==0]
print("Evens List comprenhensions: ", evens_list_compre)