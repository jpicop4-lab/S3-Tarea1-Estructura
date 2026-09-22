            #CONTADOR DE PALABRAS ÚNICAS
#Bosquejo
    #agregar_multiples("hola", "mundo", "hola")

    #agregar_palabra("hola"):
    #  conjunto = {"hola"}
    #  lista    = ["hola"]

    #agregar_palabra("mundo"):
    #  conjunto = {"hola", "mundo"}
    #  lista    = ["hola", "mundo"]

    #agregar_palabra("hola"):  <- ya está en el conjunto
    #  conjunto = {"hola", "mundo"}   (no cambia, sets no repiten)
    #  lista    = ["hola", "mundo", "hola"]   (la lista SÍ la vuelve a guardar)

    #contar_palabras():
    #  len(conjunto) = 2


class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())