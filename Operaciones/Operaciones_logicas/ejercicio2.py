# Pedir información al usuario
es_cliente_frecuente = input("¿Eres cliente frecuente? (si/no): ").strip().lower()
compras_recientes = int(input("¿Cuántas compras has realizado en el último mes?: "))
monto_total = float(input("¿Cuál fue el monto total gastado en el último mes? ($): "))

# Evaluar si el cliente califica para la promoción
if (es_cliente_frecuente == "si" and compras_recientes >= 5) or monto_total >= 1000:
    print("✅ ¡Felicidades! Calificas para la promoción especial.")
else:
    print("⚠️ Lo sentimos, no calificas para la promoción en esta ocasión.")
descuento = monto_total * 0.10
print(f"🎉 Obtienes un descuento de ${descuento:.2f} en tu próxima compra.")
