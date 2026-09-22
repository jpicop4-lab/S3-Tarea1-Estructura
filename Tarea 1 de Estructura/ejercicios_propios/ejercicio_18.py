class CalculadorManhattan:

    def __init__(self):
        self.distancias = []

    def distancia_manhattan(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = abs(x1 - x2) + abs(y1 - y2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_lejano(self, referencia, *puntos):
        punto_lejano = None
        mayor_distancia = -1

        for punto in puntos:
            distancia = self.distancia_manhattan(referencia, punto)

            if distancia > mayor_distancia:
                mayor_distancia = distancia
                punto_lejano = punto

        return punto_lejano


cm = CalculadorManhattan()

print(cm.distancia_manhattan((1, 1), (4, 5)))
print(cm.punto_mas_lejano((1, 1), (2, 2), (4, 5), (10, 1)))