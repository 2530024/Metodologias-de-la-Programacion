"""
Portada:
Axel Baruc Valdez Ramirez
Matrícula: 2530024
Grupo: IM 1-2


RESUMEN EJECUTIVO:
Un CRUD es un conjunto de operaciones básicas para gestionar datos: 
Create (crear), Read (leer), Update (actualizar) y Delete (eliminar).
Usé una lista de diccionarios porque permite almacenar múltiples registros,
cada uno con sus propios campos, y facilita recorrerlos y modificarlos.
Las funciones ayudan a separar la lógica: cada operación tiene su propio bloque,
lo que hace el código más claro, mantenible y fácil de ampliar.
El programa incluye un menú principal y funciones para crear, consultar,
actualizar, eliminar y mostrar todos los elementos del CRUD.

"""

"""
--------------------------------------------------
6. PROBLEMA ÚNICO: CRUD CON FUNCIONES
--------------------------------------------------

Problema 6.1: Gestor CRUD usando diccionarios y/o listas con funciones.

Descripción:
Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:

- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

El programa debe:

1) Definir una estructura de datos principal:
    - Opción A: dict item_id -> dict con datos del ítem.
- Opción B: list de dicts, cada dict con campos id, name, price, quantity.
    (En comentarios, explica cuál opción escogiste y por qué.)

2) Definir FUNCIONES separadas para cada operación CRUD:
    - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
    - read_item(data_structure, item_id) -> dict o None
    - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
    - delete_item(data_structure, item_id) -> bool
    - list_items(data_structure) -> list o simplemente imprime
    Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

3) Implementar un MENÚ en el código principal (main loop):
    Ejemplo de opciones:
    - 1) Create item
    - 2) Read item by id
    - 3) Update item by id
    - 4) Delete item by id
    - 5) List all items
    - 0) Exit

4) En el bucle principal:
    - Mostrar el menú.
    - Leer la opción.
    - Según la opción, pedir los datos necesarios (id, name, price, quantity).
    - Llamar a la función correspondiente.
    - Mostrar mensajes claros de resultado.

Entradas:
- option (string o int; opción de menú).
- item_id (string o int).
- name (string).
- price (float).
- quantity (int).

Salidas:
- Mensajes tipo:
    - "Item created"
    - "Item updated"
    - "Item deleted"
    - "Item not found"
    - "Items list:" y luego la lista de elementos (formato libre pero legible).

Validaciones:
- option debe ser una de las opciones definidas (por ejemplo 0–5).
- item_id no vacío tras strip().
- price y quantity deben ser números válidos:
    - price >= 0.0
    - quantity >= 0
- Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
- En CREATE:
    - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
- En READ/UPDATE/DELETE:
    - Si el id no existe, mostrar "Item not found".

Requisitos de funciones:
- Cada operación CRUD debe estar encapsulada en al menos una función.
- El código del menú principal NO debe contener toda la lógica; debe delegar a las funciones.
- Las funciones deben tener nombres descriptivos y usar parámetros/return en lugar de depender de variables globales (en lo posible).

Sugerencia de flujo:
- Un while principal que corre hasta que el usuario elija 0 (Exit).
- Dentro del while:
    - Mostrar menú.
    - Leer opción.
    - if/elif para decidir qué función llamar.
- Probar el programa con varios casos antes de entregar.
"""

