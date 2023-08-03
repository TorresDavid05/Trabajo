import datetime

def verificar_pico_placa(placa, fecha):
    # Diccionario con las restricciones de pico y placa para cada día de la semana
    restricciones = {
        0: [1, 2],  # Lunes: placas terminadas en 1 y 2
        1: [3, 4],  # Martes: placas terminadas en 3 y 4
        2: [5, 6],  # Miércoles: placas terminadas en 5 y 6
        3: [7, 8],  # Jueves: placas terminadas en 7 y 8
        4: [9, 0]   # Viernes: placas terminadas en 9 y 0
    }

    # Obtener el último dígito de la placa
    ultimo_digito = int(placa[-1])

    # Obtener el día de la semana (0 = lunes, 1 = martes, ..., 6 = domingo)
    dia_semana = fecha.weekday()

    # Verificar si la placa tiene restricción de pico y placa ese día
    if ultimo_digito in restricciones[dia_semana]:
        return True  # Tiene restricción
    else:
        return False  # No tiene restricción

# Ejemplo de uso:
placa = input("Ingrese el número de placa (sin espacios ni guiones): ")
fecha = datetime.datetime.now()

if verificar_pico_placa(placa, fecha):
    print("Su vehículo tiene restricción de pico y placa hoy.")
else:
    print("Su vehículo NO tiene restricción de pico y placa hoy.")