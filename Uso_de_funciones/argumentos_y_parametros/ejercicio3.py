def concatenar_nombres(nombre, apellido, titulo="Sr."):
    return f"{titulo} {nombre} {apellido}"

# Pedimos al usuario que ingrese los valores
nombre_usuario = input("Ingresa el nombre: ")
apellido_usuario = input("Ingresa el apellido: ")
titulo_usuario = input("Ingresa el título (opcional, presiona Enter para usar 'Sr.'): ")

# Si el usuario no ingresa un título, se usa 'Sr.' por defecto
if not titulo_usuario:
    titulo_usuario = "Sr."

# Llamamos a la función con los valores ingresados
nombre_completo = concatenar_nombres(nombre_usuario, apellido_usuario, titulo_usuario)

print(f"Nombre completo: {nombre_completo}")
