def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
    celsius (float): La temperatura en grados Celsius

    Returns:
    float: La temperatura en grados Fahrenheit
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def es_temperatura_alta(celsius):
    """
    Verifica si la temperatura es mayor a 30 grados Celsius.

    Args:
    celsius (float): La temperatura en grados Celsius

    Returns:
    bool: True si la temperatura es mayor a 30 grados, False en caso contrario
    """
    return celsius > 30


def main():
    """
    Función principal del programa.
    Solicita al usuario una temperatura en grados Celsius y muestra la conversión a Fahrenheit.
    Indica si la temperatura es alta.
    """
    # Solicitar al usuario la temperatura en grados Celsius
    temperatura_str = input("Introduce la temperatura en grados Celsius: ")

    # Convertir la temperatura a float
    try:
        temperatura_celsius = float(temperatura_str)
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    # Convertir a Fahrenheit
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")

    # Verificar si la temperatura es alta
    if es_temperatura_alta(temperatura_celsius):
        print("Hace calor.")
    else:
        print("La temperatura es moderada.")


if __name__ == "__main__":
    main()
