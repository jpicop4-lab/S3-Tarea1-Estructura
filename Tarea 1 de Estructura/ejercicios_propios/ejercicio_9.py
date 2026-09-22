class AnalizadorCadena:

    def __init__(self):
        self.ultimo_texto = ""

    def es_mayuscula(self, letra):
        return letra.isupper()

    def contar_por_caso(self, texto):
        self.ultimo_texto = texto

        conteo = {
            "mayusculas": 0,
            "minusculas": 0,
            "otros": 0
        }

        for letra in texto:
            if self.es_mayuscula(letra):
                conteo["mayusculas"] += 1

            elif letra.islower():
                conteo["minusculas"] += 1

            else:
                conteo["otros"] += 1

        return conteo


ac = AnalizadorCadena()

print(ac.contar_por_caso("Sol2026"))