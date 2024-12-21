import random
from datetime import datetime

class Pedido:
    def __init__(self, id_pedido, cliente, producto, cantidad, fecha_pedido):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.fecha_pedido = fecha_pedido

    def __repr__(self):
        return (f"ID Pedido: {self.id_pedido}, Cliente: {self.cliente}, "
                f"Producto: {self.producto}, Cantidad: {self.cantidad}, "
                f"Fecha: {self.fecha_pedido.strftime('%Y-%m-%d %H:%M:%S')}")

def quick_sort_pedidos(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_pedidos(arr, low, pi - 1)
        quick_sort_pedidos(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high].fecha_pedido  # Usamos la fecha del último pedido
    i = low - 1
    for j in range(low, high):
        if arr[j].fecha_pedido <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Lista de pedidos
pedidos = [
    Pedido(1, "Juan Pérez", "Filtro de Aire", 2, datetime(2024, 3, 15, 10, 30)),
    Pedido(2, "Ana Aguilar}", "Batería", 1, datetime(2024, 1, 12, 14, 45)),
    Pedido(3, "Carlos Ruiz", "Lámpara Trasera", 4, datetime(2024, 2, 5, 9, 15)),
    Pedido(4, "María López", "Neumático", 2, datetime(2024, 4, 2, 16, 0)),
    Pedido(5, "Luis Fernández", "Amortiguador", 1, datetime(2024, 1, 22, 18, 30)),
]

# Ordenar los pedidos por fecha utilizando Quick Sort
quick_sort_pedidos(pedidos, 0, len(pedidos) - 1)

# Mostrar los pedidos ordenados por fecha
print("Pedidos ordenados por fecha de llegada:")
for pedido in pedidos:
    print(pedido)

