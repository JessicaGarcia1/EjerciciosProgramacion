# Temperaturas registradas durante una semana (en grados Celsius)
temperaturas = [22, 25, 19, 21, 23, 20, 24]

# Calcular el promedio de las temperaturas
promedio = sum(temperaturas) / len(temperaturas)
print(f"Promedio de temperaturas: {promedio:.2f}°C")

# Encontrar la temperatura más alta y más baja
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
print(f"Temperatura más alta: {temperatura_maxima}°C")
print(f"Temperatura más baja: {temperatura_minima}°C")

# Identificar el día con la temperatura más alta
dia_maxima = temperaturas.index(temperatura_maxima) + 1  # +1 porque los días empiezan en 1
print(f"La temperatura más alta ocurrió el día {dia_maxima}.")
