def calcular_factorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))

        factorial = calcular_factorial(numero)

        if factorial is not None:
            print(f"El factorial de {numero} es: {factorial}")
        else:
            print("El factorial no está definido para números negativos.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
