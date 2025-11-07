magicians = ["ron", "harry", "hermione", "snape"]
#Ciclo For
for elemento in magicians:
    print(elemento)
    print(elemento.upper())
    print(f"{elemento.title()}ese fue un gran hechizo")
    print("\n")

#For de enteros
for value in range(1,6):
    print(value)

"""

    Identacion. 

    Python usa la identacion para definir bloques de codigo.
    Cuando una linea de codigo esta concectada a la linea de codigo 
    anterior

    Basicamente, se utilizan 4 espacios en blanco
    para obligarnos a escribir codigo ordenado y estructurado

"""

#No olvidemos identar (donde necesita)
#Ejemplo
magicions = ["alice", "david", "jorge"]
for magician in magicions:
    print(f"{magician.title()}, ese fue un gran hechizo!")
print(f"No puedo esperar a ver tu proximo hechizo, {magician.title()}.\n")

#Identacion innesesaria
message = "Hello Python world!"
# print(message) #Error

#Error de syntaxis
magicians = ["ron", "harry", "hermione", "snape"]
for magician in magicians: # (SyntaxisError): olvidar colocar los dos puntos (:)
    print(magician)