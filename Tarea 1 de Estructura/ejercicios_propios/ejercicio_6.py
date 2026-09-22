class GestorPesos:

    def __init__(self):
        self.gestor_peso =[]

    def registrar_peso(self, peso):
        self.gestor_peso.append(peso)

    def registrar_multiples(self, *pesos):
        for peso in pesos:
            self.registrar_peso(peso)

    def minimo(self):
        return min(self.gestor_peso)

    def maximo(self):
        return max(self.gestor_peso)

    def rango(self):
        return max(self.gestor_peso) - min(self.gestor_peso)

gp = GestorPesos()
gp.registrar_multiples(70, 65, 80, 75)

print(gp.gestor_peso)
print(gp.maximo())
print(gp.minimo())
print(gp.rango())