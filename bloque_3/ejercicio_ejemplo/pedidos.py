





class Pedidos():
    def __init__(self, cliente, productos:list):
        self.cliente = cliente
        self.productos = productos
    
    def añadir_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for i in self.productos:
            total += i.precio
        return total
































