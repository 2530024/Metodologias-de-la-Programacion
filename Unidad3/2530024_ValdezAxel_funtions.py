"""
Portada: Axel Baruc Valdez Ramirez
Matricula: 2530024
Grupo: IM 1-2

RESUMEN EJECUTIVO:
Una función en Python es un bloque de código organizado que realiza una tarea específica
y permite reutilizar lógica sin repetir instrucciones. 
Los parámetros se definen al crear la función y actúan como variables internas,
mientras que los argumentos son los valores reales que se envían al llamarla. 
Dividir la lógica en funciones facilita la estructura del programa, mejora la lectura
y permite reutilizar comportamientos en distintos contextos. 
Un valor de retorno entrega un resultado a quien llamó la función, lo cual es preferible
a solo imprimir porque permite seguir procesando datos y hacer pruebas más precisas. 
El documento incluirá la descripción de cada problema, el diseño de las funciones,
la definición de entradas y salidas, las validaciones implementadas y algunas pruebas básicas.

"""

"""
Problem 1: Rectangle area and perimeter (basic functions)
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.

Entradas:
- width (float)
- height (float)

Salidas:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

Operaciones clave sugeridas:
- area = width * height
- perimeter = 2 * (width + height)
"""

def calculate_area(width, height):
    #Calculate the area of a rectangle.
    return width * height
def calculate_perimeter(width, height):
    #Calculate the perimeter of a rectangle.
    return 2 * (width + height)
# Código principal
try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
except ValueError:
    print("Error: invalid input")


"""
Test cases:
1) Normal:
    - Input: width = 5, height = 10
    - Output: Area: 50, Perimeter: 30
2) Border:
    - Input: width = 0.1, height = 0.1
    - Output: Area: 0.01, Perimeter: 0.4
3) Error:
    - Input: width = -5, height = 10
    - Output: Error: invalid input
"""

"""
Problem 2: Grade classifier (function with return string)
escripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Entradas:
- score (float o int)

Salidas:
- "Score:" <score>
- "Category:" <grade_letter>

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.

Operaciones clave sugeridas:
- if/elif para rangos.
- Función con un único return al final o varios returns (pero bien documentados).
"""

def classify_grade(score):
    #Classify the grade based on the score.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Código principal
try:
    score = float(input("Enter score (0-100): "))
    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        category = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {category}")
except ValueError:
    print("Error: invalid input")

"""
Test cases:
1) Normal:
    - Input: score = 85
    - Output: Score: 85, Category: B
2) Border:
    - Input: score = 90
    - Output: Score: 90, Category: A
3) Error:
    - Input: score = 105
    - Output: Error: invalid input
"""

"""
Problem 3: List statistics function (min, max, average)

Descripción:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), llamar la función y mostrar los valores.

Entradas:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Salidas:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- split() para construir la lista de strings.
- Conversión a float o int dentro de un ciclo.
- sum(), len(), min(), max() dentro de summarize_numbers().
"""
def summarize_numbers(numbers_list):
    #Summarize the list of numbers: min, max, average.
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)
    return {
        "min": minimum,
        "max": maximum,
        "average": average
    }
# Código principal
numbers_text = input("Enter numbers separated by commas: ").strip()
if not numbers_text:
    print("Error: invalid input")
else:
    try:
        numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
        if not numbers_list:
            print("Error: invalid input")
        else:
            summary = summarize_numbers(numbers_list)
            print(f"Min: {summary['min']}")
            print(f"Max: {summary['max']}")
            print(f"Average: {summary['average']}")
    except ValueError:
        print("Error: invalid input")

"""
Test cases:
1) Normal:
    - Input: "10, 20, 30"
    - Output: Min: 10.0, Max: 30.0, Average: 20.0
2) Border:
    - Input: "5"
    - Output: Min: 5.0, Max: 5.0, Average: 5.0
3) Error:
    - Input: ""
    - Output: Error: invalid input
"""

"""
Problem 4: Apply discount list (pure function)
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.

Entradas:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Salidas:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- Construir la lista de float desde texto.
- En la función, usar un ciclo para crear una nueva lista:
  - discounted_price = price * (1 - discount_rate)
- No modificar la lista de entrada (pure function).
"""
def apply_discount(prices_list, discount_rate):
    #Apply discount to the list of prices and return a new list.
    discounted_prices = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_prices.append(discounted_price)
    return discounted_prices