def create_item(store, item_id, name, price, quantity):
    """
    Crea un ítem en la estructura store.
    - Si el id ya existe, no permite duplicado y retorna None.
    - Si se crea, retorna el dict del ítem creado.
    """
    key = str(item_id)
    if key in store:
        return None
    item = {
        "id": key,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    store[key] = item
    return item

def read_item(store, item_id):
    """
    Devuelve el item dict si existe, o None si no existe.
    """
    return store.get(str(item_id))

def update_item(store, item_id, new_name, new_price, new_quantity):
    """
    Actualiza los campos del ítem con item_id.
    - Retorna True si se actualizó correctamente.
    - Retorna False si el item no existe.
    """
    key = str(item_id)
    if key not in store:
        return False
    store[key]["name"] = new_name
    store[key]["price"] = new_price
    store[key]["quantity"] = new_quantity
    return True

def delete_item(store, item_id):
    """
    Borra el ítem con item_id.
    - Retorna True si el item existía y fue borrado.
    - Retorna False si no existía.
    """
    key = str(item_id)
    if key in store:
        del store[key]
        return True
    return False

def list_items(store):
    """
    Devuelve la lista de items almacenados.
    """
    return list(store.values())

def input_non_empty(prompt):
    """
    Lee una línea y devuelve la cadena sin espacios al inicio/final si no está vacía.
    Si está vacía, retorna None.
    """
    s = input(prompt).strip()
    return s if s != "" else None

def parse_price(s):
    """
    Intenta convertir a float y validar price >= 0.0.
    """
    try:
        p = float(s)
        if p < 0.0:
            return None
        return p
    except ValueError:
        return None

def parse_quantity(s):
    """
    Intenta convertir a int y validar quantity >= 0.
    """
    try:
        q = int(s)
        if q < 0:
            return None
        return q
    except ValueError:
        return None

def print_item(item):
    """
    Imprime un item de forma legible.
    """
    print(f"- id: {item['id']}, name: {item['name']}, price: {item['price']}, quantity: {item['quantity']}")

# Bucle principal colocado directamente en nivel superior según petición (sin función main)
store = {}
MENU = (
    "\nSelecciona una opción:\n"
    "1) Create item\n"
    "2) Read item by id\n"
    "3) Update item by id\n"
    "4) Delete item by id\n"
    "5) List all items\n"
    "0) Exit\n"
    "Opción: "
)

while True:
    option = input(MENU).strip()
    # Validación básica de opción
    if option not in {"0", "1", "2", "3", "4", "5"}:
        print("Error: invalid input")
        continue

    if option == "0":
        print("Saliendo...")
        break

    if option == "1":
        # Create
        item_id = input_non_empty("Ingrese id: ")
        if item_id is None:
            print("Error: invalid input")
            continue
        name = input_non_empty("Ingrese name: ")
        if name is None:
            print("Error: invalid input")
            continue
        price_s = input("Ingrese price: ").strip()
        price = parse_price(price_s)
        if price is None:
            print("Error: invalid input")
            continue
        quantity_s = input("Ingrese quantity: ").strip()
        quantity = parse_quantity(quantity_s)
        if quantity is None:
            print("Error: invalid input")
            continue

        created = create_item(store, item_id, name, price, quantity)
        if created is None:
            # Política: no permitir duplicados
            print("Error: invalid input (id already exists)")
        else:
            print("Item created")

    elif option == "2":
        # Read
        item_id = input_non_empty("Ingrese id: ")
        if item_id is None:
            print("Error: invalid input")
            continue
        item = read_item(store, item_id)
        if item is None:
            print("Item not found")
        else:
            print("Item encontrado:")
            print_item(item)

    elif option == "3":
        # Update
        item_id = input_non_empty("Ingrese id del item a actualizar: ")
        if item_id is None:
            print("Error: invalid input")
            continue
        # Primero verificar existencia
        if read_item(store, item_id) is None:
            print("Item not found")
            continue

        new_name = input_non_empty("Ingrese new name: ")
        if new_name is None:
            print("Error: invalid input")
            continue
        new_price_s = input("Ingrese new price: ").strip()
        new_price = parse_price(new_price_s)
        if new_price is None:
            print("Error: invalid input")
            continue
        new_quantity_s = input("Ingrese new quantity: ").strip()
        new_quantity = parse_quantity(new_quantity_s)
        if new_quantity is None:
            print("Error: invalid input")
            continue

        ok = update_item(store, item_id, new_name, new_price, new_quantity)
        if ok:
            print("Item updated")
        else:
            print("Item not found")

    elif option == "4":
        # Delete
        item_id = input_non_empty("Ingrese id: ")
        if item_id is None:
            print("Error: invalid input")
            continue
        ok = delete_item(store, item_id)
        if ok:
            print("Item deleted")
        else:
            print("Item not found")

    elif option == "5":
        # List all
        items = list_items(store)
        print("Items list:")
        if not items:
            print("(no items)")
        else:
            for it in items:
                print_item(it)

"""
CONCLUSIONES
El uso de funciones permitió dividir el CRUD en partes claras, evitando repetir código
y facilitando la lectura y el mantenimiento del programa. Trabajar con una lista
de diccionarios resultó práctico porque admite múltiples registros organizados por claves,
haciendo más sencilla la búsqueda y actualización. Un reto frecuente fue validar entradas
del usuario (como campos vacíos o tipos incorrectos), lo cual solucioné agregando verificaciones
antes de procesar los datos. Este CRUD podría ampliarse guardando información en archivos
como JSON o integrándolo con una base de datos para mantener persistencia y estructuras más complejas.

REFERENCES:
1) Python Documentation – Data Structures (List, Dict)
2) Python Documentation – Functions and Scope
3) Tutoriales de CRUD en memoria con Python (material de cursos y guías educativas)

"""