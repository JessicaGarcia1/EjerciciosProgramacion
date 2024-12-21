def busqueda_secuencial_cliente(lista_clientes, nombre_cliente):
    for cliente in lista_clientes:
        if cliente['nombre'] == nombre_cliente:
            return cliente  # Retorna el cliente completo
    return None  # Si no se encuentra el cliente, retorna None

clientes = [
    {"nombre": "Juan Pérez", "telefono": "271-123-4356", "direccion": "Calle 12, Avenida 1, Cordoba"},
    {"nombre": "Ana Gómez", "telefono": "234-567-8901", "direccion": "Avenida 4, Orizaba"},
    {"nombre": "Carlos Ruiz", "telefono": "345-678-9012", "direccion": "Calle 7 y 9, Cordoba"}
]

nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")

cliente_encontrado = busqueda_secuencial_cliente(clientes, nombre_cliente)

if cliente_encontrado:
    print(f"Cliente encontrado: {cliente_encontrado}")
else:
    print(f"Cliente {nombre_cliente} no encontrado.")
