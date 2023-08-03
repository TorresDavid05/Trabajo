if __name__ == "__main__":
    suma = 0
    for i in range(1, 21):
        suma += i

    print(f"La suma de los primeros 20 números naturales es: {suma}")
    if suma == 210:
        print("El total es 210.")
    else:
        print("El total no es igual a 210.")
