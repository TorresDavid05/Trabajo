def esta_en_rango(numero, rango_inicial, rango_final):
    return rango_inicial <= numero <= rango_final

if __name__ == "__main__":
    try:
        num = float(input("Ingrese un número: "))
        rango_inicio = float(input("Ingrese el límite inferior del rango: "))
        rango_fin = float(input("Ingrese el límite superior del rango: "))

        if esta_en_rango(num, rango_inicio, rango_fin):
            print(f"El número {num} está dentro del rango [{rango_inicio}, {rango_fin}]")
        else:
            print(f"El número {num} está fuera del rango [{rango_inicio}, {rango_fin}]")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
