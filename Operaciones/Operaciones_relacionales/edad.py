# Edad del usuario
edad = int(input("Ingrese su edad: "))

# Definir los límites de edad
edad_minima = 18
edad_maxima = 45

# Validar si la edad está dentro del rango permitido
if edad_minima <= edad <= edad_maxima:
    print(f"✅ Con {edad} años, puedes participar en el evento.")
elif edad < edad_minima:
    diferencia = edad_minima - edad
    print(f"⚠️ Con {edad} años, no puedes participar. Te faltan {diferencia} años para cumplir con la edad mínima de {edad_minima}.")
else:  # edad > edad_maxima
    exceso = edad - edad_maxima
    print(f"⚠️ Con {edad} años, no puedes participar. Excedes la edad máxima permitida por {exceso} años.")