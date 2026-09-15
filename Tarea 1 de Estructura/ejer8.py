            # GESTOR DE EQUIPOS
# Bosquejo

    # Crear equipos:
    # A
    # B
    # C

    # Diccionario inicial:
    # {
    #     "A": [],
    #     "B": [],
    #     "C": []
    # }


    # Agregar jugadores:

    # Equipo A:
    # Juan
    # Pedro
    #
    # A → ["Juan", "Pedro"]

    # Equipo B:
    # Carlos
    # Luis
    # Ana
    #
    # B → ["Carlos", "Luis", "Ana"]

    # Equipo C:
    # Maria
    #
    # C → ["Maria"]


    # Diccionario final:
    # {
    #     "A": ["Juan", "Pedro"],
    #     "B": ["Carlos", "Luis", "Ana"],
    #     "C": ["Maria"]
    # }


    # Buscar equipo con más integrantes:
    #
    # ¿A tiene más jugadores que 0?
    # 2 > 0 → SÍ
    # equipo_mayor = "A"
    # mayor_cantidad = 2
    #
    # ¿B tiene más jugadores que 2?
    # 3 > 2 → SÍ
    # equipo_mayor = "B"
    # mayor_cantidad = 3
    #
    # ¿C tiene más jugadores que 3?
    # 1 > 3 → NO
    #
    # Equipo con más integrantes:
    # "B"

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        equipo_mayor = None
        mayor_cantidad = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor


# Programa principal
eq = Equipos()

eq.crear_equipo("A")
eq.crear_equipo("B")
eq.crear_equipo("C")

eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")

eq.agregar_jugador("B", "Carlos")
eq.agregar_jugador("B", "Luis")
eq.agregar_jugador("B", "Ana")

eq.agregar_jugador("C", "Maria")

print(eq.equipos)
print(f"Equipo con más integrantes: {eq.equipo_mayor_integrantes()}")