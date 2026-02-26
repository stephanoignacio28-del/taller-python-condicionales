"""
EJERCICIO 3 — descuento tienda
Archivo: 03_descuento.py
Pedir:
subtotal (float)  
tipo_cliente (vip o regular)

Reglas:

Si es vip:
15% de descuento.

Si es regular:
5% solo si subtotal >= 100  
si no, no hay descuento.

Mostrar:
subtotal  
descuento aplicado  
total final  
"""
subtotal = -1.0
while subtotal < 0:
    subtotal = float(input("Introduce el subtotal de la compra: "))
    if subtotal < 0:
        print("Error: El subtotal no puede ser negativo. Inténtalo de nuevo.")
tipo_cliente = input("Introduce tipo de cliente (vip / regular): ").lower()
descuento_aplicado = 0.0

if tipo_cliente == "vip":
    descuento_aplicado = subtotal * 0.15 
elif tipo_cliente == "regular":
    if subtotal >= 100:
        descuento_aplicado = subtotal * 0.05 
    else:
        descuento_aplicado = 0.0 
total_final = subtotal - descuento_aplicado
print("-" * 30)
print(f"Subtotal: ${subtotal:.2f}") 
print(f"Descuento aplicado: ${descuento_aplicado:.2f}") 
print(f"Total final: ${total_final:.2f}") 