if __name__ == "__main__":
    n = 5  # Tamaño de la letra Z

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("*", end=" ")
            elif i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
