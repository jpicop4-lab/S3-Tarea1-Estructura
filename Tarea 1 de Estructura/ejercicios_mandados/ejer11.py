            # CONTADOR DE FRECUENCIA
# Bosquejo

    # Elementos a cargar:
    #
    # "a"
    # "b"
    # "a"
    # "c"
    # "a"
    # "b"


    # Agregar elementos al diccionario:
    #
    # ¿"a" existe?
    # → NO → "a": 1
    #
    # ¿"b" existe?
    # → NO → "b": 1
    #
    # ¿"a" existe?
    # → SÍ → aumentar a 2
    #
    # ¿"c" existe?
    # → NO → "c": 1
    #
    # ¿"a" existe?
    # → SÍ → aumentar a 3
    #
    # ¿"b" existe?
    # → SÍ → aumentar a 2


    # Diccionario final:
    # {
    #     "a": 3,
    #     "b": 2,
    #     "c": 1
    # }


    # Buscar elemento más frecuente:
    #
    # ¿"a" tiene frecuencia mayor que 0?
    # 3 > 0 → SÍ
    # elemento_mayor = "a"
    # mayor_frecuencia = 3
    #
    # ¿"b" tiene frecuencia mayor que 3?
    # 2 > 3 → NO
    #
    # ¿"c" tiene frecuencia mayor que 3?
    # 1 > 3 → NO
    #
    # Más frecuente:
    # "a"


    # Buscar frecuencia de "a":
    #
    # ¿"a" existe en el diccionario?
    # → SÍ
    # → frecuencia = 3
    #
    # Resultado:
    # 3

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = None
        mayor_frecuencia = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor_frecuencia:
                mayor_frecuencia = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


# Programa principal
cf = ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("c")
cf.agregar_elemento("a")
cf.agregar_elemento("b")

print("Frecuencias:", cf.frecuencias)
print("Más frecuente:", cf.elemento_mas_frecuente())
print("Frecuencia de 'a':", cf.frecuencia_elemento("a"))