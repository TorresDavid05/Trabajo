def encontrar_mayor_valor(datos):
    mayor_valor = float('-inf')
    for dato in datos:
        if dato > mayor_valor:
            mayor_valor = dato
    return mayor_valor

if __name__ == "__main__":
    try:
        # Leer los datos desde el teclado como una lista de números separados por espacios
        datos_str = input("Ingrese los datos (precios) separados por espacios: ")
        datos = [float(dato) for dato in datos_str.split()]

        if not datos:
            print("Por favor, ingrese al menos un dato.")
        else:
            mayor_valor = encontrar_mayor_valor(datos)
            print(f"El mayor valor es: {mayor_valor}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
