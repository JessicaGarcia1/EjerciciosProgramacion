# Almacenar productos en un inventario
inventario = []  # Lista vacía para guardar los productos

while True:
    print("\n=== Menú de Gestión de Inventario ===")
    print("1. Registrar nuevo producto")
    print("2. Ver productos en inventario")
    print("3. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1-3): "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue  # Regresa al inicio
    
    if opcion == 1:
        print("\n🔷 Opción 1 seleccionada: Registrar nuevo producto.")
        nombre_producto = input("Ingresa el nombre del producto: ").strip()  # Usamos .strip() para quitar espacios
        cantidad = input("Ingresa la cantidad del producto: ").strip()
        
        if nombre_producto and cantidad.isdigit():  # Verifica que el nombre no esté vacío y que la cantidad sea un número
            cantidad = int(cantidad)  # Convierte la cantidad a entero
            inventario.append({"producto": nombre_producto, "cantidad": cantidad})  # Guarda el producto como un diccionario
            print(f"✅ El producto '{nombre_producto}' con cantidad {cantidad} ha sido registrado exitosamente.\n")
        else:
            print("⚠️ El nombre o la cantidad no son válidos. Intenta de nuevo.\n")
    
    elif opcion == 2:
        print("\n🔷 Opción 2 seleccionada: Ver productos en inventario.")
        if inventario:
            print("📋 Inventario de productos:")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. Producto: {item['producto']} | Cantidad: {item['cantidad']}")
        else:
            print("⚠️ El inventario está vacío. Registra productos primero.\n")
    
    elif opcion == 3:
        print("\n👋 Nos Vemos Pronto\n")
        break  # Finaliza el bucle y el programa
    else:
        print("\n⚠️ Opción inválida. Por favor, selecciona un número válido.\n")
