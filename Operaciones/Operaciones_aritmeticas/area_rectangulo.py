# calcular el área del rectángulo
def calcular_area_rectangulo(ancho, altura):
    area = ancho * altura  # Fórmula: área = ancho * altura
    return area

# Solicitar el ancho y la altura
ancho = float(input("Ingrese el ancho del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Llamar a la función y mostrar el resultado
area = calcular_area_rectangulo(ancho, altura)
print(f"El área del rectángulo con ancho {ancho} y altura {altura} es: {area}")