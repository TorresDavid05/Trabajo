def calcular_promedio(notas):
    total_notas = sum(notas)
    promedio = total_notas / len(notas)
    return promedio

def determinar_aprobacion(promedio):
    if promedio >= 3.0:
        return "Aprobó"
    else:
        return "No aprobó"

if __name__ == "__main__":
    try:
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i + 1} (0.0 a 5.0): "))
            if nota < 0.0 or nota > 5.0:
                print("Por favor, ingrese una nota válida (entre 0.0 y 5.0).")
                exit()
            notas.append(nota)

        promedio = calcular_promedio(notas)
        resultado_aprobacion = determinar_aprobacion(promedio)

        print(f"El promedio del estudiante es: {promedio:.2f}")
        print(f"El estudiante {resultado_aprobacion} la asignatura.")
    except ValueError:
        print("Por favor, ingrese notas válidas (números entre 0.0 y 5.0).")
