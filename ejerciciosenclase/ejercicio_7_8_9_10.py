class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo balance: {self.balance}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo balance: {self.balance}")
        else:
            print("Fondos insuficientes o cantidad inválida para retiro.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Cuota de manejo del 2% aplicada. Nuevo balance: {self.balance}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")


cuenta = CuentaBancaria("123456789", ["Juan", "María"], 1000)
cuenta.mostrar_detalles()

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()

cuenta.mostrar_detalles()

