def obtener_numero_mas_pequeno(lista):
    if len(lista) == 0:
        return None
    return min(lista)

if __name__ == "__main__":
    lista = [5, 2, 8, 1, 9]
    numero_mas_pequeno = obtener_numero_mas_pequeno(lista)
    
    if numero_mas_pequeno is not None:
        print(f"El número más pequeño de la lista es: {numero_mas_pequeno}")
    else:
        print("La lista está vacía, no se puede obtener el número más pequeño.")
