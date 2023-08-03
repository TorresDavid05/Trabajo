if __name__ == "__main__":
    try:
        numeros = []
        for i in range(10):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

        suma = sum(numeros)
        promedio = suma / len(numeros)

        print(f"La suma de los números es: {suma}")
        print(f"El promedio de los números es: {promedio:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
