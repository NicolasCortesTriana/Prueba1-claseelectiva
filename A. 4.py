#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.
# Constantes PT100 IEC 60751
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Temperatura previamente inicializada
T = -20  # °C

# Cálculo de resistencia según rango
if T >= 0:
    R = R0 * (1 + A*T + B*(T**2))
else:
    R = R0 * (1 + A*T + B*(T**2) + C*(T - 100)*(T**3))

print("Cálculo de RTD PT100 (Callendar-Van Dusen)")
print(f"Temperatura = {T} °C")
print(f"Resistencia = {R:.4f} ohmios")