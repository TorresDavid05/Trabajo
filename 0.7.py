def calcular_area_cuadrado(lado):
    return lado ** 2

if __name__ == "__main__":
    try:
        lado = float(input("Ingrese la longitud de un lado del cuadrado: "))

        area = calcular_area_cuadrado(lado)

        print(f"El área del cuadrado es: {area}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
