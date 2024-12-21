n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Imprime espacios
    for j in range(1, i + 1):
        print(j, end=" ")  # Imprime números
    print()  # Salto de línea
