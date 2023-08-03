def obtener_digitos_binarios(numero):
    digitos_binarios = []
    while numero > 0:
        residuo = numero % 2
        digitos_binarios.insert(0, residuo)
        numero //= 2
    return digitos_binarios

if __name__ == "__main__":
    try:
        num_decimal = int(input("Ingrese un número entero decimal: "))
        digitos_binarios = obtener_digitos_binarios(num_decimal)
        print(f"El equivalente binario de {num_decimal} es: {''.join(map(str, digitos_binarios))}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
