class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido al inventario.")

    def eliminar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                self.productos.remove(prod)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            print("Productos encontrados:")
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Inventario de productos:")
            for prod in self.productos:
                print(prod)


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar el menú interactivo
menu()
