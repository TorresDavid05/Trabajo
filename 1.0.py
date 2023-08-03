def determinar_par_impar_cero(numero):
    if numero == 0:
        return "Cero"
    elif numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número: "))

        resultado = determinar_par_impar_cero(numero)

        print(f"El número ingresado es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
