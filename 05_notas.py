"""
EJERCICIO 5 — CLASIFICADOR DE NOTAS (explicación clara)
Archivo: 05_notas.py

Simula un sistema académico.
Pedir al usuario 3 notas:
n1  
n2  
n3  

Las notas deben estar entre:
0 y 100

PRIMERO:
Validar que todas estén en ese rango.
Si alguna nota es menor que 0
o mayor que 100:

Mostrar:
"Error: nota inválida"

Y terminar el programa.

SI todas son válidas:

Calcular promedio.
Clasificar:

90 - 100 → Excelente  
80 - 89 → Muy bueno  
70 - 79 → Bueno  
60 - 69 → Supletorio  
menor a 60 → Reprobado  

Mostrar:

Notas ingresadas  
Promedio  
Clasificación final  

Este ejercicio evalúa:
- Validación de datos
- Condicionales múltiples
- Lógica académica real
"""

# 1. Entrada de datos
n1 = float(input("Ingresa la nota 1 (0-100): "))
n2 = float(input("Ingresa la nota 2 (0-100): "))
n3 = float(input("Ingresa la nota 3 (0-100): "))

# 2. Validación obligatoria con el operador OR
# Si la nota 1 es inválida O la nota 2 es inválida O la nota 3 es inválida:
if (n1 < 0 or n1 > 100) or (n2 < 0 or n2 > 100) or (n3 < 0 or n3 > 100):
    print("Error: nota inválida")
    # El programa termina aquí si entra en este bloque
else:
    # 3. Cálculo del promedio si todas las notas pasaron la validación
    promedio = (n1 + n2 + n3) / 3
    
    # 4. Clasificación según la escala académica [cite: 22]
    if promedio >= 90:
        clasificacion = "Excelente"
    elif promedio >= 80:
        clasificacion = "Muy bueno"
    elif promedio >= 70:
        clasificacion = "Bueno"
    elif promedio >= 60:
        clasificacion = "Supletorio"
    else:
        clasificacion = "Reprobado"

    # 5. Salida de resultados
    print("\n" + "-"*30)
    print(f"Notas ingresadas: {n1}, {n2}, {n3}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Clasificación final: {clasificacion}")
    print("-"*30)