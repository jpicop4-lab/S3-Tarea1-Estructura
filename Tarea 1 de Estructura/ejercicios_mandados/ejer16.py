            # CODIFICADOR CÉSAR
# Bosquejo

    # Palabra: "hola"
    # Desplazamiento: 3

    # Codificar cada letra:
    # h → k
    # o → r
    # l → o
    # a → d

    # Resultado:
    # "krod"

    # Si una letra llega al final del alfabeto:
    # y + 3 → b
    # z + 1 → a
    #
    # Se utiliza % para volver al inicio del alfabeto.

    # Historial:
    # guardar palabra original → palabra codificada
    #
    # Ejemplo:
    # {
    #     "hola": "krod"
    # }

class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            codigo = ord(letra.lower()) - ord("a")
            nuevo_codigo = (codigo + desplazamiento) % 26
            return chr(nuevo_codigo + ord("a"))

        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


# Programa principal
cc = CodificadorCesar()

palabra = input("Palabra: ")
desplazamiento = int(input("Desplazamiento (1-25): "))

resultado = cc.codificar_palabra(palabra, desplazamiento)

print(f"Palabra codificada: {resultado}")
print(f"Historial: {cc.historial}")