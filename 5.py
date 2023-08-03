import random

def juego_adivinar_numero(rango_inicial, rango_final):
    numero_secreto = random.randint(rango_inicial, rango_final)
    intentos = 0

    print(f"¡Bienvenido al juego de adivinar el número! El número está entre {rango_inicial} y {rango_final}.")
    print("Escribe 'ayuda' si necesitas una pista.")

    while True:
        intentos += 1
        adivinanza = input("Introduce tu número: ")

        if adivinanza.lower() == "ayuda":
            if numero_secreto % 2 == 0:
                print("El número secreto es par.")
            else:
                print("El número secreto es impar.")
            continue

        try:
            numero_adivinado = int(adivinanza)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero_adivinado == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif numero_adivinado < numero_secreto:
            print("El número es más grande. Sigue intentando.")
        else:
            print("El número es más pequeño. Sigue intentando.")

if __name__ == "__main__":
    rango_inicial = 1
    rango_final = 100
    juego_adivinar_numero(rango_inicial, rango_final)
