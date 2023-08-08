class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def perimetro(self):
        longitud = abs(self.p1.x - self.p2.x)
        ancho = abs(self.p1.y - self.p2.y)
        return 2 * (longitud + ancho)

    def area(self):
        longitud = abs(self.p1.x - self.p2.x)
        ancho = abs(self.p1.y - self.p2.y)
        return longitud * ancho

    def es_cuadrado(self):
        longitud = abs(self.p1.x - self.p2.x)
        ancho = abs(self.p1.y - self.p2.y)
        return longitud == ancho

p1 = Punto(4, 4)
p2 = Punto(4, 4)

mi_rectangulo = Rectangulo(p1, p2)

p = mi_rectangulo.perimetro()
print(f"El perímetro del rectángulo es {p} unidades.")

a = mi_rectangulo.area()
print(f"El área del rectángulo es {a} unidades cuadradas.")

c = mi_rectangulo.es_cuadrado()
print(f"El rectángulo es un cuadrado: {c}.")
