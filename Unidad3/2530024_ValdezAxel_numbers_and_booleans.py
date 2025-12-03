"""
    Portada del archivo
    Nombre: Axel Baruc Valdez Ramirez
    Matricula: 2530024
    Grupo: IM 1-2

    Resumen ejecutivo:
    Los tipos **int** y **float** en Python representan números, pero los primeros manejan 
    valores enteros mientras que los segundos permiten decimales, útiles para cálculos más 
    precisos. Un **booleano** es un valor lógico que solo puede ser **True** o **False**, 
    normalmente generado al evaluar comparaciones como `>`, `<`, `==` o expresiones lógicas. 
    Validar **rangos** y evitar **división entre cero** previene errores de ejecución y 
    asegura que los programas operen con datos seguros y consistentes. 
    El documento incluirá la descripción de cada problema analizado, el diseño de entradas 
    y salidas, las validaciones implementadas y la forma en que se aplican enteros, flotantes 
    y booleanos para controlar decisiones dentro del programa.

"""

"""
    Problem 1: Temperature converter and range flag
    Descripción:
    Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, 
    determina un valor booleano is_high_temperature que sea true si la 
    temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.
    
    Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
"""

temp_c_input = input("Enter temperature in Celsius: ").strip()
try:
    temp_c = float(temp_c_input)
    temp_f = (temp_c * 9/5) + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        raise ValueError("Temperature in Kelvin cannot be negative.")
    is_high_temperature = temp_c >= 30.0
    print(f"Fahrenheit: {temp_f:.2f}")
    print(f"Kelvin: {temp_k:.2f}")
    print(f"High temperature: {is_high_temperature}")
except ValueError:
    print("Invalid temperature input.")

"""
    Test cases:
1) Normal: temp_c = "25.0" -> Fahrenheit: 77.00, Kelvin: 298.15, High temperature: False
2) Border: temp_c = "30.0" -> Fahrenheit: 86.00, Kelvin: 303.15, High temperature: True
3) Error: temp_c = "-300.0" -> Invalid temperature input.
"""

"""
    Problem 2: Work hours and overtime payment

    Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de min() y max() para separar horas regulares y extra.
- Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
- Booleano: has_overtime = (hours_worked > 40)
"""
hours_worked_input = input("Enter hours worked: ").strip()
hourly_rate_input = input("Enter hourly rate: ").strip()
try:
    hours_worked = float(hours_worked_input)
    hourly_rate = float(hourly_rate_input)
    if hours_worked < 0 or hourly_rate <= 0:
        raise ValueError("Invalid input.")
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40
    print(f"Regular pay: {regular_pay:.2f}")
    print(f"Overtime pay: {overtime_pay:.2f}")
    print(f"Total pay: {total_pay:.2f}")
    print(f"Has overtime: {has_overtime}")
except ValueError:
    print("Error: invalid input.")

"""
    Test cases:
1) Normal: hours_worked = "45", hourly_rate = "20" -> Regular
pay: 800.00, Overtime pay: 150.00, Total pay: 950.00, Has overtime: True
2) Border: hours_worked = "40", hourly_rate = "15" -> Regular
pay: 600.00, Overtime pay: 0.00, Total pay: 600.00, Has overtime: False
3) Error: hours_worked = "-5", hourly_rate = "10" -> Error: invalid input.
"""

"""
Problem 3: Discount eligibility with booleans
Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Conversión a bool por comparación de strings.
- Booleanos: discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
- Cálculo: final_total = purchase_total * 0.9 si discount_eligible es true, si no, el mismo purchase_total.
"""

purchase_total_input = input("Enter purchase total: ").strip()
is_student_text = input("Is the customer a student? (YES/NO): ").strip
is_senior_text = input("Is the customer a senior? (YES/NO): ").strip()
try:
    purchase_total = float(purchase_total_input)
    if purchase_total < 0.0:
        raise ValueError("Invalid input.")
    is_student_text = is_student_text.upper()
    is_senior_text = is_senior_text.upper()
    if is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        raise ValueError("Invalid input.")
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total
    print(f"Discount eligible: {discount_eligible}")
    print(f"Final total: {final_total:.2f}")
except ValueError:
    print("Error: invalid input.")

"""
    Test cases:
1) Normal: purchase_total = "1200.0", is_student_text = "NO
", is_senior_text = "NO" -> Discount eligible: True, Final total: 1080.00
2) Border: purchase_total = "800.0", is_student_text = "YES",
    is_senior_text = "NO" -> Discount eligible: True, Final total: 720.00
3) Error: purchase_total = "-50.0", is_student_text = "MAYBE",
    is_senior_text = "NO" -> Error: invalid input.
"""

