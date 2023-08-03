def multiplicar_tres_numeros(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))
        resultado = multiplicar_tres_numeros(num1, num2, num3)
        print("El resultado de la multiplicación es:", resultado)
    except ValueError:
        print("Por favor, ingrese números válidos.")
