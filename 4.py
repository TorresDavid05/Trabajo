def mostrar_semanas_por_mes():
    meses = {
        "Enero": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Febrero": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Marzo": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Abril": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Mayo": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Junio": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Julio": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Agosto": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Septiembre": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Octubre": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Noviembre": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Diciembre": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
    }

    for mes, semanas in meses.items():
        print(f"{mes}:")
        for semana in semanas:
            print(f" - {semana}")

if __name__ == "__main__":
    mostrar_semanas_por_mes()
