"""
Portada:
Nombre: Axel Baruc Valdez Ramirez
Matrícula: 2530024
Grupo: IM 1-2

Resumen Ejecutivo:
La serie de Fibonacci es una sucesión donde cada número resulta de sumar los dos anteriores.
Calcular la serie hasta un número de términos n significa generar los primeros n valores de la secuencia.
El programa leerá un valor n ingresado por el usuario, verificará que sea un número entero y mayor a cero,
y luego generará la serie de Fibonacci hasta alcanzar esa cantidad de términos.
Finalmente mostrará la lista completa de números generados.

"""

"""
--------------------------------------------------
6. PROBLEMA ÚNICO
--------------------------------------------------

6.1 Problem: Fibonacci series up to n terms

Descripción:
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.

Entradas:
- n (int; número de términos de la serie a generar).

Salidas:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validaciones:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.

Ejemplo de comportamiento esperado (no pegues el código completo, solo úsalo como referencia lógica):
- Entrada: n = 5
- Salida:
- Fibonacci series: 0 1 1 2 3
"""

try:
    n = int(input("Enter the number of terms: "))
    if n < 1 or n > 50:
        print("Error: invalid input")
    else:
        fibonacci_series = []
        a, b = 0, 1
        for i in range(n):
            fibonacci_series.append(a)
            a, b = b, a + b
        print("Fibonacci series:", ' '.join(map(str, fibonacci_series)))
except ValueError:
    print("Error: invalid input")

"""
    Test cases:
    1) Normal: n = 5 → expected series: 0 1 1 2 3
    2) Border: n = 1 → expected series: 0
    3) Error: n = -3 → expected message: "Error: invalid input"
"""

"""
--------------------
    CONSLUSIONES
--------------------

El uso de un bucle facilitó generar la serie paso a paso sin repetir código manualmente.
Manejar correctamente los casos n = 1 y n = 2 evita errores y garantiza que la salida sea coherente con la definición original.
Esta misma lógica puede reutilizarse en programas donde se calculen secuencias numéricas,
se simulen procesos iterativos o se generen datos dependientes de pasos previos.

REFERENCIAS:
1) Python Documentation - "for" and "while" statements: https://docs.python.org/3/tutorial/controlflow.html
2) Python Docs - Ejemplos de funciones y recursividad: https://docs.python.org/3/tutorial/datastructures.html
3) Tutoriales de programación en Python - Serie de Fibonacci (Real Python, W3Schools, Programiz)

"""
