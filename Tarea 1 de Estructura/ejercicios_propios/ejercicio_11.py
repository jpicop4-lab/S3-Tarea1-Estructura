class ContadorVotos:

    def __init__(self):
        self.votos = {}

    def agregar_voto(self, candidato):
        if candidato in self.votos:
            self.votos[candidato] += 1
        else:
            self.votos[candidato] = 1

    def ganador(self):
        ganador = None
        mayor = 0

        for candidato, cantidad in self.votos.items():
            if cantidad > mayor:
                ganador = candidato
                mayor = cantidad

        return ganador

    def votos_candidato(self, candidato):
        return self.votos.get(candidato, 0)


cv = ContadorVotos()

cv.agregar_voto("A")
cv.agregar_voto("B")
cv.agregar_voto("A")
cv.agregar_voto("C")
cv.agregar_voto("A")

print(cv.ganador())
print(cv.votos_candidato("A"))
print(cv.votos)