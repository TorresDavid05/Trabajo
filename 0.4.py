def calcular_edad(anio_actual, anio_nacimiento):
    edad = anio_actual - anio_nacimiento
    return edad

if __name__ == "__main__":
    try:
        anio_actual = int(input("Ingrese el año actual: "))
        anio_nacimiento = int(input("Ingrese su año de nacimiento: "))

        edad = calcular_edad(anio_actual, anio_nacimiento)

        if edad >= 0:
            print("Su edad es:", edad, "años.")
        else:
            print("Por favor, ingrese un año de nacimiento válido.")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
