def encontrar_maximo(a, b, c):
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    return maximo

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        maximo = encontrar_maximo(num1, num2, num3)
        print(f"El máximo de los tres números es: {maximo}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
