            # CALCULADOR DE DISTANCIA
# Bosquejo

    # Puntos a cargar:
    # p1 = (0, 0)
    # p2 = (3, 4)

    # Fórmula de distancia euclidiana:
    #
    # √((x2 - x1)² + (y2 - y1)²)
    #
    # √((3 - 0)² + (4 - 0)²)
    # √(3² + 4²)
    # √(9 + 16)
    # √25
    # 5.0

    # Guardar distancia:
    # distancias = [5.0]


    # Buscar punto más cercano:
    #
    # Referencia: (0, 0)
    # Puntos:
    # (3, 4)
    # (1, 1)
    # (5, 2)

    # Distancias:
    # (3, 4) → 5.0
    # (1, 1) → 1.41
    # (5, 2) → 5.38

    # Menor distancia → 1.41
    # Punto más cercano → (1, 1)

    # Lista de distancias:
    # [5.0, 1.41, 5.38]

import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        menor_distancia = float("inf")

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto

        return punto_cercano


# Programa principal
cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

punto = cd.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (5, 2)
)

print(f"Punto más cercano: {punto}")
print(f"Distancias calculadas: {cd.distancias}")