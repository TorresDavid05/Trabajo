import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    try:
        print("Elija la figura geométrica para calcular el área:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")

        opcion = int(input("Ingrese el número correspondiente a la figura: "))

        if opcion == 1:
            lado = float(input("Ingrese el valor del lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
        elif opcion == 2:
            base = float(input("Ingrese el valor de la base del rectángulo: "))
            altura = float(input("Ingrese el valor de la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
        elif opcion == 3:
            base = float(input("Ingrese el valor de la base del triángulo: "))
            altura = float(input("Ingrese el valor de la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
        elif opcion == 4:
            radio = float(input("Ingrese el valor del radio del círculo: "))
            area = calcular_area_circulo(radio)
        else:
            print("Opción inválida. Por favor, seleccione una figura válida.")
            area = None

        if area is not None:
            print(f"El área de la figura es: {area:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
