class AnalizadorFrases:

    def encontrar_palabras_terminan(self, texto, sufijo):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.endswith(sufijo):
                resultado.append(palabra)

        return resultado

    def agrupar_por_inicial(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            inicial = palabra[0]

            if inicial not in resultado:
                resultado[inicial] = []

            resultado[inicial].append(palabra)

        return resultado

    def palabras_unicas(self, texto):
        palabras = texto.split()

        return set(palabras)


af = AnalizadorFrases()

print(af.encontrar_palabras_terminan("el gato come el pan", "el"))
print(af.agrupar_por_inicial("el gato come el pan"))
print(af.palabras_unicas("el gato come el pan el"))