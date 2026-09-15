            # BUSCADOR DE DIVISORES
# Bosquejo

    # Número a analizar: 12

    # Probar divisores desde 1 hasta 12:
    # ¿12 % 1 == 0?  → SÍ → 1
    # ¿12 % 2 == 0?  → SÍ → 2
    # ¿12 % 3 == 0?  → SÍ → 3
    # ¿12 % 4 == 0?  → SÍ → 4
    # ¿12 % 5 == 0?  → NO
    # ¿12 % 6 == 0?  → SÍ → 6
    # ¿12 % 7 == 0?  → NO
    # ¿12 % 8 == 0?  → NO
    # ¿12 % 9 == 0?  → NO
    # ¿12 % 10 == 0? → NO
    # ¿12 % 11 == 0? → NO
    # ¿12 % 12 == 0? → SÍ → 12

    # Divisores:
    # [1, 2, 3, 4, 6, 12]

    # Convertir a tupla:
    # (1, 2, 3, 4, 6, 12)


    # Número perfecto:
    # 6 → divisores excepto él mismo: 1, 2, 3
    # 1 + 2 + 3 = 6
    # 6 es perfecto → True


    # Múltiples números:
    # 6  → (1, 2, 3, 6)
    # 12 → (1, 2, 3, 4, 6, 12)

    # Diccionario:
    # {
    #     6: (1, 2, 3, 6),
    #     12: (1, 2, 3, 4, 6, 12)
    # }

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


# Programa principal
df = DivisorFinder()

print(df.encontrar_divisores(12))

print(df.es_perfecto(6))
print(df.es_perfecto(12))

print(df.encontrar_multiples_divisores(6, 12, 15))