import numpy as np
import pandas as pd

# Cargar los CSV con los datos de ventas e inventarios
ventas_df = pd.read_csv(r"C:\Users\Jessica Garcia\OneDrive - Kenworth Del este\Escritorio\ventas.csv")
inventarios_df = pd.read_csv(r"C:\Users\Jessica Garcia\OneDrive - Kenworth Del este\Escritorio\inventarios.csv")

# Verificar los datos cargados
print("Datos de Ventas")
print(ventas_df)
print("\nDatos de Inventarios")
print(inventarios_df)

# Procesar las fechas en ventas.csv asegurando el formato correcto
ventas_df["Fecha"] = pd.to_datetime(ventas_df["Fecha"], dayfirst=True, errors="coerce")

# Mostrar filas con fechas no válidas para depuración
fechas_invalidas = ventas_df[ventas_df["Fecha"].isnull()]
if not fechas_invalidas.empty:
    print("\nAdvertencia: Se encontraron fechas no válidas:")
    print(fechas_invalidas)

# Filtrar datos con fechas válidas únicamente
ventas_df = ventas_df.dropna(subset=["Fecha"])

# Agrupar las fechas por mes
fechas = ventas_df["Fecha"].dt.to_period("M").unique()

# Obtener los valores únicos de cada dimensión
productos = ventas_df["Producto"].unique()
sucursales = ventas_df["Sucursal"].unique()

# Crear un arreglo tridimensional para las ventas: Producto x Sucursal x Mes
ventas_matriz = np.zeros((len(productos), len(sucursales), len(fechas)))

# Llenar el arreglo con las cantidades vendidas
for _, row in ventas_df.iterrows():
    try:
        fecha_procesada = row["Fecha"].to_period("M")
        fecha_idx = np.where(fechas == fecha_procesada)[0][0]
    except IndexError:
        print(f"Fecha no encontrada: {row['Fecha']}")
        continue  # Saltar esta fila si no se encuentra la fecha

    producto_idx = np.where(productos == row["Producto"])[0][0]
    sucursal_idx = np.where(sucursales == row["Sucursal"])[0][0]
    ventas_matriz[producto_idx, sucursal_idx, fecha_idx] += row["Cantidad"]

# Crear un arreglo para los inventarios iniciales: Producto x Sucursal
inventarios_matriz = np.zeros((len(productos), len(sucursales)))

# Llenar el arreglo con los inventarios iniciales
for _, row in inventarios_df.iterrows():
    try:
        producto_idx = np.where(productos == row["Producto"])[0][0]
        sucursal_idx = np.where(sucursales == row["Sucursal"])[0][0]
        inventarios_matriz[producto_idx, sucursal_idx] = row["Inventario Inicial"]
    except IndexError:
        print(f"Producto o Sucursal no encontrado en inventarios: {row}")
        continue  # Saltar filas con problemas               
                
# Cálculo de ventas totales por producto, sucursal y mes
print("\nVentas totales por producto, sucursal y mes:")
for i, producto in enumerate(productos):
    for j, sucursal in enumerate(sucursales):
        for k, mes in enumerate(fechas):
            total_ventas = ventas_matriz[i, j, k]
            if total_ventas > 0:  # Solo imprimir cuando las ventas sean mayores a 0
                # Usamos strftime para formatear la fecha completa
                fecha_formateada = mes.strftime("%d-%m-%Y")  # Formato día-mes-año
                print(f"{producto} - {sucursal} - {fecha_formateada}: {total_ventas} unidades")

# Calcular el total de inventarios restantes por producto y sucursal
inventarios_restantes = inventarios_matriz.copy()

# Restar las ventas de los inventarios
for i in range(len(productos)):
    for j in range(len(sucursales)):
        for k in range(len(fechas)):
            if ventas_matriz[i, j, k] > 0:
                inventarios_restantes[i, j] -= ventas_matriz[i, j, k]

# Imprimir inventarios restantes solo si son mayores que cero
print("\nInventarios restantes por producto y sucursal:")
for i, producto in enumerate(productos):
    for j, sucursal in enumerate(sucursales):
        if inventarios_restantes[i, j] > 0:  # Verificar si hay inventario restante
            print(f"{producto} - {sucursal}: {inventarios_restantes[i, j]} unidades restantes")
        
# Cálculo de la rotación de inventarios (ventas / inventarios)
print("\nRotación de inventarios (ventas / inventarios):")
for i, producto in enumerate(productos):
    for j, sucursal in enumerate(sucursales):
        total_ventas = ventas_matriz[i, j, :].sum()
        inventario_inicial = inventarios_matriz[i, j]
        if inventario_inicial > 0:
            rotacion = total_ventas / inventario_inicial
        else:
            rotacion = 0
        
        # Solo imprimir si la rotación es mayor que 0
        if rotacion > 0:
            print(f"{producto} - {sucursal}: {rotacion:.2f}")
