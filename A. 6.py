# Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
# efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
# cilindro para realizar el cálculo.

import math


# DATOS PREVIAMENTE INICIALIZADOS


presion_bar = 6  # presión de trabajo en bar
D_mm = 50        # diámetro del pistón en mm
d_mm = 20        # diámetro del vástago en mm


# CONVERSIONES


P = presion_bar * 100000      # bar -> Pa
D = D_mm / 1000               # mm -> m
d = d_mm / 1000               # mm -> m


# CÁLCULO DE ÁREAS


A_avance = math.pi * (D/2)**2
A_retroceso = A_avance - (math.pi * (d/2)**2)


# CÁLCULO DE FUERZAS


F_avance = P * A_avance
F_retroceso = P * A_retroceso


# MOSTRAR RESULTADOS


print("CILINDRO NEUMÁTICO DE DOBLE EFECTO")
print("----------------------------------")
print(f"Presión: {presion_bar} bar")
print(f"Diámetro pistón: {D_mm} mm")
print(f"Diámetro vástago: {d_mm} mm")

print("\nÁreas:")
print(f"Área avance: {A_avance:.6f} m²")
print(f"Área retroceso: {A_retroceso:.6f} m²")

print("\nFuerzas:")
print(f"Fuerza de avance: {F_avance:.2f} N")
print(f"Fuerza de retroceso: {F_retroceso:.2f} N")
