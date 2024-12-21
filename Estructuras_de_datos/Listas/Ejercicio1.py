# Bahías de servicio
bahias = ["Bahía 1", "Bahía 2", "Bahía 3", "Bahía 4"]

# Unidades asignadas por modelo y bahía
tractocamiones_asignados = {bahia: {} for bahia in bahias}

# Estado de las bahías
estado_bahias = {bahia: "Disponible" for bahia in bahias}

# Asignacion de unidades a una bahía
def asignar_unidad(bahia, modelo, cantidad):
    if estado_bahias[bahia] == "Ocupada":
        print(f"La bahía '{bahia}' ya está ocupada. No se pueden asignar más unidades.")
        return

    if bahia in tractocamiones_asignados:
        tractocamiones_asignados[bahia][modelo] = cantidad
        estado_bahias[bahia] = "Ocupada"
        print(f"Se asignaron {cantidad} unidades del modelo '{modelo}' a la bahía '{bahia}', que ahora está ocupada.")
    else:
        print(f"La bahía '{bahia}' no existe.")

# FLiberacion de una bahía
def liberar_bahia(bahia):
    if estado_bahias[bahia] == "Disponible":
        print(f"La bahía '{bahia}' ya está disponible.")
        return

    tractocamiones_asignados[bahia].clear()
    estado_bahias[bahia] = "Disponible"
    print(f"La bahía '{bahia}' ha sido desocupada y está disponible nuevamente.")

# Gernerar un reporte de las bahías
def generar_reporte():
    print("\n--- Reporte de Bahías ---")
    for bahia, estado in estado_bahias.items():
        print(f"\n{bahia} ({estado}):")
        if estado == "Ocupada":
            for modelo, cantidad in tractocamiones_asignados[bahia].items():
                print(f"  Modelo '{modelo}': {cantidad} unidades asignadas.")
        else:
            print("  Sin unidades asignadas.")
    print("---------------------------------")

# Programa
print("Bienvenido al sistema de asignación de bahías del taller\n")

while True:
    print("\nOpciones:")
    print("1. Asignar unidad a una bahía")
    print("2. Liberar una bahía")
    print("3. Ver reporte de bahías")
    print("4. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        print("\nBahías disponibles:")
        for bahia, estado in estado_bahias.items():
            print(f"  - {bahia} ({estado})")
        
        bahia_seleccionada = input("\nIngrese el nombre de la bahía: ").strip()
        if bahia_seleccionada not in bahias:
            print("La bahía ingresada no existe. Inténtelo nuevamente.")
            continue
        
        modelo = input("Ingrese el modelo del tractocamión (ejemplo: Kenworth T680): ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad de unidades a asignar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue
        except ValueError:
            print("Debe ingresar un número válido para la cantidad.")
            continue

        asignar_unidad(bahia_seleccionada, modelo, cantidad)

    elif opcion == 2:
        bahia_seleccionada = input("\nIngrese el nombre de la bahía a liberar: ").strip()
        if bahia_seleccionada not in bahias:
            print("La bahía ingresada no existe. Inténtelo nuevamente.")
            continue

        liberar_bahia(bahia_seleccionada)

    elif opcion == 3:
        generar_reporte()

    elif opcion == 4:
        print("Saliendo del sistema. ¡Gracias!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")