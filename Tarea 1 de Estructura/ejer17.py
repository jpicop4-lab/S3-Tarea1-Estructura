            # AGRUPADOR DE EDADES
# Bosquejo

    # Edades a cargar:
    # 5, 15, 30, 70

    # Clasificar cada edad:

    # ¿5?  → 5 < 13       → niño
    # ¿15? → 13 ≤ 15 < 18 → adolescente
    # ¿30? → 18 ≤ 30 < 65 → adulto
    # ¿70? → 70 ≥ 65      → mayor

    # Diccionario:
    # {
    #     "niño": [5],
    #     "adolescente": [15],
    #     "adulto": [30],
    #     "mayor": [70]
    # }

    # Si hay varias personas en una categoría:
    #
    # Edades: 5, 8, 15, 16, 25, 30, 70
    #
    # {
    #     "niño": [5, 8],
    #     "adolescente": [15, 16],
    #     "adulto": [25, 30],
    #     "mayor": [70]
    # }

    # Promedio de una categoría:
    # adulto → [25, 30]
    # (25 + 30) / 2 = 27.5

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)


# Programa principal
ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))

print(f"Promedio de adultos: {ae.edad_promedio_categoria('adulto')}")

