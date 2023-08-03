def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

if __name__ == "__main__":
    lista = [1, 2, 2, 3, 4, 4, 5]
    lista_sin_duplicados = eliminar_duplicados(lista)
    print(f"Lista original: {lista}")
    print(f"Lista sin duplicados: {lista_sin_duplicados}")
