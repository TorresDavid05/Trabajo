class Ave:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("¡Chirp chirp!")

class Aguila(Ave):
    def __init__(self, nombre, edad, envergadura):
        super().__init__(nombre, edad)
        self.envergadura = envergadura

    def hacer_sonido(self):
        print("¡Creee!")

class Pinguino(Ave):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        print("¡Ping ping!")

# Ejemplo de uso:
ave_generico = Ave("Pájaro", 2)
print(f"{ave_generico.nombre} tiene {ave_generico.edad} años.")
ave_generico.hacer_sonido()

aguila1 = Aguila("Águila Real", 5, 200)
print(f"{aguila1.nombre} tiene {aguila1.edad} años y una envergadura de {aguila1.envergadura} cm.")
aguila1.hacer_sonido()

pinguino1 = Pinguino("Pingui", 3, "Blanco y negro")
print(f"{pinguino1.nombre} tiene {pinguino1.edad} años y es de color {pinguino1.color}.")
pinguino1.hacer_sonido()
