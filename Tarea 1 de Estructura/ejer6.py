            #ESTADISTICA DE TEMPERATURA
#Bosquejo
    #registrar_multiples(20, 25, 18, 30)
    #  lista = [20, 25, 18, 30]

    #minima():
    #  el más chico entre 20, 25, 18, 30 → 18

    #maxima():
    #  el más grande entre 20, 25, 18, 30 → 30

    #promedio():
    #  (20 + 25 + 18 + 30) / 4 = 93 / 4 = 23.25

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())
print(gt.minima())
print(gt.maxima())