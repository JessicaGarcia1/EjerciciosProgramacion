# Solicitar información al usuario
años_experiencia = int(input("Ingrese sus años de experiencia laboral: "))
sabe_python = input("¿Tienes conocimientos en Python? (si/no): ").strip().lower()
sabe_sql = input("¿Tienes conocimientos en SQL? (si/no): ").strip().lower()

# Evaluar si la persona califica para el trabajo
if años_experiencia >= 2 and (sabe_python == "si" or sabe_sql == "si"):
    print("✅ ¡Felicidades! Cumples con los requisitos para aplicar al trabajo.")
else:
    print("⚠️ Lo sentimos, no cumples con los requisitos para este puesto.")
5