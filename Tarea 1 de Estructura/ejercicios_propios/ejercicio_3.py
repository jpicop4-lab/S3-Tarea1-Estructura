class Presupuesto:

    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self,concepto,monto):
        self.gastos[concepto] = monto

    def total_gastos(self):
        return sum(self.gastos.values())

    def gastos_por_rango(self, monto_min, monto_max):
        gastos_totales =[]
        for concepto, monto in self.gastos.items():
            if monto_min <= monto <= monto_max:
                gastos_totales.append(concepto)
        return gastos_totales

p = Presupuesto()

p.agregar_gasto("luz", 30.50)
p.agregar_gasto("agua", 12.00)

print(p.total_gastos())
print(p.gastos_por_rango(10, 20))