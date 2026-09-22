            # ANALIZADOR DE STRINGS
# Bosquejo

    # Texto 1:
    # "Hola123"

    # Revisar cada carácter:
    #
    # H → consonante
    # o → vocal
    # l → consonante
    # a → vocal
    # 1 → dígito
    # 2 → dígito
    # 3 → dígito
    #
    # Resultado:
    # {
    #     "vocales": 2,
    #     "consonantes": 2,
    #     "digitos": 3
    # }


    # Texto 2:
    # "Un gusto, Me llamo emilio1404213, tangamandapio"
    #
    # Revisar carácter por carácter:
    #
    # ¿Es vocal?       → contar en "vocales"
    # ¿Es dígito?      → contar en "digitos"
    # ¿Es letra?       → contar en "consonantes"
    # ¿Es espacio/coma? → no contar
    #
    # Se obtiene un nuevo conteo de:
    # {
    #     "vocales": ...,
    #     "consonantes": ...,
    #     "digitos": ...
    # }


    # Comparar longitud de textos:
    #
    # ¿Texto 2 es más largo que texto 1?
    # len(texto 2) > len(texto 1) → SÍ
    #
    # texto_mas_largo =
    # "Un gusto, Me llamo emilio1404213, tangamandapio"


    # Resultado final:
    # Diccionario → conteo del último texto analizado
    # texto_mas_largo → texto con mayor cantidad de caracteres

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouAEIOU"

    def contar_por_tipo(self, texto):
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:
            if self.solo_vocales(letra):
                conteo["vocales"] += 1
            elif letra.isdigit():
                conteo["digitos"] += 1
            elif letra.isalpha():
                conteo["consonantes"] += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return conteo


# Programa principal
astr = AnalizadorString()

resultado = astr.contar_por_tipo("Hola123")
resultado = astr.contar_por_tipo("Un gusto, Me llamo emilio1404213, tangamandapio")

print(resultado)
print(f"Texto más largo: {astr.texto_mas_largo}")