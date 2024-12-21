class NodoRefaccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subnodos = []

    def agregar_subnodo(self, subnodo):
        self.subnodos.append(subnodo)

    def __str__(self):
        return self.nombre


class ArbolRefacciones:
    def __init__(self, raiz):
        self.raiz = raiz

    def buscar_nodo(self, nombre, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual.nombre.lower() == nombre.lower():
            return nodo_actual
        for subnodo in nodo_actual.subnodos:
            encontrado = self.buscar_nodo(nombre, subnodo)
            if encontrado:
                return encontrado
        return None

    def agregar_nodo(self, nombre_padre, nuevo_nodo):
        padre = self.buscar_nodo(nombre_padre)
        if padre:
            padre.agregar_subnodo(nuevo_nodo)
            print(f"Nodo '{nuevo_nodo.nombre}' agregado bajo '{padre.nombre}'.")
        else:
            print(f"El nodo padre '{nombre_padre}' no fue encontrado.")

    def imprimir_arbol(self, nodo_actual=None, nivel=0):
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + str(nodo_actual))
        for subnodo in nodo_actual.subnodos:
            self.imprimir_arbol(subnodo, nivel + 1)


# Programa principal
print("=== Sistema de Gestión de Refacciones ===")

# Crear la línea principal (raíz del árbol)
nombre_linea_principal = input("Ingrese el nombre de la línea principal (e.g., Horton, Fleetguard): ")
linea_principal = NodoRefaccion(nombre_linea_principal)
arbol_refacciones = ArbolRefacciones(linea_principal)

while True:
    print("\nOpciones:")
    print("1. Agregar línea, categoría o número de parte")
    print("2. Imprimir árbol de refacciones")
    print("3. Buscar línea, categoría o número de parte")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar nodo
        nombre_padre = input("Ingrese el nombre del nodo padre (línea o categoría): ")
        nombre_nuevo_nodo = input("Ingrese el nombre de la nueva línea, categoría o número de parte: ")
        nuevo_nodo = NodoRefaccion(nombre_nuevo_nodo)
        arbol_refacciones.agregar_nodo(nombre_padre, nuevo_nodo)

    elif opcion == "2":
        # Imprimir árbol
        print("\nÁrbol de refacciones:")
        arbol_refacciones.imprimir_arbol()

    elif opcion == "3":
        # Buscar nodo
        nombre_nodo = input("Ingrese el nombre de la línea, categoría o número de parte a buscar: ")
        nodo = arbol_refacciones.buscar_nodo(nombre_nodo)
        if nodo:
            print(f"Nodo encontrado: {nodo}")
        else:
            print(f"Nodo '{nombre_nodo}' no encontrado.")

    elif opcion == "4":
        # Salir
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
