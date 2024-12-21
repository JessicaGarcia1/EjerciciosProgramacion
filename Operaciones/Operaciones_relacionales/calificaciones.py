# Ingresar calificacion del estudiante
calificacion = float(input("Ingrese la calificación del estudiante (0 a 10): "))

# Verificar si la calificación es suficiente para aprobar
if calificacion >= 6:
    print(f"Estudiante aprobado con una calificación de {calificacion}.")
else:
    print(f"Estudiante reprobado con una calificación de {calificacion}.")