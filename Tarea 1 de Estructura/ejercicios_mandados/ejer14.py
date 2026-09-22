            # REGISTRO DE NOTAS
# Bosquejo

    # Estudiantes y notas:
    # Ana → 95
    # Bob → 70
    # Carlos → 85

    # Guardar en diccionario:
    # {
    #     "Ana": 95,
    #     "Bob": 70,
    #     "Carlos": 85
    # }

    # ¿Nota de Ana >= 70?     95 >= 70 → SÍ → "Ana"
    # ¿Nota de Bob >= 70?     70 >= 70 → SÍ → "Bob"
    # ¿Nota de Carlos >= 70?  85 >= 70 → SÍ → "Carlos"

    # Estudiantes aprobados:
    # ["Ana", "Bob", "Carlos"]

    # Buscar mejor estudiante:
    # Ana → 95
    # Bob → 70
    # Carlos → 85
    #
    # Mayor nota → 95
    # Mejor estudiante → ("Ana", 95)

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor = None
        mayor_nota = float("-inf")

        for estudiante, nota in self.notas.items():
            if nota > mayor_nota:
                mayor_nota = nota
                mejor = estudiante

        return (mejor, mayor_nota)


# Programa principal
rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)

print("Aprobados:", rn.estudiantes_aprobados(70))
print("Mejor estudiante:", rn.mejor_estudiante())