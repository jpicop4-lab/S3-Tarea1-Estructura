            # GESTOR DE PERSONAS
# Bosquejo

    # Personas y edades:
    # Ana → 28
    # Emilio → 19

    # Guardar en diccionario:
    # {
    #     "Ana": 28,
    #     "Emilio": 19
    # }


    # Buscar personas mayores de 18:
    #
    # ¿Ana tiene 28 >= 18?     → SÍ → "Ana"
    # ¿Emilio tiene 19 >= 18?  → SÍ → "Emilio"
    #
    # Lista de mayores:
    # ["Ana", "Emilio"]


    # Calcular edad promedio:
    #
    # Ana → 28
    # Emilio → 19
    #
    # Suma:
    # 28 + 19 = 47
    #
    # Cantidad de personas:
    # 2
    #
    # Promedio:
    # 47 / 2 = 23.5
    #
    # Resultado:
    # 23.50

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_personas(self, nombre,edad):
        self.personas[nombre] = edad

    def personas_mayores(self,edad_minima):
        mayores = []

        for nombre,edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)

        return mayores

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = 0

        for nombre, edad in self.personas.items():
            suma += edad

        return suma / len(self.personas)

# Programa principal
gp= GestorPersonas()

gp.agregar_personas("Ana",28)
gp.agregar_personas("Emilio", 19)

print(gp.personas_mayores(18))
print(f"Edad promedio:  {gp.edad_promedio():.2f}")