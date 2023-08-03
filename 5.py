if __name__ == "__main__":
    try:
        numero_entero = int(input("Ingrese el número entero para mostrar su tabla de multiplicar: "))

        print(f"Tabla de multiplicar del {numero_entero}:")
        for i in range(1, 11):
            resultado = numero_entero * i
            print(f"{numero_entero} x {i} = {resultado}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
