# Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
# ingresadas por el usuario.

import matplotlib.pyplot as plt

x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.quiver(0,0,0, x,y,z)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vector en 3D")

plt.show()