class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y el objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs únicos de usuarios

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"Libro con ISBN {isbn} no disponible.")

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(isbn)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario {usuario.nombre} no tiene el libro con ISBN {isbn}.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and libro.info[0] == titulo) or \
               (autor and libro.info[1] == autor) or \
               (categoria and libro.categoria == categoria):
                resultados.append(str(libro))
        return resultados if resultados else "No se encontraron libros."

    def __str__(self):
        return f"Biblioteca con {len(self.libros_disponibles)} libros y {len(self.usuarios)} usuarios registrados."

# Ejemplo de uso
biblioteca = Biblioteca()
usuario1 = Usuario("Juan", "U001")
libro1 = Libro("Python 101", "John Doe", "Programación", "1234567890")

biblioteca.registrar_usuario(usuario1)
biblioteca.agregar_libro(libro1)
biblioteca.prestar_libro("1234567890", usuario1)

print(usuario1.listar_libros_prestados())
