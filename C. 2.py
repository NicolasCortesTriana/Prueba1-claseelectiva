# Realice un programa que le permita al usuario ingresar los coeficientes de una función de
# transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
# de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.


import math
import matplotlib.pyplot as plt

wn = float(input("Ingrese la frecuencia natural: "))
zeta = float(input("Ingrese el factor de amortiguamiento: "))

t = [i*0.01 for i in range(0, 1000)]
y = []

for ti in t:
    if zeta < 1:
        wd = wn*math.sqrt(1-zeta*zeta)
        yi = 1 - math.exp(-zeta*wn*ti)*(math.cos(wd*ti) +
             (zeta/math.sqrt(1-zeta*zeta))*math.sin(wd*ti))
        tipo = "Subamortiguado"
    elif zeta == 1:
        yi = 1 - math.exp(-wn*ti)*(1 + wn*ti)
        tipo = "Criticamente amortiguado"
    else:
        a = wn*(zeta + math.sqrt(zeta*zeta - 1))
        b = wn*(zeta - math.sqrt(zeta*zeta - 1))
        yi = 1 - (math.exp(-a*ti) - math.exp(-b*ti))/(2*math.sqrt(zeta*zeta - 1))
        tipo = "Sobreamortiguado"
    y.append(yi)

print("Tipo de sistema:", tipo)

plt.plot(t, y)
plt.xlabel("Tiempo ")
plt.ylabel("Respuesta")
plt.title("funcion de transferencia segundo orden")
plt.grid()
plt.show()