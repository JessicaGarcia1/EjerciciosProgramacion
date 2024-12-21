n = 50  # Hasta qué número buscar primos

print(f"Números primos entre 1 y {n}:")
for num in range(2, n + 1):  # Itera del 2 al número dado
    es_primo = True
    for divisor in range(2, int(num ** 0.5) + 1):  # Verifica divisores hasta la raíz cuadrada
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")