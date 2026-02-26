# Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el
# valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω). Posteriormente realice en Python la
# gráfica

import math
import matplotlib.pyplot as plt

V = float(input("Voltaje : "))
R = float(input("Resistencia : "))
C = float(input("Capacitancia: ")) * 1e-6

t = [i*0.01 for i in range(0, 1000)]
Vc_carga = []
Vc_descarga = []

for ti in t:
    Vc_carga.append(V*(1 - math.exp(-ti/(R*C))))
    Vc_descarga.append(V*math.exp(-ti/(R*C)))

plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")
plt.xlabel("segundos")
plt.ylabel("Voltaje ")
plt.title("Circuito RC")
plt.legend()
plt.grid()
plt.show()