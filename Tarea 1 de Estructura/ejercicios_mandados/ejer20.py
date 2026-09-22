            # ANALIZADOR DE PATRONES
# Bosquejo

    # Texto:
    # "el gato está aquí"

    # Separar palabras con split():
    # ["el", "gato", "está", "aquí"]


    # Buscar palabras que comiencen con un patrón:
    #
    # Texto: "el gato está aquí"
    # Patrón: "ga"
    #
    # ¿"el".startswith("ga")?    → NO
    # ¿"gato".startswith("ga")?  → SÍ → "gato"
    # ¿"está".startswith("ga")?  → NO
    # ¿"aquí".startswith("ga")?  → NO
    #
    # Resultado:
    # ["gato"]


    # Agrupar por longitud:
    #
    # "el"   → len = 2
    # "gato" → len = 4
    # "está" → len = 4
    # "aquí" → len = 4
    #
    # Diccionario:
    # {
    #     2: ["el"],
    #     4: ["gato", "está", "aquí"]
    # }


    # Palabras únicas:
    #
    # Texto:
    # "el gato gato está el"
    #
    # Lista:
    # ["el", "gato", "gato", "está", "el"]
    #
    # Conjunto:
    # {"el", "gato", "está"}
    #
    # Los repetidos se eliminan automáticamente.

class AnalizadorPatrones:

    def __init__(self):
        self.texto = ""

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        palabras = self.texto.split()
        return set(palabras)


# Programa principal
ap = AnalizadorPatrones()

texto = "el gato está aquí"

print(ap.encontrar_palabras(texto, "ga"))
print(ap.agrupar_por_longitud(texto))

ap.texto = "el gato gato está el"
print(ap.palabras_unicas())