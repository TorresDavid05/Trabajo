def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Verificar si la cadena invertida es igual a la cadena original
    return cadena == cadena[::-1]

if __name__ == "__main__":
    cadena_ejemplo = "Anita lava la tina"
    if es_palindromo(cadena_ejemplo):
        print(f'"{cadena_ejemplo}" es un palíndromo.')
    else:
        print(f'"{cadena_ejemplo}" NO es un palíndromo.')
