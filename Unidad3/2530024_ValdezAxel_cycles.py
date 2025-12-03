"""
Portada:
Nombre: Axel Baruc Valdez Ramirez
Matricula: 2530024
Grupo: IM 1-2

RESUMEN EJECUTIVO:
Un bucle for se utiliza para recorrer secuencias o rangos de valores de forma controlada y predecible,
ideal cuando se conoce la cantidad de iteraciones. 
El bucle while resulta más natural cuando la repetición depende de una condición que puede cambiar dinámicamente,
como la lectura de datos hasta que el usuario ingrese un valor válido. 
Un contador incrementa el número de repeticiones y un acumulador suma valores progresivamente. 
Definir correctamente la condición de salida es esencial para evitar ciclos infinitos y asegurar que el programa avance. 
El documento incluirá la descripción de cada problema, el diseño de entradas y salidas, las validaciones aplicadas
y el uso de for y while en diversos contextos como recorridos, creación de menús y lectura repetida de información.

"""

"""
Problem 1: Sum of range with for

Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.

Entradas:
- n (int; límite superior del rango).

Salidas:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de range(1, n + 1)
- Uso de un for con acumuladores para total_sum y even_sum.
"""

def sum_of_range(n):
    try:
        n = int(n)
        if n < 1:
            print("Error: invalid input")
            return

        total_sum = 0
        even_sum = 0

        for number in range(1, n + 1):
            total_sum += number
            if number % 2 == 0:
                even_sum += number

        print(f"Sum 1..{n}: {total_sum}")
        print(f"Even sum 1..{n}: {even_sum}")

    except ValueError:
        print("Error: invalid input")

# Example usage:
n = input("Enter a positive integer n: ")
sum_of_range(n)

"""
    Test cases:
1) Normal: n = 5
    Output: Sum 1..5: 15
            Even sum 1..5: 6
2) Border: n = 1
    Output: Sum 1..1: 1
            Even sum 1..1: 0
3) Error: n = -3
    Output: Error: invalid input
"""

"""
Problem 2: Multiplication table with for
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entradas:
- base (int)
- m (int; límite de la tabla)

Salidas:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, m + 1):
- Cálculo de producto y formateo de la salida con f-strings.
"""
def multiplication_table(base, m):
    try:
        base = int(base)
        m = int(m)
        if m < 1:
            print("Error: invalid input")
            return

        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")

    except ValueError:
        print("Error: invalid input")

# Example usage:
base = input("Enter the base number: ")
m = input("Enter the limit m: ")
multiplication_table(base, m)

"""
    Test cases:
1) Normal: base = 3, m = 5
    Output:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
2) Border: base = 7, m = 1
    Output:
    7 x 1 = 7
3) Error: base = 4, m = 0
    Output: Error: invalid input
"""

"""
Problem 3: Factorial with while
Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.

Entradas:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Salidas:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

Operaciones clave sugeridas:
- while True con break al leer el sentinela o
- while number != sentinel_value
- Acumulador para suma y contador para cantidad.
"""
def average_until_sentinel(sentinel_value=-1):
    total_sum = 0.0
    count = 0

    while True:
        user_input = input("Enter a number (or -1 to finish): ")
        try:
            number = float(user_input)
            if number == sentinel_value:
                break
            total_sum += number
            count += 1
        except ValueError:
            print("Error: invalid input")

    if count == 0:
        print("Error: no data")
    else:
        average_value = total_sum / count
        print(f"Count: {count}")
        print(f"Average: {average_value}")

# Example usage:
average_until_sentinel()

"""
    Test cases:
1) Normal: Inputs: 5, 10, -1
    Output: Count: 2
            Average: 7.5
2) Border: Inputs: abc, 4, -1
    Output: Error: invalid input
            Count: 1
            Average: 4.0
3) Error: Inputs: -1
    Output: Error: no data
"""

