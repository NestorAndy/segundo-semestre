# Definición de la clase ClimaDiario
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio semanal
    def calcular_promedio_semanal(self):
        suma_temperaturas = sum(self.temperaturas)
        promedio = suma_temperaturas / len(self.temperaturas)
        return promedio

# Función principal para ejecutar el programa
def main():
    clima = ClimaDiario()

    clima.ingresar_temperaturas_diarias()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
