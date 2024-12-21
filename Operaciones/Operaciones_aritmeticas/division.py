# dividir dos números
def dividir():
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))

    # Verificar si el denominador no es cero
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        # Calcular la división
        resultado = num1 / num2
        # Mostrar el resultado
        print(f"La división de {num1} entre {num2} es: {resultado}")

# Llamar a la función
dividir()
