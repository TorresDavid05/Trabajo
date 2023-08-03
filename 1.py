def sumar_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    resultado = sumar_lista(lista)
    print(f"La suma de los elementos de la lista es: {resultado}")
