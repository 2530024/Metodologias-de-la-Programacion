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