def calcular_raiz_cuadrada(numero, iteraciones=100):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

    aproximacion = numero
    for _ in range(iteraciones):
        aproximacion = 0.5 * (aproximacion + numero / aproximacion)

    return aproximacion

if __name__ == "__main__":
    try:
        numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        resultado = calcular_raiz_cuadrada(numero)
        print(f"La raíz cuadrada de {numero} es aproximadamente: {resultado}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Ha ocurrido un error:", e)
