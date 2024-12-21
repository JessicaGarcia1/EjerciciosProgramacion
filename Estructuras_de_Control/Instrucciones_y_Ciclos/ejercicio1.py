calificacion = float(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("🎉 Excelente: A")
elif calificacion >= 80:
    print("👍 Bueno: B")
elif calificacion >= 70:
    print("👌 Regular: C")
else:
    print("⚠️ Insuficiente: F")
