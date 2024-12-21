# Solicitar las temperaturas al usuario
temperaturas = []
print("Ingresa las temperaturas de los 7 días:")
for i in range(7):
    temp = float(input(f"Día {i+1}: "))
    temperaturas.append(temp)

# Procesar los datos (similar al ejemplo anterior)
promedio = sum(temperaturas) / len(temperaturas)
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
dia_maxima = temperaturas.index(temperatura_maxima) + 1

# Mostrar los resultados
print(f"\nPromedio de temperaturas: {promedio:.2f}°C")
print(f"Temperatura más alta: {temperatura_maxima}°C")
print(f"Temperatura más baja: {temperatura_minima}°C")
print(f"La temperatura más alta ocurrió el día {dia_maxima}.")
