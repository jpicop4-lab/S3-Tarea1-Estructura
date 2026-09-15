            # SELECTOR DE RANGOS
# Bosquejo

    # Rangos a cargar: (1,3), (2,4)

    # Primer rango: (1,3)
    # Números → 1, 2, 3
    # Tupla → (1, 2, 3)

    # Segundo rango: (2,4)
    # Números → 2, 3, 4
    # Tupla → (2, 3, 4)

    # Combinar los rangos:
    # (1, 2, 3) + (2, 3, 4)

    # Usar conjunto para eliminar repetidos:
    # {1, 2, 3, 4}

    # Convertir a lista:
    # Lista final → [1, 2, 3, 4]

class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for inicio, fin in rangos:
            rango = self.crear_rango(inicio, fin)
            elementos.update(rango)

        return sorted(list(elementos))


# Programa principal
sr = SelectorRango()

resultado = sr.elementos_en_multiples_rangos((1, 3), (2, 4))

print(resultado)