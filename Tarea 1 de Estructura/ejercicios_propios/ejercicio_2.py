class ControlAsistencia:

    def __init__(self):
        self.asistentes = set()
        self.lista_asistente = []

    def registrar_nombre(self, nombre):
        if nombre not in self.asistentes:
            self.asistentes.add(nombre)
            self.lista_asistente.append(nombre)

    def contar_asistentes(self):
        return len(self.asistentes)

    def regristrar_varios(self, *args):
        for nombre in args:
            self.registrar_nombre(nombre)

ca = ControlAsistencia()

ca.regristrar_varios("Ana","Emilio","Ana")

print(ca.contar_asistentes())