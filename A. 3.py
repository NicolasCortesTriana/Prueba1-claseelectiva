# Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual deben consultar sobre el uso de funciones trigonométricas en Python.

import math

# Coordenadas rectangulares previamente inicializadas
x = 3
y = 4
z = 5


# CILÍNDRICAS

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)  # en radianes


# ESFÉRICAS

rho = math.sqrt(x**2 + y**2 + z**2)

# Evitar división por cero si rho = 0
if rho == 0:
    phi = 0
else:
    phi = math.acos(z / rho)


# IMPRIMIR RESULTADOS
    
print("Coordenadas rectangulares:")
print(f"x = {x}, y = {y}, z = {z}")

print("\nCoordenadas cilíndricas:")
print(f"r = {r:.4f}")
print(f"theta (rad) = {theta:.4f}")
print(f"theta (deg) = {math.degrees(theta):.4f}")
print(f"z = {z}")

print("\nCoordenadas esféricas:")
print(f"rho = {rho:.4f}")
print(f"theta (rad) = {theta:.4f}")
print(f"theta (deg) = {math.degrees(theta):.4f}")
print(f"phi (rad) = {phi:.4f}")
print(f"phi (deg) = {math.degrees(phi):.4f}")

