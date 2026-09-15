            # COMBINADOR DE LISTAS
# Bosquejo

    # Listas a cargar:
    # lista1 = [1, 2]
    # lista2 = [3, 4]

    # Intercalar elementos:
    # 1 → de lista1
    # 3 → de lista2
    # 2 → de lista1
    # 4 → de lista2

    # Resultado:
    # [1, 3, 2, 4]
    # lista1 = [1, 2]
    # lista2 = [3, 4]
    # lista3 = [5, 6]

    # Intercalar:
    # 1 → 3 → 5
    # 2 → 4 → 6

    # Resultado:
    # [1, 3, 5, 2, 4, 6]

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []

        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        mayor = max(len(lista) for lista in listas)

        for i in range(mayor):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])

        return resultado


# Programa principal
cl = CombinadorListas()

print(cl.intercalar([1, 2], [3, 4]))

print(cl.intercalar_multiples(
    [1, 2],
    [3, 4],
    [5, 6]
))