"""
    Problem 4: Basic statistics of three integers
    Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano all_even que indique si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Operaciones clave sugeridas:
- sum_value = n1 + n2 + n3
- average_value = sum_value / 3
- max(), min()
- all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

"""
n1_input = input("Enter first integer: ").strip()
n2_input = input("Enter second integer: ").strip()
n3_input = input("Enter third integer: ").strip()
try:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
except ValueError:
    print("Invalid integer input.")

"""
    Test cases:
1) Normal: n1 = "4", n2 = "8", n3 = "12" -> Sum: 24, Average: 8.00, Max: 12, Min: 4, All even: True
2) Border: n1 = "1", n2 = "2", n3 = "3" -> Sum: 6, Average: 2.00, Max: 3, Min: 1, All even: False
3) Error: n1 = "5", n2 = "abc", n3 = "10" -> Invalid integer input.
"""

"""
    Problem 5: Loan eligibility (income and debt ratio)
    Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de deuda relativa: debt_ratio = monthly_debt / monthly_income
- Booleano: eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
"""
monthly_income_input = input("Enter monthly income: ").strip()
monthly_debt_input = input("Enter monthly debt: ").strip()
credit_score_input = input("Enter credit score: ").strip()
try:
    monthly_income = float(monthly_income_input)
    monthly_debt = float(monthly_debt_input)
    credit_score = int(credit_score_input)
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        raise ValueError("Invalid input.")
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
    print(f"Debt ratio: {debt_ratio:.2f}")
    print(f"Eligible: {eligible}")
except ValueError:
    print("Error: invalid input.")

"""
    Test cases:
1) Normal: monthly_income = "10000.0", monthly_debt = "3000.0", credit_score = "700" -> Debt ratio: 0.30, Eligible: True
2) Border: monthly_income = "8000.0", monthly_debt = "3200.0", credit_score = "650" -> Debt ratio: 0.40, Eligible: True
3) Error: monthly_income = "0.0", monthly_debt = "-500. 0", credit_score = "-100" -> Error: invalid input.
"""

"""
    Problem 6: Body Mass Index (BMI) and category flag
    Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de bmi como float.
- Uso de round(bmi, 2) para mostrar 2 decimales.
- Evaluación de rangos con condiciones encadenadas.


"""
weight_kg_input = input("Enter weight in kg: ").strip()
height_m_input = input("Enter height in meters: ").strip()
try:
    weight_kg = float(weight_kg_input)
    height_m = float(height_m_input)
    if weight_kg <= 0.0 or height_m <= 0.0:
        raise ValueError("Invalid input.")
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0
    print(f"BMI: {bmi_rounded:.2f}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight}")
except ValueError:
    print("Error: invalid input.")

"""
    Test cases:
1) Normal: weight_kg = "70.0", height_m = "1.75" -> BMI: 22.86, Underweight: False, Normal: True, Overweight: False
2) Border: weight_kg = "50.0", height_m = "1.80" -> BMI: 15.43, Underweight: True, Normal: False, Overweight: False
3) Error: weight_kg = "-60.0", height_m = "0.0" -> Error: invalid input.
"""

"""
    CONCLUSIONES:
    Los numeros enteros y flotantes son fundamentales para distintas operaciones matematicas 
    y logicas en Python. Nos permiten ralizar calculos precisos y la toma de decisiones porque 
    nos generan booleanos al evaluar condiciones.
    Es importante validar rangos para evitar errores de ejecucion y asegurar que los datos
    y evitar la divisones de cero porque es indeterminado osea incalculable entonces 
    el programa puede fallar.
    Aprendi que las conbinaciones de los operadores logicos con los booleanos son
    muy utiles para tomar decisiones complejas en los programas para un gran aplio espacio de validacion.


    REFERENCIAS:
    # REFERENCIAS
1.  Python Documentation - Built-in Types: Numeric Types (int, float, complex).
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2. Python Documentation - Boolean Type (bool).
    https://docs.python.org/3/library/stdtypes.html#boolean-values

3. Tutorial oficial de Python: Operadores aritméticos, relacionales y lógicos.
    https://docs.python.org/3/reference/expressions.html

4. Cormen, Leiserson, Rivest & Stein - "Introduction to Algorithms" (Capítulos de fundamentos).

5. Apuntes de programación básica y validación de datos numéricos de cursos introductorios 
    (por ejemplo, materiales docentes de universidades como MIT OCW o UNAM).

6. Sweigart, Al - “Automate the Boring Stuff with Python” (capítulos de tipos de datos y control de flujo).

URL DEL REPOSITORIO EN GITHUB:
https://github.com/2530024/Metodologias-de-la-Programacion
"""