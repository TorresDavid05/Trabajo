class Car:
    def __init__(self, marca, modelo, year, color, capacidad_de_conbustible, capacidad_actual_gasolina):
        self.marca = marca
        self.modelo = modelo
        '''año de fabricación del carro'''
        self.year = year
        self.color = color
        self.capacidad_de_conbustible = capacidad_de_conbustible
        self.capacidad_actual_gasolina = capacidad_actual_gasolina

    def start(self):
        print("El carro está arrancando.")

    def stop(self):
        print("El carro se detuvo.")

    def refuel(self, amount):
        if amount <= 0:
            print("La cantidad de combustible debe ser mayor que cero.")
        elif self.capacidad_actual_gasolina + amount > self.capacidad_de_conbustible:
            print("El tanque no puede contener tanta cantidad de combustible.")
        else:
            self.capacidad_actual_gasolina += amount
            print(f"Se ha añadido {amount} litros de combustible. Ahora tienes {self.capacidad_actual_gasolina} litros en el tanque.")

    def drive(self, distance):
        if distance <= 0:
            print("La distancia debe ser mayor que cero.")
        elif distance * 10 > self.capacidad_actual_gasolina:
            print("No tienes suficiente combustible para recorrer esa distancia.")
        else:
            self.capacidad_actual_gasolina -= distance * 10
            print(f"Has recorrido {distance} kilómetros. Ahora te quedan {self.capacidad_actual_gasolina} litros de combustible.")

# Ejemplo de uso:
my_car = Car("Toyota", "Corolla", 2022, "Blue", 50, 20)

my_car.start()
my_car.drive(30)
my_car.refuel(10)
my_car.drive(20)
my_car.stop()
