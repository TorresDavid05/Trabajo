def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

if __name__ == "__main__":
    try:
        numeros = []
        for i in range(5):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

        promedio = calcular_promedio(numeros)

        print("El promedio de los números ingresados es:", promedio)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
