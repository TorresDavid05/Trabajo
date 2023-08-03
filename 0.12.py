def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        cateto1 = float(input("Ingrese la longitud del primer cateto: "))
        cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

        hipotenusa = calcular_hipotenusa(cateto1, cateto2)

        print("La longitud de la hipotenusa es:", hipotenusa)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
