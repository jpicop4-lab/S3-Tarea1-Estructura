class Pedidos:

    def __init__(self):
        self.pedidos =[]

    def agregar_pedido(self, cliente, estado):
        pedido =(cliente,estado)
        self.pedidos.append(pedido)

    def pedidos_pendientes(self):
        pendientes = []

        for cliente, estado in self.pedidos:
            if estado == "pendiente":
                pendientes.append((cliente, estado))
        return pendientes

    def eliminar_entregado(self, cliente):
        for pedido in self.pedidos:
            if pedido[0] == cliente and pedido [1]== "entregado":
                self.pedidos.remove(pedido)
                break

p = Pedidos()

p.agregar_pedido("Ana", "pendiente")
p.agregar_pedido("Luis", "entregado")
p.agregar_pedido("Carlos", "pendiente")

print(p.pedidos_pendientes())
