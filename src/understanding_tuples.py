"""
    Las tuplas son listas de elementos que no pueden cambiar 
    su tamaño. Las tuplas son listas inmutables

    Se utilizan los () para definir una tupla
    Ejemplo
"""
#Rectangulo (largo, ancho)
rectangle_dimensions = (200, 50) #Tupla
print(f"Largo {rectangle_dimensions[0]} mm") #200
print(f"Ancho {rectangle_dimensions[1]} mm") #50

# Vamos a intentar modificar una tupla
# rectangle_dimensions[0] = 250 #Error de tipo o TypeError
# rectangle_dimensions[1] = 100 #Error de tipo o TypeError

for dimmension in rectangle_dimensions:
    print(dimmension)

"""
    No podemos modificar una tupla, ni tampoco agregar/eliminar elementos.
    Ñp que si podemos hacer es cambiar 
    la asignacion una variable que almacena una tupla
"""

rectangle_dimensions = (300, 150, 50) #Volvemos a definir pero con nuevos valores o agregar o quitar
for dimension in rectangle_dimensions:
    print(dimension)