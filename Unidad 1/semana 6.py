# Clase base 'Animal'
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad     # Atributo protegido

    # Método para mostrar información del animal
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

    # Método a ser sobrescrito en las clases derivadas
    def hacer_sonido(self):
        pass

# Clase derivada 'Perro'
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescribir el método 'hacer_sonido'
    def hacer_sonido(self):
        return "Guau"

    # Método específico de la clase 'Perro'
    def buscar_pelota(self):
        return "El perro está buscando la pelota"

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}, Raza: {self.raza}"

# Clase derivada 'Gato'
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescribir el método 'hacer_sonido'
    def hacer_sonido(self):
        return "Miau"

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}, Color: {self.color}"

# Función principal para probar las clases
def main():
    # Crear una instancia de 'Perro'
    mi_perro = Perro("Fido", 5, "Labrador")
    print(mi_perro.mostrar_informacion())
    print(mi_perro.hacer_sonido())
    print(mi_perro.buscar_pelota())

    # Crear una instancia de 'Gato'
    mi_gato = Gato("Misu", 3, "Blanco")
    print(mi_gato.mostrar_informacion())
    print(mi_gato.hacer_sonido())

    # Polimorfismo: usando la misma interfaz para diferentes tipos de objetos
    animales = [mi_perro, mi_gato]
    for animal in animales:
        print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

if __name__ == "__main__":
    main()
