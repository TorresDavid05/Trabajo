import random

def representar_barras_asteriscos(numero_elementos, rango_min, rango_max):
    numeros_aleatorios = [random.randint(rango_min, rango_max) for _ in range(numero_elementos)]

    print("Números generados:")
    for numero in numeros_aleatorios:
        print(f"{numero}: {'*' * numero}")

if __name__ == "__main__":
    numero_elementos = 10
    rango_min = 1
    rango_max = 20
    representar_barras_asteriscos(numero_elementos, rango_min, rango_max)
