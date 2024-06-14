# Función para ingresar las temperaturas diarias
def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

# Función principal para ejecutar el programa
def main():
    print("Ingrese las temperaturas diarias de la semana:")
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
