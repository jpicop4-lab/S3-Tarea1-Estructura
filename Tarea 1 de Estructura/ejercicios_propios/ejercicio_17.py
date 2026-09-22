class AgrupadorNotas:

    def __init__(self):
        self.categorias = {
            "excelente": [],
            "bueno": [],
            "regular": [],
            "reprobado": []
        }

    def clasificar_nota(self, nota):
        if nota >= 90:
            return "excelente"
        elif nota >= 70:
            return "bueno"
        elif nota >= 50:
            return "regular"
        else:
            return "reprobado"

    def agrupar_por_categoria(self, *notas):
        self.categorias = {
            "excelente": [],
            "bueno": [],
            "regular": [],
            "reprobado": []
        }

        for nota in notas:
            categoria = self.clasificar_nota(nota)
            self.categorias[categoria].append(nota)

        return self.categorias

    def nota_promedio_categoria(self, categoria):
        notas = self.categorias[categoria]

        if len(notas) == 0:
            return 0

        return sum(notas) / len(notas)


an = AgrupadorNotas()

print(an.agrupar_por_categoria(95, 80, 60, 30))
print(an.nota_promedio_categoria("excelente"))