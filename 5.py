def invertir_cadena(cadena):
    return cadena[::-1]

if __name__ == "__main__":
    cadena_ejemplo = "1234abcd"
    resultado = invertir_cadena(cadena_ejemplo)
    print(f"El resultado de invertir la cadena es: {resultado}")
