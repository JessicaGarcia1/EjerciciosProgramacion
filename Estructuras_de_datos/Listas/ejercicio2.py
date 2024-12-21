class InventarioRefacciones:
    def __init__(self):
        # La informacion se almacena en un diccionario que contiene el nombre de la refacción y su cantidad disponible
        self.inventario = []

    # Agregar una refacción al inventario
    def agregar_refaccion(self, nombre, cantidad):
        for refaccion in self.inventario:
            if refaccion["nombre"] == nombre:
                refaccion["cantidad"] += cantidad
                print(f"Se agregaron {cantidad} unidades de '{nombre}'.")
                return
        self.inventario.append({"nombre": nombre, "cantidad": cantidad})
        print(f"Se agregó {cantidad} unidades de '{nombre}' al inventario.")

    # Eliminar refacción del inventario
    def eliminar_refaccion(self, nombre, cantidad):
        for refaccion in self.inventario:
            if refaccion["nombre"] == nombre:
                if refaccion["cantidad"] >= cantidad:
                    refaccion["cantidad"] -= cantidad
                    print(f"Se eliminaron {cantidad} unidades de '{nombre}'.")
                else:
                    print(f"No hay suficientes unidades de '{nombre}' para eliminar.")
                return
        print(f"Refacción '{nombre}' no encontrada en el inventario.")

    # Consultar el stock de una refacción
    def consultar_stock(self, nombre):
        for refaccion in self.inventario:
            if refaccion["nombre"] == nombre:
                print(f"Stock de '{nombre}': {refaccion['cantidad']} unidades.")
                return
        print(f"Refacción '{nombre}' no encontrada en el inventario.")

    # Mostrar el inventario completo
    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return
        print("\nInventario de Refacciones:")
        for refaccion in self.inventario:
            print(f"{refaccion['nombre']}: {refaccion['cantidad']} unidades")


# Programa
inventario = InventarioRefacciones()

while True:
    print("\nOpciones:")
    print("1. Agregar refacción al inventario")
    print("2. Eliminar refacción del inventario")
    print("3. Consultar stock de una refacción")
    print("4. Mostrar inventario completo")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        nombre = input("Ingrese el nombre de la refacción: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
            continue
        inventario.agregar_refaccion(nombre, cantidad)

    elif opcion == 2:
        nombre = input("Ingrese el nombre de la refacción: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
            continue
        inventario.eliminar_refaccion(nombre, cantidad)

    elif opcion == 3:
        nombre = input("Ingrese el nombre de la refacción: ").strip()
        inventario.consultar_stock(nombre)

    elif opcion == 4:
        inventario.mostrar_inventario()

    elif opcion == 5:
        print("¡Gracias!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
