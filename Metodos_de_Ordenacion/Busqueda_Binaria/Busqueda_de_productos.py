# búsqueda binaria para encontrar el producto en un almacén específico
def busqueda_binaria_productos(almacen, producto_objetivo):
    inicio = 0
    fin = len(almacen) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        producto = almacen[medio]
        
        if producto['nombre'] == producto_objetivo:
            return producto  # Retorna el producto encontrado
        elif producto['nombre'] < producto_objetivo:
            inicio = medio + 1  # Ignorar la mitad izquierda
        else:
            fin = medio - 1  # Ignorar la mitad derecha
    
    return None  # Si no se encuentra el producto

# Listas de productos ordenados por nombre dentro de cada almacén
almacen_rescate = [
    {'nombre': 'Filtro de Aire', 'cantidad': 50},
    {'nombre': 'Batería', 'cantidad': 20},
    {'nombre': 'Frenos', 'cantidad': 10},
    {'nombre': 'Aceite', 'cantidad': 30},
]

almacen_red_total = [
    {'nombre': 'Filtro de Combustible', 'cantidad': 100},
    {'nombre': 'Aceite', 'cantidad': 60},
    {'nombre': 'Frenos', 'cantidad': 25},
    {'nombre': 'Batería', 'cantidad': 15},
]

almacen_mx = [
    {'nombre': 'Aceite', 'cantidad': 40},
    {'nombre': 'Filtro de Aire', 'cantidad': 75},
    {'nombre': 'Frenos', 'cantidad': 50},
    {'nombre': 'Batería', 'cantidad': 60},
]

almacen_ultrashif = [
    {'nombre': 'Batería', 'cantidad': 30},
    {'nombre': 'Filtro de Aire', 'cantidad': 100},
    {'nombre': 'Aceite', 'cantidad': 25},
    {'nombre': 'Frenos', 'cantidad': 40},
]

# Diccionario de almacenes
almacenes = {
    'Almacén de Rescate': almacen_rescate,
    'Almacén de Red Total': almacen_red_total,
    'Almacén de MX': almacen_mx,
    'Almacén de Ultrashif': almacen_ultrashif,
}

# Mostrar la lista de almacenes disponibles
print("Almacenes disponibles:")
for nombre_almacen in almacenes.keys():
    print(f"- {nombre_almacen}")

# Solicitar al usuario el almacén y el producto a buscar
almacen_objetivo = input("Ingrese el nombre del almacén: ")
producto_objetivo = input("Ingrese el nombre del producto que desea buscar: ")

# Verificar si el almacén existe
if almacen_objetivo in almacenes:
    almacen = almacenes[almacen_objetivo]
    
    producto_encontrado = busqueda_binaria_productos(almacen, producto_objetivo)
    
    if producto_encontrado:
        print("\nProducto encontrado:")
        print(f"Producto: {producto_encontrado['nombre']}")
        print(f"Cantidad disponible: {producto_encontrado['cantidad']} unidades")
    else:
        print("\nNo se encontró el producto en este almacén.")
else:
    print("\nEl almacén ingresado no existe.")
