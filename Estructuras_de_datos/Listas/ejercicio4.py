class Mesa:
    def __init__(self, id_mesa, capacidad):
        self.id_mesa = id_mesa
        self.capacidad = capacidad
        self.estado = "Disponible"  # Disponible u Ocupada

    def __str__(self):
        return f"Mesa {self.id_mesa}: Capacidad {self.capacidad} - Estado: {self.estado}"

    def ocupar(self):
        self.estado = "Ocupada"

    def liberar(self):
        self.estado = "Disponible"


class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, id_mesa, capacidad):
        mesa = Mesa(id_mesa, capacidad)
        self.mesas.append(mesa)

    def buscar_mesa(self, id_mesa):
        for mesa in self.mesas:
            if mesa.id_mesa == id_mesa:
                return mesa
        return None

    def reservar_mesa(self, id_mesa, num_comensales):
        mesa = self.buscar_mesa(id_mesa)
        if mesa:
            if mesa.estado == "Disponible" and num_comensales <= mesa.capacidad:
                mesa.ocupar()
                print(f"Mesa {id_mesa} reservada exitosamente para {num_comensales} comensales.")
            elif mesa.estado == "Ocupada":
                print(f"Mesa {id_mesa} ya está ocupada.")
            else:
                print(f"Mesa {id_mesa} no tiene suficiente capacidad para {num_comensales} comensales.")
        else:
            print("Mesa no encontrada.")

    def liberar_mesa(self, id_mesa):
        mesa = self.buscar_mesa(id_mesa)
        if mesa:
            if mesa.estado == "Ocupada":
                mesa.liberar()
                print(f"Mesa {id_mesa} liberada exitosamente.")
            else:
                print(f"Mesa {id_mesa} ya está disponible.")
        else:
            print("Mesa no encontrada.")

    def mostrar_estado_mesas(self):
        print("\nEstado de las mesas:")
        for mesa in self.mesas:
            print(mesa)

    def generar_informe_mesas_ocupadas(self):
        print("\nInforme de Mesas Ocupadas:")
        ocupadas = [mesa for mesa in self.mesas if mesa.estado == "Ocupada"]
        if ocupadas:
            for mesa in ocupadas:
                print(mesa)
        else:
            print("No hay mesas ocupadas en este momento.")


# Programa principal
restaurante = Restaurante()

# Agregar mesas al sistema
restaurante.agregar_mesa("M1", 2)
restaurante.agregar_mesa("M2", 4)
restaurante.agregar_mesa("M3", 6)
restaurante.agregar_mesa("M4", 8)

while True:
    print("\nOpciones:")
    print("1. Mostrar estado de las mesas")
    print("2. Reservar mesa")
    print("3. Liberar mesa")
    print("4. Generar informe de mesas ocupadas")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        restaurante.mostrar_estado_mesas()

    elif opcion == 2:
        id_mesa = input("Ingrese el ID de la mesa a reservar: ").strip()
        try:
            num_comensales = int(input("Ingrese el número de comensales: "))
            restaurante.reservar_mesa(id_mesa, num_comensales)
        except ValueError:
            print("Por favor, ingrese un número válido para el número de comensales.")

    elif opcion == 3:
        id_mesa = input("Ingrese el ID de la mesa a liberar: ").strip()
        restaurante.liberar_mesa(id_mesa)

    elif opcion == 4:
        restaurante.generar_informe_mesas_ocupadas()

    elif opcion == 5:
        print("¡Gracias!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
