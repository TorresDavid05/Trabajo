def palabras_mas_largas_que_n(lista_palabras, n):
    palabras_mas_largas = [palabra for palabra in lista_palabras if len(palabra) > n]
    return palabras_mas_largas

if __name__ == "__main__":
    lista_palabras = ["python", "programa", "ejemplo", "largo", "lista", "corto"]
    n = 5
    palabras_mas_largas = palabras_mas_largas_que_n(lista_palabras, n)
    print(f"Lista de palabras: {lista_palabras}")
    print(f"Palabras más largas que {n}: {palabras_mas_largas}")
