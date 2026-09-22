class Cuentas:

    def __init__(self):
        self.saldos = {}

    def depositar(self, cuenta, monto):
        if cuenta in self.saldos:
            self.saldos[cuenta] += monto
        else:
            self.saldos[cuenta] = monto

    def retirar(self, cuenta, monto):
        if cuenta in self.saldos and self.saldos[cuenta] >= monto:
            self.saldos[cuenta] -= monto
            return True

        return False

    def cuentas_saldo_bajo(self, minimo):
        resultado = []

        for cuenta, saldo in self.saldos.items():
            if saldo < minimo:
                resultado.append(cuenta)

        return resultado


cu = Cuentas()

cu.depositar("Ana", 100)

print(cu.retirar("Ana", 70))
print(cu.cuentas_saldo_bajo(50))