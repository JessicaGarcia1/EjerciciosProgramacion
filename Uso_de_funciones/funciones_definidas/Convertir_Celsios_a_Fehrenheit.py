def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32

# Solicitar al usuario el valor en Celsius
try:
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
    print(f"{grados_celsius}°C son equivalentes a {grados_fahrenheit:.2f}°F.")
except ValueError:
    print("⚠️ Por favor, ingresa un número válido.")