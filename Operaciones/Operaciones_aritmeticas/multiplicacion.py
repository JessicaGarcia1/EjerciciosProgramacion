# multiplicacion
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    # operacion
    resultado = numero1 * numero2
    
    # resultado
    print("La multiplicación de", numero1, "y", numero2, "es:", resultado)

except ValueError:
    print("Por favor ingresa solo números válidos.")
