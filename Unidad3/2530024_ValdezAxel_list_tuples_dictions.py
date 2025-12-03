"""
Portada:
Nombre: Axel Baruc Valdez Ramirez
Matricula: 2530024
Grupo: IM 1-2

Resumen Ejecutivo:
Las listas, tuplas y diccionarios son estructuras fundamentales en Python: 
las listas almacenan elementos ordenados y modificables, las tuplas guardan datos ordenados pero no pueden cambiarse,
y los diccionarios organizan información mediante pares clave–valor. 
Que una lista sea mutable significa que sus elementos pueden agregarse, eliminarse o alterarse,
mientras que la inmutabilidad de una tupla impide cualquier modificación después de creada. 
Los diccionarios permiten acceder rápidamente a información asociando claves únicas con valores específicos,
útiles para representar registros, catálogos y datos indexados. 
El documento abarcará la descripción de cada problema, el diseño de entradas y salidas,
las validaciones aplicadas y el uso práctico de listas, tuplas y diccionarios en situaciones como estadísticas,
almacenamiento de datos y organización estructurada de información.

"""

"""
Problem 1: Shopping list basics (list operations)

Descripción:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).

Entradas:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Salidas:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validaciones:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

Operaciones clave sugeridas:
- split(), strip(), append(), len(), in.
"""

# Input
initial_items_text = input("Enter initial items (comma-separated): ").strip()
new_item = input("Enter a new item to add: ").strip()
search_item = input("Enter an item to search for: ").strip()

# Process
items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
items_list.append(new_item)
len_list = len(items_list)
is_in_list = search_item in items_list
# Output
print("Items list:", items_list)
print("Total items:", len_list)
print("Found item:", is_in_list)

"""
    Test cases:
1) Normal: initial_items_text="apple,banana,orange", new_item="grape", search_item="banana"
    Output: Items list: ['apple', 'banana', 'orange', 'grape']
                Total items: 4
                Found item: true
2) Border: initial_items_text="", new_item="kiwi", search_item="kiwi"
    Output: Items list: ['kiwi']
                Total items: 1
                Found item: true
3) Error: initial_items_text="   ", new_item=" ", search_item="mango"
    Output: Items list: [' ']
                Total items: 1
                Found item: false
"""

"""
    Problem 2: Points and distances with tuples
    Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Entradas:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.

Operaciones clave sugeridas:
- Creación de tuplas: point_a = (x1, y1), point_b = (x2, y2)
- Cálculo de distancia: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
- Cálculo de punto medio: ((x1 + x2)/2, (y1 + y2)/2)
"""

# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
# Process
point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
# Output
print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)

"""
    Test cases:
1) Normal: x1=0, y1=0, x2=3, y2=4
    Output: Point A: (0.0, 0.0)
                Point B: (3.0, 4.0)
                Distance: 5.0
                Midpoint: (1.5, 2.0)
2) Border: x1=1, y1=1, x2=1, y2=1
    Output: Point A: (1.0, 1.0)
                Point B: (1.0, 1.0)
                Distance: 0.0
                Midpoint: (1.0, 1.0)
3) Error: x1="a", y1=2, x2=3, y2=4
    Output: ValueError on float conversion
"""

"""
    Problem 3: Product catalog with dictionary
    Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.

Entradas:
- product_name (string).
- quantity (int; cantidad a comprar).

Salidas:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"

Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).

Operaciones clave sugeridas:
- Definir dict literal: product_prices = {"apple": 10.0, ...}
- in para verificar existencia de clave.
- Acceso: unit_price = product_prices[product_name]
"""

# Input
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}
product_name = input("Enter product name: ").strip()
quantity = int(input("Enter quantity to buy: "))
# Process and Output
if product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")

"""
    Test cases:
1) Normal: product_name="banana", quantity=3
    Output: Unit price: 5.0
                Quantity: 3
                Total: 15.0
2) Border: product_name="apple", quantity=1
    Output: Unit price: 10.0
                Quantity: 1
                Total: 10.0
3) Error: product_name="grape", quantity=2
    Output: Error: product not found
"""

"""
Problem 4: Student grades with dict and list

Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Operaciones clave sugeridas:
- Diccionario de listas: grades = {"Alice": [90, 85], ...}
- sum(), len() para promedio.
- in para verificar clave.
"""

