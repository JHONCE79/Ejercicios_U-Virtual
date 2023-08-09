class Carta:
    PINTAS = ["Corazones", "Diamantes", "Tréboles", "Picas"]

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def mostrar_carta(self):
        print(f"Carta: {self.valor} de {self.pinta}")


valor_carta = "Rey"
pinta_carta = Carta.PINTAS[2]
carta = Carta(valor_carta, pinta_carta)
carta.mostrar_carta()