"""
Problem 4: Password attempts with while
Descripción:
Implementa un sistema sencillo de intento de contraseña. Define en el código una contraseña correcta (por ejemplo, "admin123"). El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

Operaciones clave sugeridas:
- while attempts < MAX_ATTEMPTS:
- Comparación de cadenas, contador de intentos.
- Opción de usar break al éxito.
"""
def password_attempts():
    CORRECT_PASSWORD = "admin123"
    MAX_ATTEMPTS = 3
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        user_password = input("Enter password: ")
        if user_password == CORRECT_PASSWORD:
            print("Login success")
            return
        else:
            attempts += 1
            print("Incorrect password")

    print("Account locked")

# Example usage:
password_attempts()

"""
    Test cases:
1) Normal: Inputs: admin123
    Output:
    Login success
2) Border: Inputs: wrong, admin123
    Output:
    Incorrect password
    Login success
3) Error: Inputs: wrong, wrong, wrong
    Output:
    Incorrect password
    Incorrect password
    Incorrect password
    Account locked
"""

"""
Problem 5: Simple menu with while
Descripción:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.

Entradas:
- option (string o int; elección del usuario).

Salidas:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

Operaciones clave sugeridas:
- while option != 0:
- if/elif para cada opción.
- Variable counter inicializada fuera del bucle.
"""
def simple_menu():
    counter = 0

    while True:
        print("Menu:")
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")

        user_input = input("Select an option: ")
        try:
            option = int(user_input)
        except ValueError:
            print("Error: invalid option")
            continue

        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")

# Example usage:
simple_menu()
"""
    Test cases:
1) Normal: Inputs: 1, 2, 3, 2, 0
    Output:
    Hello!
    Counter: 0
    Counter incremented
    Counter: 1
    Bye!
2) Border: Inputs: 4, 0
    Output:
    Error: invalid option
    Bye!
3) Error: Inputs: abc, 4, -1, 0
    Output:
    Error: invalid option
    Error: invalid option
    Error: invalid option
    Bye!
"""

"""
Problem 6: Pattern printing with nested loops
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, n + 1):
    - construir una cadena con i asteriscos usando "*" * i
- (Opcional) otro bucle for para el patrón invertido.
"""
def print_patterns(n):
    try:
        n = int(n)
        if n < 1:
            print("Error: invalid input")
            return

        # Print normal pattern
        for i in range(1, n + 1):
            print("*" * i)

        # Optional: Print inverted pattern
        print()  # Blank line between patterns
        for i in range(n, 0, -1):
            print("*" * i)

    except ValueError:
        print("Error: invalid input")

# Example usage:
n = input("Enter the number of rows for the pattern: ")
print_patterns(n)

"""
    Test cases:
1) Normal: n = 4
    Output:
    *
    **
    ***
    ****

    ****
    ***
    **
    *
2) Border: n = 1
    Output:
    *

    *
3) Error: n = 0
    Output: Error: invalid input
"""

"""
CONCLUSIONES:
La diferencia principal entre los bucles for y while es que el for es finito y el while cuando no se sabe el rango de repeticiones.
El uso de contadores y acumuladores es esencial para llevar un registro de las iteraciones y los totales en los bucles.
El riesgo del ciclos infinitos es grande por lo que es crucial definir condiciones de salida claras para que el programa finalice y no se relentize el programa o quede atascado.
Los menus e intentos son buenos para una organizacion, mas dinamico y facil de usar para el usuario.
Aprendi que es raro los bucles anidados pero sirven para patrones y estructuras mas complejas.

REFERENCIAS:
# References:
1) Python documentation - The for statement and while statement.
    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
    https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
    
2) Python Tutorial - Control Flow Tools (incluye for, while y break/continue).
    https://docs.python.org/3/tutorial/controlflow.html
    
3) “Automate the Boring Stuff with Python” - Secciones sobre bucles, contadores y acumuladores.

4) Libros y apuntes de algoritmos y programación básica (UNAM, MIT OCW, CUCEI, etc.).

5) Artículos educativos sobre patrones comunes con bucles en Python:
    recorridos, validaciones, menús y lectura repetitiva (Real Python, GeeksforGeeks).

URL DEL REPOSITORIO EN GITHUB:
https://github.com/2530024/Metodologias-de-la-Programacion
"""