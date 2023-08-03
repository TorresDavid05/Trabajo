def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def determinar_estado_imc(imc):
    if imc < 18.5:
        return "Desnutrido"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad grado 1"
    elif 35 <= imc < 40:
        return "Obesidad grado 2"
    else:
        return "Obesidad grado 3"

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese el peso en Kg: "))
        estatura = float(input("Ingrese la estatura en metros: "))

        if peso <= 0 or estatura <= 0:
            print("Por favor, ingrese valores válidos (peso y estatura deben ser mayores que 0).")
        else:
            imc = calcular_imc(peso, estatura)
            estado_imc = determinar_estado_imc(imc)
            print(f"El IMC calculado es: {imc:.2f}")
            print(f"Estado según el IMC: {estado_imc}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
