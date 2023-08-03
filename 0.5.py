def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100

if __name__ == "__main__":
    try:
        numero = float(input("Ingrese un número: "))
        porcentaje = 20

        resultado = calcular_porcentaje(numero, porcentaje)

        print(f"El 20% de {numero} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
