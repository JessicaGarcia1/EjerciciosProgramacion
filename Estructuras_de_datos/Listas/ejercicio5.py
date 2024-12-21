class Libro:
    def __init__(self, titulo, autor, genero, precio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False


class Libreria:
    def __init__(self):
        self.inventario = []

    def agregar_libro(self, titulo, autor, genero, precio, cantidad):
        libro = Libro(titulo, autor, genero, precio, cantidad)
        self.inventario.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente al inventario.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.inventario:
            if getattr(libro, criterio, "").lower() == valor.lower():
                resultados.append(libro)
        return resultados

    def registrar_venta(self, titulo, cantidad):
        for libro in self.inventario:
            if libro.titulo.lower() == titulo.lower():
                if libro.vender(cantidad):
                    print(f"Venta registrada: {cantidad} unidades de '{titulo}'.")
                else:
                    print(f"No hay suficientes ejemplares de '{titulo}' en el inventario.")
                return
        print(f"El libro '{titulo}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        if self.inventario:
            print("\nInventario actual:")
            for libro in self.inventario:
                print(libro)
        else:
            print("El inventario está vacío.")

    def generar_informe(self):
        print("\nInforme de inventario:")
        agotados = [libro for libro in self.inventario if libro.cantidad == 0]
        disponibles = [libro for libro in self.inventario if libro.cantidad > 0]

        if disponibles:
            print("\nLibros disponibles:")
            for libro in disponibles:
                print(libro)
        else:
            print("\nNo hay libros disponibles.")

        if agotados:
            print("\nLibros agotados:")
            for libro in agotados:
                print(libro)
        else:
            print("\nNo hay libros agotados.")


# Programa
libreria = Libreria()

while True:
    print("\nOpciones:")
    print("1. Mostrar inventario")
    print("2. Agregar libro")
    print("3. Registrar venta")
    print("4. Buscar libro")
    print("5. Generar informe de inventario")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        libreria.mostrar_inventario()

    elif opcion == 2:
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        genero = input("Ingrese el género del libro: ").strip()
        try:
            precio = float(input("Ingrese el precio del libro: "))
            cantidad = int(input("Ingrese la cantidad inicial del libro: "))
            libreria.agregar_libro(titulo, autor, genero, precio, cantidad)
        except ValueError:
            print("Por favor, ingrese valores válidos para el precio y la cantidad.")

    elif opcion == 3:
        titulo = input("Ingrese el título del libro vendido: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            libreria.registrar_venta(titulo, cantidad)
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    elif opcion == 4:
        print("Criterios de búsqueda: 'titulo', 'autor', 'genero'")
        criterio = input("Ingrese el criterio de búsqueda: ").strip()
        valor = input(f"Ingrese el valor para buscar por {criterio}: ").strip()
        resultados = libreria.buscar_libro(criterio, valor)
        if resultados:
            print("\nResultados de la búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio}: {valor}")

    elif opcion == 5:
        libreria.generar_informe()

    elif opcion == 6:
        print("¡Gracias!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
