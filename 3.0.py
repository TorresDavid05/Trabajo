def determinar_signo(numero):
    if numero == 0:
        return "Cero"
    elif numero > 0:
        return "Positivo"
    else:
        return "Negativo"

if __name__ == "__main__":
    try:
        numero = float(input("Ingrese un número: "))

        resultado = determinar_signo(numero)

        print(f"El número ingresado es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
