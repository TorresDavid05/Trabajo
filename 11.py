def imprimir_numeros_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

if __name__ == "__main__":
    lista_determinada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Números pares de la lista:")
    imprimir_numeros_pares(lista_determinada)
