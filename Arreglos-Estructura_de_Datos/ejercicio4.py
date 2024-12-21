import numpy as np
import pandas as pd

ventas_df = pd.read_csv(r"C:\Users\Jessica Garcia\OneDrive - Kenworth Del este\Escritorio\Ventas.csv")

# Verificar los datos cargados
print("Datos:")
print(ventas_df)

# Obtener los valores únicos de cada dimensión
productos = ventas_df["Producto"].unique()
sucursal = ventas_df["Sucursal"].unique()
fechas = ventas_df["Fecha"].unique()

# Crear un arreglo tridimensional: Producto x Sucursal x Fecha
ventas_matriz = np.zeros((len(productos), len(sucursal), len(fechas)))

# Llenar el arreglo con los datos del CSV
for _, row in ventas_df.iterrows():
    producto_idx = np.where(productos == row["Producto"])[0][0]
    tienda_idx = np.where(sucursal == row["Sucursal"])[0][0]
    fecha_idx = np.where(fechas == row["Fecha"])[0][0]
    ventas_matriz[producto_idx, tienda_idx, fecha_idx] += row["Cantidad"]

# Calcular totales por dimensión
# Total de ventas por producto
print("\nVentas totales por producto:")
for i, total in enumerate(ventas_matriz.sum(axis=(1, 2))):
    print(f"Producto {productos[i]}: {total}")

# Total de ventas por tienda
print("\nVentas totales por Sucursal:")
for i, total in enumerate(ventas_matriz.sum(axis=(0, 2))):
    print(f"{sucursal[i]}: {total}")

# Total de ventas por día
print("\nVentas totales por día:")
for i, total in enumerate(ventas_matriz.sum(axis=(0, 1))):
    print(f"{fechas[i]}: {total}")
