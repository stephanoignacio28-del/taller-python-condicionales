"""
EJERCICIO 1 — saludo formateado
Archivo: 01_saludo_formateado.py

Pedir:
- nombre  
- edad  
- ciudad  

Mostrar:
Hola Juan, tienes 20 años y vives en Quito

Usar:
input, int, f-string  
"""
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
while edad < 0:
    print("La edad no puede ser negativa. Por favor, introduce una edad válida.")
    edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ")
print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}")