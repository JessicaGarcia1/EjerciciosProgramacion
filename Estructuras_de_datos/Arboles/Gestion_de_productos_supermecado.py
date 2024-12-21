class NodoProducto:
    def __init__(self, nombre, stock=None):
        self.nombre = nombre
        self.stock = stock  # Cantidad en inventario
        self.subproductos = []

    def agregar_subproducto(self, subproducto):
        self.subproductos.append(subproducto)

    def actualizar_stock(self, cantidad):
        if self.stock is not None:
            self.stock += cantidad

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock})" if self.stock is not None else self.nombre


class ArbolInventario:
    def __init__(self, raiz):
        self.raiz = raiz

    def buscar_producto(self, nombre, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual.nombre.lower() == nombre.lower():
            return nodo_actual
        for subproducto in nodo_actual.subproductos:
            encontrado = self.buscar_producto(nombre, subproducto)
            if encontrado:
                return encontrado
        return None

    def agregar_producto(self, nombre_categoria, nuevo_nodo):
        categoria = self.buscar_producto(nombre_categoria)
        if categoria:
            categoria.agregar_subproducto(nuevo_nodo)
            print(f"Producto '{nuevo_nodo.nombre}' agregado bajo la categoría '{categoria.nombre}'.")
        else:
            print(f"La categoría '{nombre_categoria}' no fue encontrada.")

    def imprimir_inventario(self, nodo_actual=None, nivel=0):
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + str(nodo_actual))
        for subproducto in nodo_actual.subproductos:
            self.imprimir_inventario(subproducto, nivel + 1)

    def actualizar_stock_producto(self, nombre_producto, cantidad):
        producto = self.buscar_producto(nombre_producto)
        if producto and producto.stock is not None:
            producto.actualizar_stock(cantidad)
            print(f"Stock actualizado: {producto}")
        elif producto:
            print(f"'{nombre_producto}' no es un producto final, no se puede actualizar el stock.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")


# Sistema
print("=== Gestión de Inventario en Supermercados ===")

# Crear el Supermercado
nombre_cadena = input("Ingrese el nombre de la cadena de supermercados: ")
supermercado = NodoProducto(nombre_cadena)
arbol_inventario = ArbolInventario(supermercado)

while True:
    print("\nOpciones:")
    print("1. Agregar categoría o producto")
    print("2. Imprimir inventario")
    print("3. Actualizar stock de producto")
    print("4. Buscar producto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar nodo
        nombre_categoria = input("Ingrese el nombre de la categoria: ")
        nombre_producto = input("Ingrese el nombre del producto o subcategoría: ")
        es_producto_final = input("¿Es un producto final? (sí/no): ").lower() == "sí"

        if es_producto_final:
            stock = int(input(f"Ingrese el stock inicial para '{nombre_producto}': "))
            nuevo_nodo = NodoProducto(nombre_producto, stock)
        else:
            nuevo_nodo = NodoProducto(nombre_producto)

        arbol_inventario.agregar_producto(nombre_categoria, nuevo_nodo)

    elif opcion == "2":
        print("\nInventario del supermercado:")
        arbol_inventario.imprimir_inventario()

    elif opcion == "3":
        # Actualizar stock
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        cantidad = int(input("Ingrese la cantidad a agregar o restar (use valores negativos para restar): "))
        arbol_inventario.actualizar_stock_producto(nombre_producto, cantidad)

    elif opcion == "4":
        # Buscar nodo
        nombre_busqueda = input("Ingrese el nombre de la categoría o producto a buscar: ")
        nodo = arbol_inventario.buscar_producto(nombre_busqueda)
        if nodo:
            print(f"Encontrado: {nodo}")
        else:
            print(f"No se encontró la categoría o producto '{nombre_busqueda}'.")

    elif opcion == "5":
        # Salir
        print("Vuelve Pronto")
        break

    else:
        print("Opción no válida. Intente nuevamente.")