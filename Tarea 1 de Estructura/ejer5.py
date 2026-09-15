            #DETECTOR DE NÚMEROS PARES E IMPARES
#Bosquejos
    #separar(1, 2, 3, 4, 5)

    #es_par(1) → 1 % 2 = 1 → No es par → impar
    #es_par(2) → 2 % 2 = 0 → Sí es par
    #es_par(3) → 3 % 2 = 1 → impar
    #es_par(4) → 4 % 2 = 0 → par
    #es_par(5) → 5 % 2 = 1 → impar

    #diccionario = {'pares': [2, 4], 'impares': [1, 3, 5]}

    #cantidad_pares_impares():
    #  cant_pares = len([2,4]) = 2
    #  cant_impares = len([1,3,5]) = 3
    #  resultado: (2, 3)

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())