if __name__ == "__main__":
    try:
        numeros = []
        for i in range(3):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

        numeros_ascendente = sorted(numeros)
        numeros_descendente = sorted(numeros, reverse=True)

        print("Números en orden ascendente:", numeros_ascendente)
        print("Números en orden descendente:", numeros_descendente)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
