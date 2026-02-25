# Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro) donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen

import math

# FUNCIONES DE VOLUMEN

def volumen_prisma(largo, ancho, altura):
    return largo * ancho * altura

def volumen_piramide(largo, ancho, altura):
    return (largo * ancho * altura) / 3

def volumen_cono_truncado(R, r, h):
    return (1/3) * math.pi * h * (R**2 + R*r + r**2)

def volumen_cilindro(r, h):
    return math.pi * (r**2) * h


# main

print("CALCULO DE VOLUMENES")
print("---------------------")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione una opción (1-4): "))

if opcion == 1:
    largo = float(input("Ingrese el largo de la base: "))
    ancho = float(input("Ingrese el ancho de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = volumen_prisma(largo, ancho, altura)

elif opcion == 2:
    largo = float(input("Ingrese el largo de la base: "))
    ancho = float(input("Ingrese el ancho de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = volumen_piramide(largo, ancho, altura)

elif opcion == 3:
    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    volumen = volumen_cono_truncado(R, r, h)

elif opcion == 4:
    r = float(input("Ingrese el radio: "))
    h = float(input("Ingrese la altura: "))
    volumen = volumen_cilindro(r, h)

else:
    print("Opción no válida")
    volumen = None

# -impresion valor final

if volumen is not None:
    print(f"\nEl volumen del sólido es: {volumen} unidades cúbicas")