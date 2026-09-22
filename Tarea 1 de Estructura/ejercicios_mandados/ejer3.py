            #GESTOR DE COMPRAS CON TOTALES
#Bosquejo
    #agregar_articulo("pan", 2.50)
    #  diccionario = {"pan": 2.50}

    #agregar_articulo("leche", 3.00)
    #  diccionario = {"pan": 2.50, "leche": 3.00}

    #total_carrito():
    #  sumar valores → 2.50 + 3.00 = 5.50

    #articulos_por_rango(2, 3):
    #  ¿pan (2.50) está entre 2 y 3?    Sí → incluir
    #  ¿leche (3.00) está entre 2 y 3?  Sí → incluir
    #  resultado: ["pan", "leche"]

class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
print(c.total_carrito())
print(c.articulos_por_rango(2, 3))