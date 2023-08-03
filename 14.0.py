def calcular_pulsaciones(edad, genero):
    if genero == 1:
        pulsaciones = (220 - edad) / 10
    elif genero == 2:
        pulsaciones = (210 - edad) / 10
    else:
        pulsaciones = None
    return pulsaciones

if __name__ == "__main__":
    try:
        edad = int(input("Ingrese la edad: "))
        genero = int(input("Ingrese el género (1 para femenino, 2 para masculino): "))

        if edad <= 0 or (genero != 1 and genero != 2):
            print("Por favor, ingrese valores válidos (edad mayor que 0 y género 1 o 2).")
        else:
            pulsaciones = calcular_pulsaciones(edad, genero)
            if pulsaciones is not None:
                print(f"El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: {pulsaciones:.2f}")
            else:
                print("Por favor, ingrese un género válido (1 para femenino, 2 para masculino).")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
