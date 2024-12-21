def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not any(c.isdigit() for c in contrasena):
        return "La contraseña debe contener al menos un número."
    if not any(c.isupper() for c in contrasena):
        return "La contraseña debe contener al menos una letra mayúscula."
    if not any(c in "!@#$%^&*()" for c in contrasena):
        return "La contraseña debe contener al menos un carácter especial."
    return "Contraseña válida."

# Solicitar al usuario que ingrese una contraseña
contrasena_usuario = input("Ingresa tu contraseña para validar: ")

# Validar la contraseña ingresada
resultado = validar_contrasena(contrasena_usuario)

# Mostrar el resultado
print(resultado)
