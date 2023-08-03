def contar_votos(n):
    candidatos = {1: "Candidato 1", 2: "Candidato 2", 3: "Candidato 3"}
    votos_candidatos = {candidato: 0 for candidato in candidatos.values()}
    votos_blancos = 0
    votos_nulos = 0

    for _ in range(n):
        voto = int(input("Ingrese el voto (1, 2, 3 o 0 para voto en blanco): "))
        if voto == 1 or voto == 2 or voto == 3:
            votos_candidatos[candidatos[voto]] += 1
        elif voto == 0:
            votos_blancos += 1
        else:
            votos_nulos += 1

    return votos_candidatos, votos_blancos, votos_nulos

if __name__ == "__main__":
    try:
        n_personas = int(input("Ingrese el número de personas que votaron: "))
        if n_personas <= 0:
            print("El número de personas debe ser mayor a cero.")
        else:
            votos_candidatos, votos_blancos, votos_nulos = contar_votos(n_personas)
            print(f"Total de votos por candidato:")
            for candidato, votos in votos_candidatos.items():
                print(f"{candidato}: {votos} votos")
            print(f"Total de votos en blanco: {votos_blancos} votos")
            print(f"Total de votos nulos: {votos_nulos} votos")
    except ValueError:
        print("Por favor, ingrese un número válido.")
