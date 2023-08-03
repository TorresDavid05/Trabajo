def calcular_valor_total(cantidad, precio_unitario_original):
    if cantidad <= 5:
        precio_unitario_con_descuento = precio_unitario_original
    elif cantidad < 10:
        descuento_porcentaje = 5
    else:
        descuento_porcentaje = 8

    if cantidad >= 6:
        descuento = (precio_unitario_original * descuento_porcentaje) / 100
        precio_unitario_con_descuento = precio_unitario_original - descuento

    valor_total = cantidad * precio_unitario_con_descuento
    return valor_total

if __name__ == "__main__":
    try:
        cantidad = int(input("Ingrese la cantidad de artículos: "))
        precio_unitario_original = float(input("Ingrese el precio unitario original: "))

        if cantidad < 1 or precio_unitario_original < 0:
            print("Por favor, ingrese valores válidos (cantidad mayor o igual a 1 y precio unitario mayor o igual a 0).")
        else:
            valor_total = calcular_valor_total(cantidad, precio_unitario_original)
            print(f"El valor total a pagar es: ${valor_total:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
