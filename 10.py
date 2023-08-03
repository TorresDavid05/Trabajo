def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(num):
            print(f"{num} es un número primo.")
        else:
            print(f"{num} NO es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

