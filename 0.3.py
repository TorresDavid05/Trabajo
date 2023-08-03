def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

if __name__ == "__main__":
    try:
        velocidad_km_h = float(input("Ingrese la velocidad en kilómetros por hora (Km/h): "))
        tiempo_h = float(input("Ingrese el tiempo en horas (h): "))

        distancia_km = calcular_distancia(velocidad_km_h, tiempo_h)

        print("La distancia recorrida es:", distancia_km, "Km")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
