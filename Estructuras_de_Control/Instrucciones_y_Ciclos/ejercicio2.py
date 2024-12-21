#Elegir opciones de un menú
print("Menú de opciones:")
print("1. Ver saldo")
print("2. Realizar un depósito")
print("3. Retirar dinero")
print("4. Salir")

opcion = int(input("Selecciona una opción (1-4): "))

if opcion == 1:
    saldo = 1000.23
    print(f"📊 Mostrando saldo actual ${saldo:,.2f}")
elif opcion == 2:
    print("💰 Ingrese el monto a depositar.")
elif opcion == 3:
    print("🏧 Ingrese el monto a retirar.")
elif opcion == 4:
    print("👋 Gracias por usar nuestros servicios. ¡Adiós!")
else:
    print("⚠️ Opción inválida. Intenta de nuevo.")
