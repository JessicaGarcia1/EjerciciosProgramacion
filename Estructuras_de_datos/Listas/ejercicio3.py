class Libro:
    def __init__(self, id_libro, titulo, autor, cantidad, precio):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def eliminar(self):
        self.cantidad = 0

class Inventario:
    def __init__(self):
        self.libros = []

    # Agregar un libro al inventario
    def agregar_libro(self, id_libro, titulo, autor, cantidad, precio):
        libro = Libro(id_libro, titulo, autor, cantidad, precio)
        self.libros.append(libro)

    # Buscar libro por ID
    def buscar_libro(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        return None

    # Actualizar cantidad de un libro
    def actualizar_libro(self, id_libro, cantidad):
        libro = self.buscar_libro(id_libro)
        if libro:
            libro.actualizar_cantidad(cantidad)
            print(f"Libro '{libro.titulo}' actualizado. Nueva cantidad: {libro.cantidad}")
        else:
            print("Libro no encontrado.")

    # Eliminar libro del inventario
    def eliminar_libro(self, id_libro):
        libro = self.buscar_libro(id_libro)
        if libro:
            libro.eliminar()
            print(f"Libro '{libro.titulo}' eliminado del inventario.")
        else:
            print("Libro no encontrado.")

    # Generar informe de libros con baja cantidad
    def generar_informe_baja_cantidad(self):
        print("\nInforme de Libros con Baja Cantidad (menos de 5 unidades):")
        for libro in self.libros:
            if libro.cantidad < 5:
                print(libro)

    # Mostrar todos los libros en inventario
    def mostrar_inventario(self):
        if not self.libros:
            print("El inventario está vacío.")
            return
        print("\nInventario de Libros:")
        for libro in self.libros:
            print(libro)

# Programa principal
inventario = Inventario()

while True:
    print("\nOpciones:")
    print("1. Agregar libro")
    print("2. Actualizar cantidad de libro")
    print("3. Eliminar libro")
    print("4. Generar informe de libros con baja cantidad")
    print("5. Mostrar inventario")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        id_libro = input("Ingrese el ID del libro: ").strip()
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad de libros: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
            continue
        try:
            precio = float(input("Ingrese el precio del libro: "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
            continue
        inventario.agregar_libro(id_libro, titulo, autor, cantidad, precio)

    elif opcion == 2:
        id_libro = input("Ingrese el ID del libro a actualizar: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad a agregar (puede ser negativa): "))
            inventario.actualizar_libro(id_libro, cantidad)
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    elif opcion == 3:
        id_libro = input("Ingrese el ID del libro a eliminar: ").strip()
        inventario.eliminar_libro(id_libro)

    elif opcion == 4:
        inventario.generar_informe_baja_cantidad()

    elif opcion == 5:
        inventario.mostrar_inventario()

    elif opcion == 6:
        print("Saliendo del sistema. ¡Gracias!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
