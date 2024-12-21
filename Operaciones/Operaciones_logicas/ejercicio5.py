# Solicitar información
meta_ventas = float(input("Ingresa la meta de ventas para el mes ($): "))
ventas_totales = float(input("Ingresa las ventas totales realizadas ($): "))
numero_empleados = int(input("Ingresa el número de empleados responsables: "))

# Evaluar si se cumple la meta
if ventas_totales >= meta_ventas:
    print("✅ ¡Felicidades! Se cumplió la meta de ventas.")
    # Calcular el bono por empleado si se supera la meta
    if ventas_totales > meta_ventas:
        bono = (ventas_totales - meta_ventas) * 0.10 / numero_empleados
        print(f"🎉 Bono asignado a cada empleado: ${bono:,.2f}")
else:
    # Calcular el porcentaje alcanzado
    porcentaje = (ventas_totales / meta_ventas) * 100
    print("⚠️ No se cumplió la meta de ventas.")
    print(f"Solo se alcanzó el {porcentaje:.2f}% de la meta.")
