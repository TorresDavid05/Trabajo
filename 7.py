import random

def lanzamientos_hasta_cinco():
    contador_lanzamientos = 0

    while True:
        resultado_lanzamiento = random.randint(1, 6)
        contador_lanzamientos += 1
        print(f"Lanzamiento {contador_lanzamientos}: {resultado_lanzamiento}")

        if resultado_lanzamiento == 5:
            break

    return contador_lanzamientos

if __name__ == "__main__":
    lanzamientos = lanzamientos_hasta_cinco()
    print(f"Se necesitaron {lanzamientos} lanzamientos para obtener el número 5.")