# Input
grades_dict = {
    "Alice": [90.0, 85.0, 78.0],
    "Bob": [60.0, 70.0, 65.0],
    "Charlie": [88.0, 92.0, 95.0]
}
student_name = input("Enter student name: ").strip()
# Process and Output
if student_name in grades_dict:
    grades_list = grades_dict[student_name]
    if grades_list:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", is_passed)
    else:
        print("Error: no grades available")
else:
    print("Error: student not found")

"""
    Test cases:
1) Normal: student_name="Alice"
    Output: Grades: [90.0, 85.0, 78.0]
                Average: 84.33333333333333
                Passed: true
2) Border: student_name="Bob"
    Output: Grades: [60.0, 70.0, 65.0]
                Average: 65.0
                Passed: false
3) Error: student_name="David"
    Output: Error: student not found
"""

"""
Problem 5: Inventory management with list and dict
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Operaciones clave sugeridas:
- lower(), split()
- Recorrer la lista y actualizar el diccionario:
  - if word in freq_dict: freq_dict[word] += 1
  - else: freq_dict[word] = 1
- Uso de un ciclo para encontrar la palabra con mayor frecuencia.
"""

# Input
sentence = input("Enter a sentence: ").strip()
# Process
words_list = sentence.lower().split()
freq_dict = {}
for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1
most_common_word = max(freq_dict, key=freq_dict.get) if freq_dict else None
# Output
print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word)
"""
    Test cases:
1) Normal: sentence="This is a test. This test is only a test."
    Output: Words list: ['this', 'is', 'a', 'test.', 'this', 'test', 'is', 'only', 'a', 'test.']
                Frequencies: {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}
                Most common word: this
2) Border: sentence="Hello hello HELLO"
    Output: Words list: ['hello', 'hello', 'hello']
                Frequencies: {'hello': 3}
                Most common word: hello
3) Error: sentence="   "
    Output: Words list: []
                Frequencies: {}
                Most common word: None
"""

"""
    Problem 6: Simple contact book (dictionary CRUD)
    Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().

Operaciones clave sugeridas:
- Diccionario: contacts = {"Alice": "1234567890", ...}
- get(), in, pop()
- Estructura if/elif para manejar cada acción.
"""

# Input
contacts = {
    "Alice": "1234567890",
    "Bob": "0987654321"
}
action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
name = input("Enter contact name: ").strip()
# Process and Output
if action_text == "ADD":
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print("Contact saved:", name, phone)
elif action_text == "SEARCH":
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Error: contact not found")
elif action_text == "DELETE":
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted:", name)
    else:
        print("Error: contact not found")
else:
    print("Error: invalid action")

"""
    Test cases:
1) Normal: action_text="ADD", name="Charlie", phone="5555555555"
    Output: Contact saved: Charlie 5555555555
2) Border: action_text="SEARCH", name="Alice"
    Output: Phone: 1234567890
3) Error: action_text="DELETE", name="David"
    Output: Error: contact not found
"""

"""
    CONCLUSIONES:
Las listas resultan convenientes cuando se requiere modificar el conjunto de datos con frecuencia,
ya que permiten agregar, quitar o reorganizar elementos con facilidad. 
Las tuplas funcionan mejor para valores que deben mantenerse fijos, como coordenadas o configuraciones estables. 
Los diccionarios destacan cuando se necesita acceder rápidamente a información mediante claves identificadoras. 
Al combinar estas estructuras surgen patrones comunes, como diccionarios que almacenan listas para agrupar datos,
o listas de diccionarios para manejar registros más complejos. 
Elegir la estructura correcta depende del nivel de cambio esperado y de cómo se necesite consultar la información.

REFERENCIAS:
1) Python documentation – Built-in Types: list, tuple, dict. https://docs.python.org/3/library/stdtypes.html
2) Python Tutorial – Data Structures (listas, tuplas, diccionarios). https://docs.python.org/3/tutorial/datastructures.html
3) “Automate the Boring Stuff with Python” – Capítulos sobre colecciones y estructuras de datos.
4) Apuntes de algoritmos y programación básica de cursos universitarios (UNAM, MIT OCW, etc.).
5) Artículos y guías de buenas prácticas en el uso de colecciones en Python (Real Python, GeeksforGeeks).
6) Notas de clase sobre modelado de información y organización de datos en Python.

"""