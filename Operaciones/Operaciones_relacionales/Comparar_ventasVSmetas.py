def obtener_float(mensaje):
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:  # Verifica si la entrada está vacía
                raise ValueError("La entrada no puede estar vacía.")
            return float(valor)
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese un número válido.")

# Datos de las ventas y la meta 
ventas = obtener_float("Ingrese las ventas realizadas por el vendedor: ")
meta = obtener_float("Ingrese la meta de ventas establecida: ")

# Comparar las ventas con la meta
if ventas >= meta:
    print(f"El vendedor cumplió con la meta. Ventas realizadas: ${ventas:,.2f}, Meta: ${meta:,.2f}")
else:
    print(f"El vendedor no cumplió con la meta. Ventas realizadas: ${ventas:,.2f}, Meta: ${meta:,.2f}")

# Porcentaje alcanzado de la meta
porcentaje = (ventas / meta) * 100
print(f"El vendedor alcanzó el {porcentaje:.2f}% de la meta.")

