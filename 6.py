import random

def lanzamientos_de_dado(n):
    contador_tres = 0

    for _ in range(n):
        resultado_lanzamiento = random.randint(1, 6)
        print(f"Lanzamiento: {resultado_lanzamiento}")

        if resultado_lanzamiento == 3:
            contador_tres += 1

    return contador_tres

if __name__ == "__main__":
    try:
        n_lanzamientos = int(input("Ingrese el número de lanzamientos del dado: "))
        if n_lanzamientos <= 0:
            print("El número de lanzamientos debe ser mayor a cero.")
        else:
            veces_tres = lanzamientos_de_dado(n_lanzamientos)
            print(f"Se obtuvo el número 3 en {veces_tres} lanzamientos.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
