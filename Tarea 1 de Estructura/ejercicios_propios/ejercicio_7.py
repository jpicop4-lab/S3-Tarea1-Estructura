class GestorEmpleados:

    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, nombre, salario):
        self.empleados[nombre] = salario

    def empleados_bien_pagados (self, salario_minimo):
        bien_pagados =[]

        for nombre, salario in self.empleados.items():
            if salario >= salario_minimo:
                bien_pagados.append(nombre)
        return bien_pagados

    def salario_promedio(self):
        return sum(self.empleados.values()) / len(self.empleados)

ge = GestorEmpleados()

ge.agregar_empleado("Luis", 1200)
ge.agregar_empleado("Eva", 800)

print(ge.empleados_bien_pagados(100))
print(ge.salario_promedio())
    