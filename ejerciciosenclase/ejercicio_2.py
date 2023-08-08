class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        return ((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2) ** 0.5

    def mostrar(self):
        print(f"El punto es ({self.x}, {self.y}).")

p1 = Punto(35, 42)
p2 = Punto(63, 82)

d = p1.distancia(p2)
print(f"La distancia entre los puntos es {d} unidades.")

p1.mostrar()
p2.mostrar()

