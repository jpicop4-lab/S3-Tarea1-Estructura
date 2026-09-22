class RotadorLista:

    def rotar_izquierda(self, lista, n):

        resultado = []

        n = n % len(lista)

        for i in range(n, len(lista)):
            resultado.append(lista[i])

        for i in range(n):
            resultado.append(lista[i])

        return resultado

    def rotar_multiples(self, n, *listas):

        resultado = {}

        for lista in listas:
            rotada = self.rotar_izquierda(lista, n)
            resultado[tuple(lista)] = rotada

        return resultado


r = RotadorLista()

print(r.rotar_izquierda([1, 2, 3, 4], 1))

print(r.rotar_multiples(
    1,
    [1, 2, 3, 4],
    [5, 6, 7],
    [10, 20, 30]
))