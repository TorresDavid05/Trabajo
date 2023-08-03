def multiplicar_lista(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

if __name__ == "__main__":
    lista = [2, 3, 4, 5]
    resultado = multiplicar_lista(lista)
    print(f"El resultado de multiplicar los elementos de la lista es: {resultado}")
