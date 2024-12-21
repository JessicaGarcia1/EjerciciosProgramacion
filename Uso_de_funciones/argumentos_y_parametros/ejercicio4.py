def calcular_media(*numeros):
    return sum(numeros) / len(numeros)

# se calcula la media de kos numeros que indicamos
media = calcular_media(5, 10, 15, 20)
print(f"La media de los números es: {media}")
