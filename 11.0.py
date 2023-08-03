def calcular_precio_pizza(tamano):
    if tamano == 1:
        precio = 15000
    elif tamano == 2:
        precio = 24000
    elif tamano == 3:
        precio = 36000
    else:
        precio = None

    return precio

if __name__ == "__main__":
    try:
        print("Tamaños de pizza:")
        print("1. Pequeña - $15000")
        print("2. Mediana - $24000")
        print("3. Grande - $36000")

        tamano_elegido = int(input("Ingrese el número correspondiente al tamaño de la pizza que desea: "))

        precio_pizza = calcular_precio_pizza(tamano_elegido)

        if precio_pizza is not None:
            print(f"El precio a pagar por la pizza es: ${precio_pizza}")
        else:
            print("Por favor, ingrese un número válido correspondiente al tamaño de la pizza.")
    except ValueError:
        print("Por favor, ingrese un número válido correspondiente al tamaño de la pizza.")
