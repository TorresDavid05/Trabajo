def determinar_mayor_o_menor_edad(nombre, edad):
    if edad < 0 or edad > 100:
        return "Por favor, ingrese una edad válida (entre 0 y 100 años)."
    elif edad >= 18:
        return f"Hola {nombre}, usted es mayor de edad."
    else:
        return f"Hola {nombre}, usted es menor de edad."

if __name__ == "__main__":
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))

        resultado = determinar_mayor_o_menor_edad(nombre, edad)

        print(resultado)
    except ValueError:
        print("Por favor, ingrese una edad válida (número entero).")
