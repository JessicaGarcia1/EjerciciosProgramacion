# Suma
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    # Realizamos la suma
    resultado = numero1 + numero2
    
    # Imprimimos el resultado
    print("La suma de", numero1, "y", numero2, "es:", resultado)

except ValueError:
    print("Por favor ingresa solo números válidos.")

