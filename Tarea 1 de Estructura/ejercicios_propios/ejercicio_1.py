class Evaluador:

    def __init__(self):
        self.puntajes = []

    def validar_puntaje(self, puntaje):
        if puntaje >= 1 and puntaje <= 100:
            return True
        else:
            return False

    def cargar_puntaje(self, *args):
        for p in args:
            if self.validar_puntaje(p):
                self.puntajes.append(p)
        return self.puntajes

    def maximo(self):
        return max(self.puntajes)

e = Evaluador()
print(e.cargar_puntaje(8, 11, 5, 0, 10, 7))
print(e.maximo())