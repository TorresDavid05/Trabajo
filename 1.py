class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Ejemplo de uso:
rectangle1 = Rectangle(5, 10)
area1 = rectangle1.calculate_area()
print("El área del rectángulo 1 es:", area1)

rectangle2 = Rectangle(7, 3)
area2 = rectangle2.calculate_area()
print("El área del rectángulo 2 es:", area2)
