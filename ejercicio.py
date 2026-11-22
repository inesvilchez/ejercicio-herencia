class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):
    def __init__(self, nombreCliente, emailCliente):
        super().__init__(nombreCliente)
        self.email = emailCliente


class Producto:
    def __init__(self, nombreProducto, precioProducto):
        self.nombre = nombreProducto
        self.precio = precioProducto


def comprar_producto_cliente(cliente, producto, unidades):
    print(
        f"El cliente con nombre {cliente.nombre} ha comprado "
        f"el producto con nombre {producto.nombre} "
        f"por un precio unitario de {producto.precio}€ "
        f"y un total de {unidades} unidades."
    )


cliente = Cliente("Ines", "ines@gmail.com")
producto = Producto("Adidas Samba", 120)

comprar_producto_cliente(cliente, producto, 3)