# Solicitar al usuario el número de estudiantes y sus calificaciones
num_estudiantes = int(input("¿Cuántos estudiantes hay? "))
calificaciones = []

for i in range(num_estudiantes):
    calificacion = float(input(f"Calificación del estudiante {i+1}: "))
    calificaciones.append(calificacion)

# Procesar los datos
promedio = sum(calificaciones) / len(calificaciones)
aprobados = sum(1 for calificacion in calificaciones if calificacion >= 60)
calificaciones_ordenadas = sorted(calificaciones)

# Mostrar los resultados
print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Número de estudiantes aprobados: {aprobados}")
print(f"Calificaciones ordenadas: {calificaciones_ordenadas}")
