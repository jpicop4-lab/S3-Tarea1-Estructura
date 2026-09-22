            #INVERSOR DE SECUENCIAS
#Bosquejo
    #invertir_lista([1, 2, 3]):
    #  Recorro de atrás hacia adelante:
    #    índice 2 → 3
    #    índice 1 → 2
    #    índice 0 → 1
    #  Resultado: [3, 2, 1]

    #invertir_multiples([1,2,3], [4,5]):
    #  invertir_lista([1,2,3]) → [3, 2, 1]
    #  invertir_lista([4,5])   → [5, 4]
    # Resultado: {(1,2,3): [3,2,1], (4,5): [5,4]}

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)          
            resultado[clave] = self.invertir_lista(lista)
        return resultado


inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))