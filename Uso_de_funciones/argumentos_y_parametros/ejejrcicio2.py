def par_o_impar(numero, verificar_par=True):
    if verificar_par:
        return numero % 2 == 0
    else:
        return numero % 2 != 0

# Llamamos a la función pasando un número y un argumento booleano
numero = int(input("Ingresa un número: "))
resultado = par_o_impar(numero, verificar_par=True)
if resultado:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
