# Pedir información al usuario
edad = int(input("Ingrese su edad: "))
es_estudiante = input("¿Eres estudiante? (si/no): ").strip().lower()

# Evaluar si cumple las condiciones para el descuento
if (edad < 18 or edad > 60) and es_estudiante == "si":
    print("✅ ¡Felicidades! Calificas para un descuento especial.")
else:
    print("⚠️ Lo sentimos, no calificas para el descuento.")
