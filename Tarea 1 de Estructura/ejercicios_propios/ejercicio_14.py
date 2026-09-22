class RegistroTiempos:

    def __init__(self):
        self.tiempos = {}

    def registrar(self, atleta, tiempo):
        self.tiempos[atleta] = tiempo

    def atletas_clasificados(self, tiempo_maximo):
        resultado = []

        for atleta, tiempo in self.tiempos.items():
            if tiempo <= tiempo_maximo:
                resultado.append(atleta)

        return resultado

    def mejor_atleta(self):
        mejor = None
        menor_tiempo = None

        for atleta, tiempo in self.tiempos.items():
            if menor_tiempo is None or tiempo < menor_tiempo:
                mejor = atleta
                menor_tiempo = tiempo

        return (mejor, menor_tiempo)


rt = RegistroTiempos()

rt.registrar("Ana", 10.5)
rt.registrar("Bob", 12.3)

print(rt.mejor_atleta())