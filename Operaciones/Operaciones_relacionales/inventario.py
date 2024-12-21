# Pedir al usuario las cantidades de inventario y del pedido
inventario = int(input("Ingrese la cantidad actual de inventario: "))
pedido = int(input("Ingrese la cantidad solicitada por el cliente: "))

# Verificar si hay suficiente inventario para cumplir con el pedido
if inventario >= pedido:
    inventario_restante = inventario - pedido
    print(f"✅ Pedido completado. Quedan {inventario_restante} unidades en el inventario.")
else:
    faltante = pedido - inventario
    print(f"⚠️ Inventario insuficiente. Faltan {faltante} unidades para completar el pedido.")