class InspeccionCalidad:
    def __init__(self, producto):
        self.producto = producto
        self.tareas = []  # Pila de tareas para el producto

    def agregar_tarea(self, tarea):
        """Agrega una tarea de inspección a la pila."""
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada al producto '{self.producto}'.")

    def completar_tarea(self):
        """Completa la última tarea agregada."""
        if self.tareas:
            tarea_realizada = self.tareas.pop()
            print(f"Tarea '{tarea_realizada}' completada para el producto '{self.producto}'.")
        else:
            print(f"No hay tareas pendientes para el producto '{self.producto}'.")

    def mostrar_tareas(self):
        """Muestra las tareas pendientes."""
        if self.tareas:
            print(f"Tareas pendientes para el producto '{self.producto}':")
            for tarea in reversed(self.tareas):  # Mostramos la pila de arriba hacia abajo
                print(f"- {tarea}")
        else:
            print(f"Todas las tareas para el producto '{self.producto}' han sido completadas.")

# Función interactiva para el usuario
def menu_inspeccion():
    producto = input("Ingrese el nombre del producto a inspeccionar: ")
    inspeccion = InspeccionCalidad(producto)

    while True:
        print("\nMenú de Inspección de Calidad:")
        print("1. Agregar tarea de inspección")
        print("2. Completar tarea")
        print("3. Mostrar tareas pendientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la descripción de la tarea: ")
            inspeccion.agregar_tarea(tarea)

        elif opcion == "2":
            inspeccion.completar_tarea()

        elif opcion == "3":
            inspeccion.mostrar_tareas()

        elif opcion == "4":
            print("Regresa pronto")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
menu_inspeccion()
