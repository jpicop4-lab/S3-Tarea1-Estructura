class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso ,estudiante):
        self.cursos[curso].append(estudiante)

    def curso_menor_integrantes(self):
        curso_menor = None
        cantidad_menor = None

        for curso, estudiantes in self.cursos.items():
            cantidad = len(estudiantes)

            if cantidad_menor is None or cantidad < cantidad_menor:
                curso_menor = curso
                cantidad_menor = cantidad

        return curso_menor

c = Cursos()

c.crear_curso("Mat")
c.crear_curso("Fis")

c.agregar_estudiante("Mat", "Ana")
c.agregar_estudiante("Fis", "Luis")
c.agregar_estudiante("Fis", "Eva")

print(c.curso_menor_integrantes())
