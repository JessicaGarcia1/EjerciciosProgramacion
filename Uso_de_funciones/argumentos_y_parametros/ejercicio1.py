def resta(*args):
    resultado = args[0]  # Comienza con el primer número
    for num in args[1:]:
        resultado -= num
    return resultado

# Llamamos a la función pasando varios argumentos
resultado = resta(10, 3, 2)
print(f"El resultado de la resta es: {resultado}")
