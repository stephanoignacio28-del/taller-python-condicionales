"""
EJERCICIO 2 — par o impar + mayoría de edad
Archivo: 02_par_impar.py

Pedir un número entero.
Mostrar si es par o impar.

Luego pedir edad.
Mostrar si es mayor o menor de edad.

Usar:
if, else, %
"""
numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")
while numero < 0:
    print("El número no puede ser negativo. Por favor, introduce un número entero válido.")
    numero = int(input("Introduce un número entero: "))
edad = int(input("Ahora, introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")