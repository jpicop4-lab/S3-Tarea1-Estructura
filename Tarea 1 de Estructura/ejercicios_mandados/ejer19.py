            # INVENTARIO
# Bosquejo

    # Productos y cantidades:
    # pan → 50
    # leche → 10
    # huevos → 20

    # Diccionario inicial:
    # {
    #     "pan": 50,
    #     "leche": 10,
    #     "huevos": 20
    # }


    # Restar stock:
    #
    # Pan tiene 50
    # Se quieren restar 30
    #
    # ¿50 >= 30? → SÍ
    # 50 - 30 = 20
    #
    # Stock actualizado:
    # {
    #     "pan": 20
    # }
    #
    # Resultado → True


    # Si se quieren restar más de lo disponible:
    #
    # Pan tiene 20
    # Se quieren restar 30
    #
    # ¿20 >= 30? → NO
    # No se modifica el stock
    #
    # Resultado → False


    # Buscar productos bajo stock:
    #
    # Mínimo: 25
    #
    # ¿Pan → 20 < 25?     → SÍ → "pan"
    # ¿Leche → 10 < 25?   → SÍ → "leche"
    # ¿Huevos → 20 < 25?  → SÍ → "huevos"
    #
    # Resultado:
    # ["pan", "leche", "huevos"]

class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        productos = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                productos.append(producto)

        return productos


# Programa principal
inv = Inventario()

inv.agregar_stock("pan", 50)

resultado = inv.restar_stock("pan", 30)
print(resultado)

print(inv.productos_bajo_stock(15))