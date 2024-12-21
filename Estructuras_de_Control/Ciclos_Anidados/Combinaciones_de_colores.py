colores = ["rojo", "azul", "verde"]
formas = ["círculo", "cuadrado", "triángulo"]

# Generar combinaciones de colores y formas
print("Combinaciones:")
for color in colores:  # Recorre los colores
    for forma in formas:  # Recorre las formas
        print(f"{color} - {forma}")
