import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return 0.5 * (base_mayor + base_menor) * altura

if __name__ == "__main__":
    opciones = ["Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Rombo", "Trapecio"]

    print("Menú de opciones:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. Calcular área del {opcion}")

    try:
        seleccion = int(input("Ingrese el número de la figura cuyo área desea calcular: "))
        if seleccion < 1 or seleccion > len(opciones):
            print("Opción inválida. Por favor, seleccione una opción válida del menú.")
        else:
            if seleccion == 1:
                lado = float(input("Ingrese el valor del lado del cuadrado: "))
                area = calcular_area_cuadrado(lado)
            elif seleccion == 2:
                base = float(input("Ingrese el valor de la base del rectángulo: "))
                altura = float(input("Ingrese el valor de la altura del rectángulo: "))
                area = calcular_area_rectangulo(base, altura)
            elif seleccion == 3:
                base = float(input("Ingrese el valor de la base del triángulo: "))
                altura = float(input("Ingrese el valor de la altura del triángulo: "))
                area = calcular_area_triangulo(base, altura)
            elif seleccion == 4:
                radio = float(input("Ingrese el valor del radio del círculo: "))
                area = calcular_area_circulo(radio)
            elif seleccion == 5:
                diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
                diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))
                area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
            elif seleccion == 6:
                base_mayor = float(input("Ingrese el valor de la base mayor del trapecio: "))
                base_menor = float(input("Ingrese el valor de la base menor del trapecio: "))
                altura = float(input("Ingrese el valor de la altura del trapecio: "))
                area = calcular_area_trapecio(base_mayor, base_menor, altura)

            print(f"El área del {opciones[seleccion - 1]} es: {area:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
