class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"El punto es ({self.x}, {self.y}).")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print(f"El punto se ha movido a ({self.x}, {self.y}).")

    def calcular_distancia(self, otro):
        return ((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2) ** 0.5
p1 = Punto(12, 27)
p2 = Punto(36, 48)

p1.mostrar()
p2.mostrar()

p1.mover(27, 95)

d = p1.calcular_distancia(p2)
print(f"La distancia entre los puntos es {d} unidades.")

