class SelectorPares:

    def crear_rango_pares(self, inicio, fin):
        pares = []

        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                pares.append(numero)

        return tuple(pares)

    def pares_en_multiples_rangos(self, *rangos):
        resultado = set()

        for inicio, fin in rangos:
            pares = self.crear_rango_pares(inicio, fin)
            resultado.update(pares)

        return sorted(resultado)


sp = SelectorPares()

print(sp.pares_en_multiples_rangos((1, 6), (4, 10)))