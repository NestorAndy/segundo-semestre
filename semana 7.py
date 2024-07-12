import os

class TempFile:
    def __init__(self, nombre):
        """
        Constructor de la clase TempFile.
        Crea un archivo temporal con el nombre especificado.

        Args:
        nombre (str): Nombre del archivo temporal a crear.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo temporal '{self.nombre}' creado")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo temporal.

        Args:
        texto (str): Texto a escribir en el archivo.
        """
        self.archivo.write(texto + '\n')
        print(f"Escrito en '{self.nombre}': {texto}")

    def cerrar(self):
        """
        Método para cerrar el archivo temporal.

        Se debe llamar explícitamente para cerrar el archivo y liberar recursos.
        """
        self.archivo.close()
        print(f"Archivo temporal '{self.nombre}' cerrado")

    def __del__(self):
        """
        Destructor de la clase TempFile.

        Se ejecuta automáticamente cuando el objeto es destruido.
        Cierra automáticamente el archivo temporal creado.
        """
        if not self.archivo.closed:
            self.cerrar()
        # Eliminar archivo temporal si existe
        if os.path.exists(self.nombre):
            os.remove(self.nombre)
            print(f"Archivo temporal '{self.nombre}' eliminado")

# Ejemplo de uso
try:
    archivo_temporal = TempFile("datos_temporales.txt")
    archivo_temporal.escribir("Hola, mundo!")
    archivo_temporal.escribir("Este es un ejemplo de uso de constructores y destructores en Python")
finally:
    del archivo_temporal

