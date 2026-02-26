"""
EJERCICIO 4 — TARIFA DE TAXI (explicación clara)
Archivo: 04_taxi.py

Este ejercicio simula una aplicación real.
Debes calcular el costo de un viaje en taxi.

Pedir al usuario:
1) Distancia recorrida en km (float)
2) Hora del viaje (número entre 0 y 23)

Reglas del sistema:

TODOS los viajes empiezan con:
Tarifa base = 1 dólar

Luego se suma el costo por km.
Si el viaje es en horario DIURNO:
Desde 6 hasta 19 horas
Costo por km = 0.50

Si el viaje es en horario NOCTURNO:
Desde 20 hasta 23
y desde 0 hasta 5
Costo por km = 0.65

Además:

Si el viaje es mayor a 10 km
se añade un recargo fijo de 2 dólares.
Debes mostrar:

Tipo de horario (día o noche)
Distancia recorrida
Costo total a pagar

Ejemplo esperado:

Horario: nocturno  
Distancia: 12 km  
Total a pagar: $9.80  

Este ejercicio evalúa:
- Condiciones múltiples
- Uso de AND / OR
- Uso de floats
- Pensamiento lógico
"""
distancia = -1.0
while distancia < 0:
    distancia = float(input("Distancia recorrida en km: "))
    if distancia < 0:
        print("Error: La distancia no puede ser negativa.")
hora = -1
while hora < 0 or hora > 23:
    hora = int(input("Hora del viaje (0-23): "))
    if hora < 0 or hora > 23:
        print("Error: La hora debe estar entre 0 y 23.")
tarifa_base = 1.0 
costo_km = 0.0
horario_tipo = ""
if 6 <= hora <= 19: 
    horario_tipo = "diurno"
    costo_km = 0.50 
else: 
    horario_tipo = "nocturno"
    costo_km = 0.65 
total = tarifa_base + (distancia * costo_km) 
if distancia > 10: 
    total += 2.0
print("\n" + "="*20)
print(f"Horario: {horario_tipo}") 
print(f"Distancia: {distancia} km")
print(f"Total a pagar: ${total:.2f}") 
print("="*20)