import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def contiene(self, punto):
        distancia = self.centro.calcular_distancia(punto)
        return distancia <= self.radio

c = Punto(0, 0)

mi_circulo = Circulo(c, 5)

a = mi_circulo.area()
print(f"El área del círculo es {a} unidades cuadradas.")

p = mi_circulo.perimetro()
print(f"El perímetro del círculo es {p} unidades.")

p1 = Punto(2, 9)

c1 = mi_circulo.contiene(p1)
print(f"El punto p1 pertenece al círculo: {c1}.")

p2 = Punto(7, 7)

c2 = mi_circulo.contiene(p2)
print(f"El punto p2 pertenece al círculo: {c2}.")
#
