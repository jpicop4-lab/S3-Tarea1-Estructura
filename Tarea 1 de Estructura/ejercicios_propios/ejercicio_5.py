class AnalizadorMultiplos:

    def __init__(self):
        self.multiplos = []
        self.no_multiplos =[]

    def es_multiplo_de_tres(self, numero):
        return numero % 3 == 0

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_multiplo_de_tres(numero):
                self.multiplos.append(numero)
            else:
                self.no_multiplos.append(numero)
        return {
            'multiplos de tres': self.multiplos,
            'no multiplos de tres' : self.no_multiplos
            }

    def cantidad_multiplo_no_multiplo(self):
        return(len(self.multiplos), len(self.no_multiplos))

am = AnalizadorMultiplos()
print(am.separar(1,3,6,7,9))