def convertir_distancia(distancia_metros):
    distancia_km = distancia_metros / 1000
    distancia_cm = distancia_metros * 100
    distancia_mm = distancia_metros * 1000
    return distancia_km, distancia_cm, distancia_mm

if __name__ == "__main__":
    try:
        distancia_metros = float(input("Ingrese la distancia en metros: "))

        distancia_km, distancia_cm, distancia_mm = convertir_distancia(distancia_metros)

        print(f"La distancia en kilómetros es: {distancia_km} km.")
        print(f"La distancia en centímetros es: {distancia_cm} cm.")
        print(f"La distancia en milímetros es: {distancia_mm} mm.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
