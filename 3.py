def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

if __name__ == "__main__":
    lista_muestra = [8, 2, 3, 0, 7]
    resultado = sumar_lista(lista_muestra)
    print(f"La suma de los números en la lista es: {resultado}")

