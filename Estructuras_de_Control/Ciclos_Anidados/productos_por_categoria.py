# Inventario de productos por categoría
inventario = {
    "Frutas": ["Manzana", "Plátano", "Naranja"],
    "Verduras": ["Zanahoria", "Lechuga", "Pepino"],
    "Lácteos": ["Leche", "Yogur", "Queso"]
}

print("\n📦 Inventario de productos por categoría:\n")
for categoria, productos in inventario.items():  # Itera por categorías y productos
    print(f"🔷 Categoría: {categoria}")
    for producto in productos:  # Itera sobre la lista de productos en cada categoría
        print(f"    - {producto}")  # Muestra cada producto
    print()  # Línea en blanco después de cada categoría
