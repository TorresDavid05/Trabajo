def calcular_factorial(numero):
    if numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número entero no negativo: "))
        resultado = calcular_factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    except ValueError as error:
        print(error)
