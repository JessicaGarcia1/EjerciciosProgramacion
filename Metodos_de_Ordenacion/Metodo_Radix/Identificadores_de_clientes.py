# contar el número de dígitos de un número
def obtener_max_digitos(lista):
    maximo = max(lista)  # Encuentra el número más grande
    return len(str(maximo))  # Cuenta los dígitos del número más grande

# Se obtiene el dígito de una posición específica
def obtener_digito(numero, posicion):
    return (numero // (10 ** posicion)) % 10

# Metodo Radix
def radix_sort(lista):
    max_digitos = obtener_max_digitos(lista)  # Número máximo de dígitos
    for posicion in range(max_digitos):
        # Crear 10 "cubetas" (listas) para cada dígito (0-9)
        cubetas = [[] for _ in range(10)]
        
        # Colocar cada número en la cubeta correspondiente según el dígito actual
        for numero in lista:
            digito = obtener_digito(numero, posicion)
            cubetas[digito].append(numero)
        
        # Combinar todas las cubetas para formar la lista ordenada parcial
        lista = [numero for cubeta in cubetas for numero in cubeta]
    
    return lista

# Datos iniciales: identificadores de clientes
identificadores_clientes = [
    10234, 5643, 128, 40321, 20987, 675, 9000, 4321, 89123, 7
]

# Mostrar identificadores originales
print("Identificadores de clientes originales:")
print(identificadores_clientes)

# Ordenar identificadores usando Metodo Radix
identificadores_ordenados = radix_sort(identificadores_clientes)

# Mostrar identificadores ordenados
print("\nIdentificadores de clientes ordenados:")
print(identificadores_ordenados)
