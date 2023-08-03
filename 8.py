if __name__ == "__main__":
    num = 1
    n = 4  # Número de filas de la pirámide

    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
