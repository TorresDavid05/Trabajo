import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Ejemplo de uso:
circle1 = Circle(5)
area1 = circle1.calculate_area()
perimeter1 = circle1.calculate_perimeter()
print("El área del círculo 1 es:", area1)
print("El perímetro del círculo 1 es:", perimeter1)

circle2 = Circle(7)
area2 = circle2.calculate_area()
perimeter2 = circle2.calculate_perimeter()
print("El área del círculo 2 es:", area2)
print("El perímetro del círculo 2 es:", perimeter2)
