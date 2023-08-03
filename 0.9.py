def calcular_valor_con_iva(valor_unitario, cantidad_productos):
    subtotal = valor_unitario * cantidad_productos
    iva = subtotal * 0.16
    total = subtotal + iva
    return total

if __name__ == "__main__":
    try:
        valor_unitario = float(input("Ingrese el valor unitario del producto: "))
        cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))

        valor_total = calcular_valor_con_iva(valor_unitario, cantidad_productos)

        print("El valor total a pagar (incluyendo IVA) es:", valor_total)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
