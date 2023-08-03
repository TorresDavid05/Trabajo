if __name__ == "__main__":
    try:
        numero = float(input("Ingrese un número: "))
        cuadrado = numero ** 2
        print("El cuadrado de", numero, "es:", cuadrado)
    except ValueError:
        print("Por favor, ingrese un número válido.")
