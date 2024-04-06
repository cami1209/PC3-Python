class Producto:
    def __init__(self, nombre, precio, año, mes):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.mes = mes

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - {self.año} - {self.mes}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)

    def filtrar_por_mes(self, mes):
        print(f"Productos del mes {mes}:")
        for producto in self.productos:
            if producto.mes == mes:
                print(producto)

if __name__ == "__main__":
    catalogo = Catalogo()

    # Agregar productos
    catalogo.agregar_producto(Producto("Filtro de aceite", 20.99, 2021, "Enero"))
    catalogo.agregar_producto(Producto("Pastillas de freno", 35.50, 2020, "Marzo"))
    catalogo.agregar_producto(Producto("Batería de arranque", 120.00, 2021, "Febrero"))

    # Mostrar todos los productos
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2021)

    # Filtrar productos por mes
    catalogo.filtrar_por_mes("Febrero")