# Código principal
prices_text = input("Enter prices separated by commas: ").strip()
try:
    discount_rate = float(input("Enter discount rate (0-1): "))
    if not prices_text:
        print("Error: invalid input")
    else:
        prices_list = [float(price.strip()) for price in prices_text.split(",")]
        if any(price <= 0 for price in prices_list) or discount_rate < 0 or discount_rate > 1:
            print("Error: invalid input")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)
            print(f"Original prices: {prices_list}")
            print(f"Discounted prices: {discounted_list}")
except ValueError:
    print("Error: invalid input")

"""
Test cases:
1) Normal:
    - Input: prices = "100, 200, 300", discount_rate = 0.10
    - Output: Original prices: [100.0, 200.0, 300.0], Discounted prices: [90.0, 180.0, 270.0]
2) Border:
    - Input: prices = "50", discount_rate = 0.0
    - Output: Original prices: [50.0], Discounted prices: [50.0]
3) Error:
    - Input: prices = "100, -50", discount_rate = 0.10
    - Output: Error: invalid input
"""

"""
Problem 5: Greeting function with default parameters
Descripción:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Entradas:
- name (string)
- title (string opcional)

Salidas:
- "Greeting:" <greeting_message>

Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().

Operaciones clave sugeridas:
- Uso de parámetros con valor por defecto: def greet(name, title=""):
- Uso de argumentos nombrados: greet(name="Alice", title="Dr.")
"""
def greet(name, title=""):
    #Generate a greeting message with optional title.
    full_name = f"{title} {name}".strip() if title else name
    return f"Hello, {full_name}!"
# Código principal
name = input("Enter name: ").strip()
title = input("Enter title (optional): ").strip()
if not name:
    print("Error: invalid input")
else:
    greeting_message = greet(name, title=title)
    print(f"Greeting: {greeting_message}")

"""
Test cases:
1) Normal:
    - Input: name = "Alice", title = "Dr."
    - Output: Greeting: Hello, Dr. Alice!
2) Border:
    - Input: name = "Bob", title = ""
    - Output: Greeting: Hello, Bob!
3) Error:
    - Input: name = "", title = "Mr."
    - Output: Error: invalid input
"""

"""
Problem 6: Factorial function (iterative or recursive)
Descripción:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <factorial_value>

Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Versión iterativa:
  - result = 1
  - for i in range(1, n + 1): result *= i
- Versión recursiva (opcional):
  - factorial(0) = 1
  - factorial(n) = n * factorial(n - 1)
"""
def factorial(n):
    #Calculate factorial of n iteratively to avoid recursion limits.
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Código principal
try:
    n = int(input("Enter a non-negative integer n: "))
    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        fact_value = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {fact_value}")
except ValueError:
    print("Error: invalid input")

"""
Test cases:
1) Normal:
    - Input: n = 5
    - Output: n: 5, Factorial: 120
2) Border:
    - Input: n = 0
    - Output: n: 0, Factorial: 1
3) Error:
    - Input: n = -3
    - Output: Error: invalid input
"""

"""
CONCLUSIONES:
Las funciones son las herramientas fundamentales para organizar y modularizar el código en Python asi como encapsular lógica reutilizable.
Al devolver el valor se puede guardar en una variable o usarlo en otras operaciones, lo que mejora la flexibilidad y reutilización del código.
Evita defaults mutables; usa None como sentinel y crea la instancia dentro, valida límites y tipos cuando el default pudiera producir un comportamiento inseguro.
Los casos son calculos repetidos, Validaciones (email, rango, tipo), operaciones comunes (promedio, suma, min, max), transformaciones (formateo, conversiones) y lógica de negocio específica.
La logica principal debe ser clara y llamar a funciones bien definidas para mantener la legibilidad y facilitar el mantenimiento del código.

REFERENCIAS:
1) Python documentation – Defining Functions (def, return, parameters, scope).
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions

2) Python documentation – Functions and Variable Scope.
    https://docs.python.org/3/reference/executionmodel.html#naming-and-binding

3) “Automate the Boring Stuff with Python” – Capítulos sobre funciones, parámetros y retorno.

4) Libros y apuntes de algoritmos y programación básica utilizados en cursos universitarios (UNAM, MIT OCW, etc.).

5) Artículos sobre diseño de funciones, buenas prácticas y modularización del código
    (Real Python, GeeksforGeeks, Programiz).
"""