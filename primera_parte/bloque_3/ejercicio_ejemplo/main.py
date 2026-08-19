


from cliente import Cliente
from producto import Producto
from pedidos import Pedidos




if __name__ == "__main__":
    cliente1 = Cliente("Elena", "Diaz", "xxxxxxxxx", "elenaputa@gmail.com" )
    producto1 = Producto("Agua", 5)
    producto2 = Producto("Patatas", 10 )

    pedido_cliente1 = Pedidos(cliente1,[])
    pedido_cliente1.añadir_producto(producto1)
    pedido_cliente1.añadir_producto(producto2)
    # cliente1.mostrar_info()

    total = pedido_cliente1.calcular_total()
    print(f"El total de tu compra {cliente1.nombre} {cliente1.primer_apellido} es {total}€")



























