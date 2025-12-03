"""
    Portada
    Nombre: Axel Baruc Valdez Ramirez
    Matricula: 2530024
    Grupo: IM 1-2

    Resumen ejecutivo:
    ¿Que es un string en Python (tipo de dato, inmutabilidad)?
    Un string en Python es una secuencia de caracteres que se utiliza para representar texto. Se define utilizando
    comillas simples (' ') o comillas dobles (" "). Los strings son inmutables, Lo que significa que una vez que se crea un string, no se puede modificar directamente.

    ¿Que operaciones basicas se pueden realizar con strings?
    Concatenar, obtener longitud, extraer subcadenas, buscar patrones, remplazar texto
    
    ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, nombres, contraseñas)?
    Es importante validar y normalizar texto de entrada para asegurar que los datos sean correctos, consistentes y seguros.

    ¿Qué cubrirá tu documento?
    descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas y uso de métodos de string con casos de prueba (incluyendo el código).
"""

#Problem 1: Fullname Formatter (name + initials)
"""
    Description: Given a person's full name in a single string (e.g., "juan carlos tovar"), the program should:
1) Normalize the text (adjusting spaces, including capitalization).
2) Display the formatted name in a Title Case and the initials (e.g., J.C.T.).
"""

full_name = input("Enter full name: ")

full_name = full_name.lower().strip()
if full_name.count(' ') > 0:
    names = full_name.split()
    initials = ''.join([name[0].upper() + '.' for name in names])
    print("Formatted Name:", ' '.join(names).title())
    print("Initials:", initials)
else:
    print("Please enter at least a first name and a last name.")

"""
    Test cases:
1) Normal: Input: "juan carlos tovar" -> Output: "Juan Carlos Tovar", "J.C.T."
2) Border: Input: "  maria  lopez  " -> Output: "Maria Lopez", "M.L."
3) Error: Input: "singleName" -> Output: "Please enter at least a first name and a last name."

"""

"""
    Problem 2: Simple email validator (structure + domain)

    Description: Validates whether an email address has a correct basic format:
- Contains exactly one '@'.
- There must be at least one '.' after the '@'.
- Contains no spaces.
If the email is valid, it also displays the domain (the part after the '@').
"""
email = input("Enter email address: ")
email = email.strip()
#Validations
if email.count('@') == 1 and ' ' not in email:
    domain_part = email[email.find('@') + 1:]
    if '.' in domain_part:
        print("Valid email: true")
        print("Domain:", domain_part)
    else:
        print("Invalid email: No '.' found in the domain part.")
else:
    print("Valid email: false")

"""
    Test cases:
1) Normal: hola@gmail.com -> Valid email: true, Domain: gmail.com
2) Border: hola@domain -> Invalid email: No '.' found in the domain part.
3) Error: hola@@gmail.com -> Valid email: false
"""

"""
    Problem 3: Palindrome checker (ignoring spaces and case)

    Description: Determines if a phrase is a palindrome, that is, it reads the same from left 
    to right and from right to left, ignoring spaces and uppercase/lowercase letters.
"""
phrase = input("Enter a phrase: ")
normalized_phrase = phrase.lower().strip().replace(' ', '')
if normalized_phrase == normalized_phrase[::-1] and len(normalized_phrase) >= 3:
    print("The phrase is a palindrome.")
else:
    print("Invalid length or the phrase is not a palindrome.")

"""
    Test cases
1) Normal: "A man a plan a canal Panama" -> The phrase is a palindrome.
2) Border: "No x in Nixon" -> The phrase is a palindrome.
3) Error: "Hi" -> Invalid length or the phrase is not a palindrome.
"""

"""
    Problem 4: Sentence word stats (lengths and first/last word)
    Description:
Given a sentence, the program should:
1) Normalize spaces (remove leading and trailing spaces).
2) Separate words with spaces.
3) Display:
- Total number of words.
- First word.
- Last word.
- Shortest and longest words (by length).
"""

sentence = input("Enter a sentence: ")
sentence = sentence.strip()
words = sentence.split()
if len(words) > 0 and words != ['']:
    first_word = words[0]
    last_word = words[-1]
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    print("Total words:", len(words))
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)

"""
    Test cases:
1) Normal: "  The quick brown fox jumps over the lazy dog  " -> Total words: 9, First word: The, Last word: dog, Shortest word: The, Longest word: jumps"
2) Border: "Hello" -> Total words: 1, First word: Hello, Last word: Hello, Shortest word: Hello, Longest word: Hello
3) Error: "    " -> (No output since there are no words)
"""

"""
    Problem 5: Password strength classifier
    Description: Classifies a password as "weak", "medium" or "strong" according 
    to minimum rules (you can refine them, but document them in the comments).
    Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).
"""

password = input("Enter a password: ")
password = password.strip()
length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)
if length < 8 or password.islower():
    print("Password strength: weak")
elif length >= 8 and (has_upper or has_digit):
    if has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")

"""
    Test cases:
1) Normal: "Password123!" -> Password strength: strong
2) Border: "password" -> Password strength: weak   
3) Error: "Pass12" -> Password strength: medium
"""

"""
    Problem 6: Product label formatter (fixed-width text)    
    Description: Given a product name and its price, generate a single-line label with the following format:
    Product: <NAME> | Price: $<PRICE>
    The complete string must be exactly 30 characters:
- If it's shorter, pad with trailing spaces.

- If it's longer, trim it down to 30 characters.
Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.

"""
product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()
try:
    price = float(price_value)
    if price < 0 or product_name == '':
        ValueError
    label = f"Product: {product_name} | Price: ${price:.2f}"
    if len(label) < 30:
        label = label.ljust(30)
    else:
        label = label[:30]
    print(f'Label: "{label}"')
except ValueError:
    print("Invalid product name or price.")

"""
    Test cases:
1) Normal: product_name = "Widget", price_value = "19.99" -> Label: "Product: Widget | Price: $19.99     "
2) Border: product_name = "SuperLongProductNameThatExceeds", price_value = "100.00" -> Label: "Product: SuperLongProductNameT"
3) Error: product_name = "", price_value = "-5" -> Invalid product name or price.
"""

"""
CONCLUSIONES:
El manejo de strings en Python permite formatear y validar datos de manera eficiente.
Conviene usar los metodos recomendados o integrados para validar, formatear y manipular cadenas de texto.
Normalizar texto (como usar strip() para eliminar espacios en blanco) asegura que las comparaciones y validaciones sean precisas, evitando errores causados por caracteres no deseados.
Al implementar validaciones claras y específicas, se asegura que los datos ingresados cumplan con los requisitos esperados antes de ser procesados. Esto previene la introducción de datos incorrectos o mal formateados que podrían causar fallos en el programa o resultados inesperados.
Aprendi que su inmutabilidad es una caracteristica clave que afecta como se manejan y manipulan las cadenas en Python pero se puede remplazar el valor original por uno nuevo y los slices es util separar en subcadenas para un orden o mayores acciones.

REFERENCIAS:
Documentación oficial de Python (Strings): https://docs.python.org/3/library/stdtypes.html#str
W3Schools - Python Strings: https://www.w3schools.com/python/python_strings.asp
Programiz - String Methods in Python: https://www.programiz.com/python-programming/methods/string
Tutoriales de Python en “Aprende Python”: https://aprendepython.com/cursos/python-desde-cero/
Python para Todos (capítulo de cadenas) – Dr. Charles Severance: https://py4e.com/es/book.php?chapter=6
"""