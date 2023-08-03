def obtener_elementos_unicos(lista):
    elementos_unicos = list(set(lista))
    return elementos_unicos

if __name__ == "__main__":
    lista_ejemplo = [1, 2, 2, 3, 3, 4, 5, 5]
    lista_unicos = obtener_elementos_unicos(lista_ejemplo)

    print(f"Lista original: {lista_ejemplo}")
    print(f"Lista con elementos únicos: {lista_unicos}")
