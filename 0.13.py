def convertir_segundos_a_horas_minutos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return horas, minutos

if __name__ == "__main__":
    try:
        segundos = int(input("Ingrese el tiempo en segundos: "))

        horas, minutos = convertir_segundos_a_horas_minutos(segundos)

        print(f"El tiempo es: {horas} horas y {minutos} minutos.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
