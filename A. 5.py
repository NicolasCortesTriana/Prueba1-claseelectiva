#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).

import math

# ----------------------------
# FUNCIONES DE ROTACIÓN
# ----------------------------

def rotacion_x(angulo_grados):
    theta = math.radians(angulo_grados)
    return [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)]
    ]

def rotacion_y(angulo_grados):
    theta = math.radians(angulo_grados)
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]

def rotacion_z(angulo_grados):
    theta = math.radians(angulo_grados)
    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ]

# ----------------------------
# PRUEBA DEL PROGRAMA
# ----------------------------

angulo = 45

Rx = rotacion_x(angulo)
Ry = rotacion_y(angulo)
Rz = rotacion_z(angulo)

print("Rotación en X (45°):")
for fila in Rx:
    print(fila)

print("\nRotación en Y (45°):")
for fila in Ry:
    print(fila)

print("\nRotación en Z (45°):")
for fila in Rz:
    print(fila)
