class AnalizadorPrimos:

    def es_primo(self, numero):
        if numero < 2:
            return False

        for i in range(2, numero):
            if numero % i == 0:
                return False

        return True

    def primos_hasta(self, limite):
        primos = []

        for numero in range(2, limite + 1):
            if self.es_primo(numero):
                primos.append(numero)

        return tuple(primos)

    def primos_en_multiples(self, *limites):
        resultado = {}

        for limite in limites:
            resultado[limite] = self.primos_hasta(limite)

        return resultado


ap = AnalizadorPrimos()

print(ap.primos_hasta(20))
print(ap.primos_en_multiples(10, 20, 30))