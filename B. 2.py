# Realice un programa que calcule X números aleatorios en un rango determinado por el usuario
import random

print("GENERADOR DE NUMEROS ALEATORIOS")
print("--------------------------------")

# Entrada de datos
cant = int(input("¿Cuántos números desea generar?: "))
min = int(input("Ingrese el valor mínimo del rango: "))
max = int(input("Ingrese el valor máximo del rango: "))

print("\nNúmeros generados:")

# Generación de números aleatorios
for i in range(cant):
    numero = random.randint(min, max)
    print(f"Número {i+1}: {numero}")
