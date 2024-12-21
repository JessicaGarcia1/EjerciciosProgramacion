# Variables iniciales
inventario = {"llantas": 20, "aceite": 50, "filtros": 30}
precios = {"llantas": 1000, "aceite": 200, "filtros": 300}
ganancias_totales = 0

# Menú interactivo
while True:
    print("\n--- Menú de Gestión de Ventas ---")
    print("1. Consultar inventario")
    print("2. Registrar una venta")
    print("3. Ver ganancias totales")
    print("4. Salir")

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue

    # Opciones del menú
    if opcion == 1:
        print("\n📦 Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto.capitalize()}: {cantidad} unidades")
    
    elif opcion == 2:
        print("\n🛒 Productos disponibles para la venta:")
        for producto, precio in precios.items():
            print(f"- {producto.capitalize()} (${precio:,.2f})")
        
        producto = input("Ingresa el producto que deseas vender: ").lower()
        if producto not in inventario:
            print("⚠️ Producto no encontrado en el inventario.")
            continue
        
        cantidad = int(input(f"¿Cuántas unidades de {producto} deseas vender? "))
        if cantidad > inventario[producto]:
            print("⚠️ No hay suficiente inventario para realizar la venta.")
        else:
            inventario[producto] -= cantidad
            total_venta = cantidad * precios[producto]
            ganancias_totales += total_venta
            print(f"✅ Venta registrada. Total: ${total_venta:,.2f}")
    
    elif opcion == 3:
        print(f"\n💰 Ganancias totales: ${ganancias_totales:,.2f}")
    
    elif opcion == 4:
        print("👋 Gracias por usar el sistema. ¡Hasta luego!")
        break
    
    else:
        print("⚠️ Opción inválida. Por favor, selecciona una opción válida.")
