# Solicitar información del estudiante
promedio = float(input("Ingresa el promedio del estudiante (0-100): "))
asistencia = float(input("Ingresa el porcentaje de asistencia del estudiante (0-100): "))

# Evaluar si el estudiante aprueba
if promedio >= 70 and asistencia >= 80:
    print("✅ ¡Felicidades! El estudiante aprueba la materia.")
else:
    print("⚠️ El estudiante no aprueba la materia.")

    # Detallar las razones por las cuales no aprueba
    if promedio < 70:
        print("⚠️ No aprueba porque su promedio es menor a 70.")
    if asistencia < 80:
        print("⚠️ No aprueba porque su asistencia es menor al 80%.")
