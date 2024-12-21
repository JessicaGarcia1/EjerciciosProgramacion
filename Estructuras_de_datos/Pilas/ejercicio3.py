class SistemaTareas:
    def __init__(self):
        self.pila_tareas = []  # Pila que almacenará las tareas a procesar

    def registrar_tarea(self, tarea):
        """Registra una tarea a la pila."""
        self.pila_tareas.append(tarea)
        print(f"Tarea '{tarea}' registrada.")

    def completar_tarea(self):
        """Marca la tarea más reciente como completada."""
        if self.pila_tareas:
            tarea = self.pila_tareas.pop()  # Se elimina la última tarea asignada
            print(f"Tarea '{tarea}' completada.")
        else:
            print("No hay tareas pendientes.")

    def mostrar_tareas(self):
        """Muestra las tareas pendientes."""
        if self.pila_tareas:
            print("Tareas pendientes:")
            for tarea in self.pila_tareas:
                print(f"- {tarea}")
        else:
            print("No hay tareas pendientes.")

# Función interactiva para el usuario
def menu_tareas():
    sistema = SistemaTareas()
    while True:
        print("\nMenú de Gestión de Tareas:")
        print("1. Registrar tarea")
        print("2. Completar tarea")
        print("3. Mostrar tareas pendientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la descripción de la tarea: ")
            sistema.registrar_tarea(tarea)

        elif opcion == "2":
            sistema.completar_tarea()

        elif opcion == "3":
            sistema.mostrar_tareas()

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
menu_tareas()