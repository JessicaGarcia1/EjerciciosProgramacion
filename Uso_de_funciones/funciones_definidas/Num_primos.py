def numeros_primos(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if numero > 1:
            es_primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(numero)
    return primos

# Llamar a la función
print(f"Números primos entre 10 y 60: {numeros_primos(10, 60)}")
