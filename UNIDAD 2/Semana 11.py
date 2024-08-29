import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto
        print(f"Producto '{producto.obtener_nombre()}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado con éxito.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if producto.obtener_nombre().lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, archivo):
        try:
            with open(archivo, 'w') as f:
                productos_serializados = {id_producto: vars(producto) for id_producto, producto in self.productos.items()}
                json.dump(productos_serializados, f)
            print(f"Inventario guardado en '{archivo}'.")
        except IOError as e:
            print(f"Error al guardar el inventario en el archivo: {e}")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_serializados = json.load(f)
                self.productos = {id_producto: Producto(**datos) for id_producto, datos in productos_serializados.items()}
            print(f"Inventario cargado desde '{archivo}'.")
        except IOError as e:
            print(f"Error al cargar el inventario desde el archivo: {e}")
        except json.JSONDecodeError:
            print("El archivo está vacío o contiene datos no válidos.")


def menu():
    inventario = Inventario()
    archivo = "inventario.txt"

    while True:
        print("\nMenú del Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no modificar): ")
            precio = input("Nuevo precio (dejar en blanco para no modificar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None, precio=float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            inventario.guardar_en_archivo(archivo)
        elif opcion == "7":
            inventario.cargar_desde_archivo(archivo)
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
