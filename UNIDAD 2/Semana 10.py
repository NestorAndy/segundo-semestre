class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'Producto(nombre={self.nombre}, cantidad={self.cantidad}, precio={self.precio})'


class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def añadir_producto(self, producto):
        self.productos.append(producto)
        try:
            with open('inventario.txt', 'a') as file:
                file.write(f'{producto.nombre},{producto.cantidad},{producto.precio}\n')
            print(f'Producto {producto.nombre} añadido y guardado en el archivo con éxito.')
        except (PermissionError, FileNotFoundError) as e:
            print(f'Error al guardar el producto en el archivo: {e}')

    def actualizar_producto(self, nombre, cantidad, precio):
        producto = self.buscar_producto(nombre)
        if producto:
            producto.cantidad = cantidad
            producto.precio = precio
            self.guardar_inventario()
            print(f'Producto {nombre} actualizado y guardado en el archivo con éxito.')
        else:
            print(f'Producto {nombre} no encontrado.')

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f'Producto {nombre} eliminado y guardado en el archivo con éxito.')
        else:
            print(f'Producto {nombre} no encontrado.')

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def cargar_inventario(self):
        try:
            with open('inventario.txt', 'r') as file:
                for line in file:
                    nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(nombre, int(cantidad), float(precio)))
            print('Inventario cargado desde el archivo con éxito.')
        except FileNotFoundError:
            print('Archivo de inventario no encontrado. Se creará uno nuevo al añadir productos.')
        except PermissionError as e:
            print(f'Error de permisos al intentar cargar el inventario: {e}')

    def guardar_inventario(self):
        try:
            with open('inventario.txt', 'w') as file:
                for producto in self.productos:
                    file.write(f'{producto.nombre},{producto.cantidad},{producto.precio}\n')
        except (PermissionError, FileNotFoundError) as e:
            print(f'Error al guardar el inventario en el archivo: {e}')


# Ejemplo de uso:
if __name__ == "__main__":
    inventario = Inventario()

    # Añadir productos
    inventario.añadir_producto(Producto("Manzana", 50, 0.5))

    # Actualizar un producto
    inventario.actualizar_producto("Manzana", 100, 0.45)

    # Eliminar un producto
    inventario.eliminar_producto("Manzana")
