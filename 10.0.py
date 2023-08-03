def calcular_valor_total(llantas_compradas):
    if llantas_compradas < 6:
        precio_unitario = 240000
    elif llantas_compradas <= 7:
        precio_unitario = 221000
    else:
        precio_unitario = 180000

    valor_total = llantas_compradas * precio_unitario
    return valor_total

if __name__ == "__main__":
    try:
        llantas_compradas = int(input("Ingrese el número de llantas que desea comprar: "))

        if llantas_compradas < 1:
            print("Por favor, ingrese un número de llantas válido (mayor o igual a 1).")
        else:
            valor_total = calcular_valor_total(llantas_compradas)
            print(f"El valor total a pagar es: ${valor_total}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
