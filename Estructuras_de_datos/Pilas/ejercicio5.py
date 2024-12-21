class GestionContenedores:
    def __init__(self, nombre_almacen):
        self.nombre_almacen = nombre_almacen
        self.contenedores = []  # Pila de contenedores vacíos

    def agregar_contenedor(self, contenedor):
        """Agrega un contenedor vacío a la pila."""
        self.contenedores.append(contenedor)
        print(f"Contenedor '{contenedor}' agregado al almacén '{self.nombre_almacen}'.")

    def utilizar_contenedor(self):
        """Retira el último contenedor vacío de la pila."""
        if self.contenedores:
            contenedor_utilizado = self.contenedores.pop()
            print(f"Contenedor '{contenedor_utilizado}' utilizado del almacén '{self.nombre_almacen}'.")
        else:
            print(f"No hay contenedores disponibles en el almacén '{self.nombre_almacen}'.")

    def mostrar_contenedores(self):
        """Muestra los contenedores vacíos disponibles."""
        if self.contenedores:
            print(f"Contenedores vacíos disponibles en el almacén '{self.nombre_almacen}':")
            for contenedor in reversed(self.contenedores):
                print(f"- {contenedor}")
        else:
            print(f"No hay contenedores vacíos en el almacén '{self.nombre_almacen}'.")

# Función principal interactiva
def menu_contenedores():
    nombre_almacen = input("Ingrese el nombre del almacén: ")
    gestion = GestionContenedores(nombre_almacen)

    while True:
        print("\nMenú de Gestión de Contenedores:")
        print("1. Agregar contenedor vacío")
        print("2. Utilizar contenedor")
        print("3. Mostrar contenedores disponibles")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contenedor = input("Ingrese el identificador del contenedor: ")
            gestion.agregar_contenedor(contenedor)

        elif opcion == "2":
            gestion.utilizar_contenedor()

        elif opcion == "3":
            gestion.mostrar_contenedores()

        elif opcion == "4":
            print("Regresa pronto")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

menu_contenedores()