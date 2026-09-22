class DecodificadorCesar:

    def __init__(self):
        self.historial = {}

    def decodificar_letra(self, letra, desplazamiento):
        posicion = ord(letra) - ord("a")
        nueva_posicion = (posicion - desplazamiento) % 26
        return chr(nueva_posicion + ord("a"))

    def decodificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.decodificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


dc = DecodificadorCesar()

print(dc.decodificar_palabra("krod", 3))
print(dc.historial)