class InventarioRefacciones:
    def __init__(self):
        self.inventario = {}  # Almacenará las refacciones y sus cantidades en el inventario

    def agregar_refaccion(self, refaccion, cantidad, precio):
        """Agrega refacciones al inventario."""
        if refaccion not in self.inventario:
            self.inventario[refaccion] = {'cantidad': 0, 'precio': precio}
        self.inventario[refaccion]['cantidad'] += cantidad
        print(f"Agregado: {cantidad} unidades de '{refaccion}' a ${precio:.2f} cada una.")

    def vender_refaccion(self, refaccion, cantidad):
        """Realiza una venta de refacciones."""
        if refaccion in self.inventario and self.inventario[refaccion]['cantidad'] >= cantidad:
            total_costo = cantidad * self.inventario[refaccion]['precio']
            self.inventario[refaccion]['cantidad'] -= cantidad
            print(f"Venta realizada: {cantidad} unidades de '{refaccion}' por un total de ${total_costo:.2f}.")
        else:
            print(f"Error: No hay suficiente inventario de '{refaccion}' para vender {cantidad} unidades.")

    def devolver_refaccion(self, refaccion, cantidad):
        """Realiza una devolución de refacciones."""
        if refaccion in self.inventario:
            self.inventario[refaccion]['cantidad'] += cantidad
            total_reembolso = cantidad * self.inventario[refaccion]['precio']
            print(f"Devolución realizada: {cantidad} unidades de '{refaccion}' por un reembolso de ${total_reembolso:.2f}.")
        else:
            print(f"Error: No se puede devolver '{refaccion}' porque no está en el inventario.")

    def mostrar_inventario(self):
        """Muestra el inventario disponible."""
        print("\nInventario actual:")
        for refaccion, detalles in self.inventario.items():
            print(f"{refaccion}: {detalles['cantidad']} unidades a ${detalles['precio']:.2f} cada una.")


# Función interactiva para el usuario
def menu_inventario():
    inventario = InventarioRefacciones()
    while True:
        print("\nMenú:")
        print("1. Agregar refacción")
        print("2. Vender refacción")
        print("3. Devolver refacción")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            refaccion = input("Ingrese el nombre de la refacción: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio unitario: "))
            inventario.agregar_refaccion(refaccion, cantidad, precio)

        elif opcion == "2":
            refaccion = input("Ingrese el nombre de la refacción a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            inventario.vender_refaccion(refaccion, cantidad)

        elif opcion == "3":
            refaccion = input("Ingrese el nombre de la refacción a devolver: ")
            cantidad = int(input("Ingrese la cantidad a devolver: "))
            inventario.devolver_refaccion(refaccion, cantidad)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Gracias, hasta luego")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del programa
menu_inventario()