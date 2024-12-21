# Lista de los estudiantes
lista_estudiantes = []  # Esta lista debe declararse solo una vez, antes del bucle

while True:
    print("\n=== Menú Principal ===")
    print("1. Registrar nuevo estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1-3): "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue  # Regresa al inicio del bucle si hay error en la entrada
    
    if opcion == 1:
        print("\n🔷 Opción 1 seleccionada: Registrar nuevo estudiante.")
        nombre = input("Ingresa el nombre del estudiante: ").strip()  # Usamos .strip() para quitar espacios al inicio y final
        if nombre:  # Verifica que el nombre no esté vacío
            lista_estudiantes.append(nombre)  # Agrega el nombre a la lista
            print(f"✅ {nombre} ha sido registrado exitosamente.\n")
        else:
            print("⚠️ El nombre no puede estar vacío. Intenta de nuevo.\n")
    
    elif opcion == 2:
        print("\n🔷 Opción 2 seleccionada: Ver lista de estudiantes.")
        if lista_estudiantes:
            print("📋 Lista de estudiantes registrados:")
            for i, estudiante in enumerate(lista_estudiantes, start=1):
                print(f"{i}. {estudiante}")
        else:
            print("⚠️ La lista está vacía. Registra estudiantes primero.\n")
    
    elif opcion == 3:
        print("\n👋 ¡Gracias! Hasta luego.\n")
        break  # Finaliza el bucle y el programa
    
    else:
        print("\n⚠️ Opción inválida. Por favor, selecciona un número válido.\n")