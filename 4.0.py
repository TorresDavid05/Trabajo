def encontrar_mayor_menor(numero1, numero2):
    if numero1 > numero2:
        return numero1, numero2
    else:
        return numero2, numero1

if __name__ == "__main__":
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        mayor, menor = encontrar_mayor_menor(numero1, numero2)

        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
