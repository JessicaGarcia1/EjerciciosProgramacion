# Inventario (lista de diccionarios)
inventario = [
    {"producto": "Laptop", "cantidad": 10},
    {"producto": "Mouse", "cantidad": 25},
    {"producto": "Teclado", "cantidad": 15},
    {"producto": "Monitor", "cantidad": 18}
]

# Buscar productos con cantidad menor a 20
print("Productos con bajo inventario:")
for item in inventario:  # Recorre cada producto
    if item["cantidad"] < 20:  # Aqui indicamos si la cantidad es menor a 20
        print(f"Producto: {item['producto']}, Cantidad: {item['cantidad']}")
