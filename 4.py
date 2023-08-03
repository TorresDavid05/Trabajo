def multiplicar_lista(lista):
    multiplicacion = 1
    for numero in lista:
        multiplicacion *= numero
    return multiplicacion

if __name__ == "__main__":
    lista_muestra = [8, 2, 3, -1, 7]
    resultado = multiplicar_lista(lista_muestra)
    print(f"La multiplicación de los números en la lista es: {resultado}")
