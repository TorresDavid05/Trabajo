def calcular_salario(salario_diario, dias_trabajados):
    salario_bruto = salario_diario * dias_trabajados
    descuento_pension = salario_bruto * 0.10
    descuento_salud = salario_bruto * 0.15
    salario_neto = salario_bruto - descuento_pension - descuento_salud
    return salario_neto

if __name__ == "__main__":
    try:
        salario_diario = float(input("Ingrese el salario diario del empleado: "))
        dias_trabajados = int(input("Ingrese el número de días trabajados: "))

        salario_total = calcular_salario(salario_diario, dias_trabajados)

        print("El salario total a pagar al empleado es:", salario_total)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
