# Metodo burbuja
def bubble_sort_refacciones(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordenar por cantidad en inventario (ascendente)
            if lista[j]["cantidad"] > lista[j + 1]["cantidad"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            # Si las cantidades son iguales, ordenar por prioridad (descendente)
            elif lista[j]["cantidad"] == lista[j + 1]["cantidad"]:
                if lista[j]["prioridad"] < lista[j + 1]["prioridad"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Si las prioridades también son iguales, ordenar por margen de ganancia (descendente)
                elif lista[j]["prioridad"] == lista[j + 1]["prioridad"]:
                    if lista[j]["margen"] < lista[j + 1]["margen"]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

# buscar una refacción por código o nombre
def buscar_refaccion(lista, busqueda):
    for ref in lista:
        if ref["codigo"] == busqueda or ref["nombre"].lower() == busqueda.lower():
            return ref
    return None

# marcar como agotada una refacción
def marcar_agotada(lista, codigo):
    for ref in lista:
        if ref["codigo"] == codigo:
            ref["cantidad"] = 0
            return True
    return False

# generar alertas de reabastecimiento
def generar_alertas(lista, umbral):
    alertas = [ref for ref in lista if ref["cantidad"] < umbral]
    return alertas

# Datos iniciales
refacciones = [
    {"codigo": "R123", "nombre": "Filtro de Aire", "cantidad": 5, "prioridad": 2, "margen": 25},
    {"codigo": "R124", "nombre": "Filtro de Aceite", "cantidad": 10, "prioridad": 3, "margen": 20},
    {"codigo": "R125", "nombre": "Batería", "cantidad": 2, "prioridad": 1, "margen": 50},
    {"codigo": "R126", "nombre": "Sensor de Velocidad", "cantidad": 2, "prioridad": 2, "margen": 15},
    {"codigo": "R127", "nombre": "Embrague", "cantidad": 7, "prioridad": 3, "margen": 40},
]

# Umbral de inventario crítico
umbral_critico = 3

# Ordenar las refacciones
bubble_sort_refacciones(refacciones)

# Mostrar las refacciones ordenadas
print("\nRefacciones ordenadas:")
for ref in refacciones:
    print(ref)

# Buscar una refacción por código o nombre
busqueda = input("\nIngrese el código o nombre de la refacción a buscar: ")
resultado = buscar_refaccion(refacciones, busqueda)
if resultado:
    print(f"\nRefacción encontrada: {resultado}")
else:
    print("\nNo se encontró la refacción.")

# Marcar una refacción como agotada
codigo_agotar = input("\nIngrese el código de la refacción a marcar como agotada: ")
if marcar_agotada(refacciones, codigo_agotar):
    print("\nLa refacción ha sido marcada como agotada.")
else:
    print("\nNo se encontró la refacción para marcar como agotada.")

# Generar alertas de reabastecimiento
print("\nAlertas de reabastecimiento:")
alertas = generar_alertas(refacciones, umbral_critico)
if alertas:
    for alerta in alertas:
        print(f"Refacción {alerta['nombre']} (Código: {alerta['codigo']}) - Cantidad: {alerta['cantidad']}")
else:
    print("No hay refacciones con inventario crítico.")
