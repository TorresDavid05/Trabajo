def contar_letras_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    for letra in cadena:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1

    return mayusculas, minusculas

if __name__ == "__main__":
    cadena_ejemplo = "Hola Mundo"
    mayusculas, minusculas = contar_letras_mayusculas_minusculas(cadena_ejemplo)

    print(f"Número de letras mayúsculas: {mayusculas}")
    print(f"Número de letras minúsculas: {minusculas}")
