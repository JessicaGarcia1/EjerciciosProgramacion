class GestionInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_refaccion(self, tipo_refaccion, stand, cantidad):
        if tipo_refaccion not in self.inventario:
            self.inventario[tipo_refaccion] = []
        self.inventario[tipo_refaccion].append({"stand": stand, "cantidad": cantidad})
        print(f"Agregado stand '{stand}' con {cantidad} unidades al inventario de '{tipo_refaccion}'.")

    def despachar_refaccion(self, tipo_refaccion, cantidad):
        if tipo_refaccion in self.inventario and self.inventario[tipo_refaccion]:
            total_despachado = 0
            while cantidad > 0 and self.inventario[tipo_refaccion]:
                stand_actual = self.inventario[tipo_refaccion][-1]
                if stand_actual["cantidad"] <= cantidad:
                    # Despachar todo el stand
                    cantidad -= stand_actual["cantidad"]
                    total_despachado += stand_actual["cantidad"]
                    print(f"Despachado stand '{stand_actual['stand']}' con {stand_actual['cantidad']} unidades.")
                    self.inventario[tipo_refaccion].pop()
                else:
                    # Despachar una parte del stand
                    stand_actual["cantidad"] -= cantidad
                    total_despachado += cantidad
                    print(f"Despachado {cantidad} unidades del stand '{stand_actual['stand']}'.")
                    cantidad = 0

            if cantidad > 0:
                print(f"Inventario insuficiente. Faltaron {cantidad} unidades por despachar.")
            print(f"Total despachado: {total_despachado} unidades de '{tipo_refaccion}'.")
        else:
            print(f"No hay inventario disponible para '{tipo_refaccion}'.")

    def mostrar_inventario(self):
        print("\nInventario actual:")
        for tipo_refaccion, stands in self.inventario.items():
            print(f"{tipo_refaccion}:")
            for stand in stands:
                print(f"  Stand '{stand['stand']}' - {stand['cantidad']} unidades")


# Función para interactuar con el usuario
def menu_interactivo():
    inventario = GestionInventario()
    while True:
        print("\nMenú:")
        print("1. Agregar refacción")
        print("2. Despachar refacción")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo_refaccion = input("Ingrese el tipo de refacción: ")
            stand = input("Ingrese el stand (ejemplo: 'Stand 1'): ")
            cantidad = int(input("Ingrese la cantidad: "))
            inventario.agregar_refaccion(tipo_refaccion, stand, cantidad)

        elif opcion == "2":
            tipo_refaccion = input("Ingrese el tipo de refacción a despachar: ")
            cantidad = int(input("Ingrese la cantidad a despachar: "))
            inventario.despachar_refaccion(tipo_refaccion, cantidad)

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            print("Regresa pronto")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del programa
menu_interactivo()