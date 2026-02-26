# Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C

import math
import matplotlib.pyplot as plt

R0 = 100
A = 3.9083e-3
B = -5.775e-7

T = list(range(-200, 201))
R = []

for t in T:
    R.append(R0 * (1 + A*t + B*t*t))

plt.plot(T, R)

plt.xlabel("Temperatura ")
plt.ylabel("Resistencia ")
plt.title("Sensor PT100")
plt.grid()
plt.show()
