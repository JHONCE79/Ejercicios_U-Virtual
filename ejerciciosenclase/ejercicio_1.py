class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def mostrar(self):
        print(f"La velocidad máxima del vehículo es {self.velocidad_maxima} km/h y el kilometraje es {self.kilometraje} km.")

mi_vehiculo = Vehiculo(120, 3200)

mi_vehiculo.mostrar()
