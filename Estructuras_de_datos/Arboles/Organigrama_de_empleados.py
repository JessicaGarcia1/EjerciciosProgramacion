class NodoEmpleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"


class ArbolOrganizacional:
    def __init__(self, director):
        self.raiz = director

    def buscar_empleado(self, nombre, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual.nombre.lower() == nombre.lower():
            return nodo_actual
        for subordinado in nodo_actual.subordinados:
            encontrado = self.buscar_empleado(nombre, subordinado)
            if encontrado:
                return encontrado
        return None

    def agregar_empleado(self, nombre_jefe, empleado):
        jefe = self.buscar_empleado(nombre_jefe)
        if jefe:
            jefe.agregar_subordinado(empleado)
            print(f"Empleado {empleado.nombre} agregado bajo el mando de {jefe.nombre}.")
        else:
            print(f"Jefe {nombre_jefe} no encontrado.")

    def imprimir_organigrama(self, nodo_actual=None, nivel=0):
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + str(nodo_actual))
        for subordinado in nodo_actual.subordinados:
            self.imprimir_organigrama(subordinado, nivel + 1)


# Organigrama
print("=== Sistema de Gestión de Empleados ===")

# Aqui se crea al director general
nombre_director = input("Ingrese el nombre del Director General: ")
puesto_director = input("Ingrese el puesto del Director General: ")
director_general = NodoEmpleado(nombre_director, puesto_director)
organigrama = ArbolOrganizacional(director_general)

while True:
    print("\nOpciones:")
    print("1. Agregar empleado")
    print("2. Imprimir organigrama")
    print("3. Buscar empleado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar empleado
        nombre_jefe = input("Ingrese el nombre del jefe: ")
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        puesto_empleado = input("Ingrese el puesto del empleado: ")
        nuevo_empleado = NodoEmpleado(nombre_empleado, puesto_empleado)
        organigrama.agregar_empleado(nombre_jefe, nuevo_empleado)

    elif opcion == "2":
        # Imprimir organigrama
        print("\nOrganigrama de la empresa:")
        organigrama.imprimir_organigrama()

    elif opcion == "3":
        # Buscar empleado
        nombre_empleado = input("Ingrese el nombre del empleado a buscar: ")
        empleado = organigrama.buscar_empleado(nombre_empleado)
        if empleado:
            print(f"Empleado encontrado: {empleado}")
        else:
            print(f"Empleado {nombre_empleado} no encontrado.")

    elif opcion == "4":
        # Salir
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
